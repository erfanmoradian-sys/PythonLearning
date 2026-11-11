from flask import Flask, request, render_template, redirect, url_for, flash
from text_analysis_utils import analyze, normalize_words, word_counter, char_cuonter, no_space_char_counter, line_counter
from text_analysis_utils import sentence_counter
from werkzeug.utils import secure_filename
from model import Analysis, Session, User
from flask_wtf import FlaskForm
from forms import Registration_Form, Login_Form
from werkzeug.security import generate_password_hash
from sqlalchemy import select
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    with Session() as session:
        return session.get(User, int(user_id))



@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/entertext', methods=['GET', 'POST'])
@login_required
def enter_text():
    if request.method == 'GET':
        return render_template('entertext.html')
    else:
        raw_text = request.form.get('raw_text')
        if raw_text and raw_text.strip():
            cleaned_text = normalize_words(raw_text)
            result = analyze(raw_text, cleaned_text)
            with Session.begin() as session:
                analysis = Analysis(
                    text = raw_text,
                    words = result["words"],
                    num_of_char = result["characters_without_spaces"],
                    num_of_char_and_space = result["characters_with_spaces"],
                    num_of_lines = result["lines"],
                    num_of_sentence = result["sentences"],
                    five_common_words = result["five_common_words"],
                    average_length = result["average_length"],
                    user_id=current_user.id
                )
                session.add(analysis)
            return render_template('result.html', analysis=analysis )
        else:
            return render_template('entertext.html', error = "Text is empty.")

@app.route('/uploader', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'GET':
        return render_template('uploader.html')
    else:
        uploaded_file = request.files.get('file')
        if uploaded_file :
            filename = secure_filename(uploaded_file.filename)
            raw_text = uploaded_file.read().decode('utf-8')
            
            if raw_text and raw_text.strip():
                cleaned_text = normalize_words(raw_text)
                result = analyze(raw_text, cleaned_text)
                with Session.begin() as session:
                    analysis = Analysis(
                        text = raw_text,
                        words = result["words"],
                        num_of_char = result["characters_without_spaces"],
                        num_of_char_and_space = result["characters_with_spaces"],
                        num_of_lines = result["lines"],
                        num_of_sentence = result["sentences"],
                        five_common_words = result["five_common_words"],
                        average_length = result["average_length"],
                        user_id = current_user.id
                    )
                    session.add(analysis)
                return render_template('result.html', analysis=analysis)
            else:
                return render_template('uploader.html', error = "The file was empty, upload another file.")  
            
        else:
            return render_template('uploader.html', error="Please upload a file")

@app.route('/history', methods = ['GET'])
@login_required
def history():
    with Session() as session:
        result = session.scalars(select(Analysis).where(Analysis.user_id==current_user.id)).all()
    return render_template('history.html', analysis=result)

@app.route("/register", methods = ['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration_Form()
    if request.method == "GET":
        return render_template("register.html", form=form)
    else:
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            with Session() as session:
                existing_email = session.scalar(select(User).where(User.email == email))
                existing_username = session.scalar(select(User).where(User.username == username))
                if existing_email:
                    form.email.errors.append("Email already exists.")
                if existing_username:
                    form.username.errors.append("Username already exists")
                if existing_email or existing_username: 
                    return render_template('register.html', form = form)
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(username=username, email=email, password=hashed_password)
                session.add(user)
                session.commit()
            
            flash(f"Account created for {username}. Login to your account", "success")
            return redirect(url_for("login"))
        else:
             return render_template("register.html", form=form)


    
@app.route("/login", methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login_Form()
    if request.method == "GET":
        return render_template('login.html', form = form)
    else:
        if form.validate_on_submit():
            with Session() as session:
                stmt = select(User).where(User.email==form.email.data)
                user = session.execute(stmt).scalar_one_or_none()
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    next_page = request.args.get('next')
                    if next_page:
                        return redirect(next_page)
                    else:
                        return redirect(url_for("home"))
                else:
                    flash(f"Login unsuccessful, check email and password.", 'error')
        return render_template('login.html', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)