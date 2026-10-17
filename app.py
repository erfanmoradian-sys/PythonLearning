from flask import Flask, request, render_template
from text_analysis_utils import analyze, normalize_words
from werkzeug.utils import secure_filename
from model import Analysis, Session

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/entertext', methods=['GET', 'POST'])
def enter_text():
    if request.method == 'GET':
        return render_template('entertext.html')
    else:
        raw_text = request.form.get('raw_text')
        if raw_text and raw_text.strip():
            cleaned_text = normalize_words(raw_text)
            result = analyze(raw_text, cleaned_text)
            session = Session()
            analysis = Analysis(text = raw_text)
            session.add(analysis)
            session.commit()
            session.close()
            return render_template('result.html', result=result )
        else:
            return render_template('entertext.html', error = "Text is empty.")

@app.route('/uploader', methods=['GET', 'POST'])
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
                session = Session()
                analysis = Analysis(text = raw_text)
                session.add(analysis)
                session.commit()
                session.close()
                return render_template('result.html', result=result)
            else:
                return render_template('uploader.html', error = "The file was empty, upload another file.")  
            
        else:
            return render_template('uploader.html', error="Please upload a file")

@app.route('/history', methods = ['GET'])
def history():
    if request.method == 'GET':
        session = Session()
        result = session.query(Analysis).all()
        return render_template('history.html', analysis=result)

if __name__ == "__main__":
    app.run(debug=True)