from flask import Flask, render_template, request

from utils.binge_api import BingeApi
from utils.file_utils import FileUtils

app = Flask(__name__)
file_utils = FileUtils()


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["uploaded_file"]
    file_extension = file_utils.get_file_extension_from_file_name(file.filename)
    file_content_bytes = file.stream.read()

    question = file_utils.get_content_from_stream(extension=file_extension, file_data_stream=file_content_bytes)

    return render_template("Question_form.html", paragraph=question)


@app.route("/submit", methods=["POST"])
def submit():
    body = request.form
    api = BingeApi()
    response = api.getAnswerFromApi(
        paragraph=body["paragraph"], question=body["question"]
    )
    return {"response": response}


@app.route("/")
def home():
    return render_template("upload_file.html")
