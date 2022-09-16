from flask import Flask, render_template, flash, redirect, request, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os
import Testing_Model

UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
Bootstrap(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', "jpeg", 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'files[]' not in request.files:
        flash('No file part')
        return redirect(request.url)
    files = request.files.getlist('files[]')
    file_names = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_names.append(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print('static/uploads/'+filename)
            res = Testing_Model.detect('static/uploads/'+filename)
            print(res[0])
            return render_template('index.html', filenames=file_names, result=res[0])

    # else:
    #	flash('Allowed image types are -> png, jpg, jpeg, gif')
    #	return redirect(request.url)

    return render_template('index.html', filenames=file_names)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run()