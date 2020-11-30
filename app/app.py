import tensorflow as tf
from tensorflow import keras
import numpy as np
import imghdr
import io
import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import cv2
from pymongo import MongoClient
from PIL import Image

if __name__ == "__main__":
    app.run()

client = MongoClient("mongodb+srv://xzk276847287:xzk2514764@cluster0.irwbb.mongodb.net/<dbname>?retryWrites=true&w=majority")
mydatabase = client.BD36
mycollection = mydatabase.fashionMnist

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config['UPLOAD_PATH'] = 'uploads/image'

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(uploaded_file.filename)))
        img = cv2.imread('uploads//image//' + filename, 0)
        dsize = (28, 28)
        img = cv2.resize(img, dsize)
        img = (np.expand_dims(img, 0))
        predictions_single = probability_model.predict(img)
        print(predictions_single)
        vals = np.argmax(predictions_single[0])
        image_file = Image.open('uploads//image//' + filename)

        imgByteArr = io.BytesIO()
        image_file.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        rec = {
            "image": imgByteArr,
            "tag": class_names[vals]
        }
        rec = mycollection.insert_one(rec)

    return render_template('pred.html', ss = class_names[vals])