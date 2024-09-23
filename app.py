from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, static_url_path='/static')

# Define a folder for storing uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # List all image files in the upload folder
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Save the uploaded image to the upload folder
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    return redirect(url_for('index'))

@app.route('/delete/<image_name>')
def delete(image_name):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    if os.path.exists(image_path):
        os.remove(image_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
