from flask import Flask, request, render_template
from text_analysis_utils import analyze, normalize_words, word_counter, char_cuonter, no_space_char_counter, line_counter
from text_analysis_utils import sentence_counter
from werkzeug.utils import secure_filename
from model import Analysis, Session

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
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
            with Session.begin() as session:
                analysis = Analysis(
                    text = raw_text,
                    words = result["words"],
                    num_of_char = result["characters_without_spaces"],
                    num_of_char_and_space = result["characters_with_spaces"],
                    num_of_lines = result["lines"],
                    num_of_sentence = result["sentences"],
                    five_common_words = result["five_common_words"],
                    average_length = result["average_length"]
                )
                session.add(analysis)
            return render_template('result.html', analysis=analysis )
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
                with Session.begin() as session:
                    analysis = Analysis(
                        text = raw_text,
                        words = result["words"],
                        num_of_char = result["characters_without_spaces"],
                        num_of_char_and_space = result["characters_with_spaces"],
                        num_of_lines = result["lines"],
                        num_of_sentence = result["sentences"],
                        five_common_words = result["five_common_words"],
                        average_length = result["average_length"]
                    )
                    session.add(analysis)
                return render_template('result.html', analysis=analysis)
            else:
                return render_template('uploader.html', error = "The file was empty, upload another file.")  
            
        else:
            return render_template('uploader.html', error="Please upload a file")

@app.route('/history', methods = ['GET'])
def history():
    session = Session()
    result = session.query(Analysis).all()
    session.close()
    return render_template('history.html', analysis=result)

if __name__ == "__main__":
    app.run(debug=True)