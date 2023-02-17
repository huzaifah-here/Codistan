from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model('model69.h5')


@app.route("/predict", methods=["POST"])
def predict_class(img_path):
    # Load the image using Keras preprocessing
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocess the image
    img_array = img_array / 255

    # Use the pre-trained model to make a prediction
    prediction = model.predict(img_array)

    # Convert the prediction to a class label
    class_label = np.argmax(prediction)

    return class_label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        img_file = request.files['image']


        img_path = 'task5/uploads/' + img_file.filename
        print(img_file)
        img_file.save(img_path)



        class_dict = {0: "Daisy", 1: "Dandelion", 2: "Rose", 3: "Sunflower", 4: "tulip"}

        class_label = predict_class(img_path)
        class_name = class_dict[class_label]

        # Render the prediction result to the web page
        return render_template('result.html', class_label=class_name)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)