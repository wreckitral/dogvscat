from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from util import base64_to_pil

print(tf.__version__)

print("MEOW WUFF")

print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))

app = Flask(__name__)

# Load the model
MODEL_PATH = 'models/dogsvscats.keras'
model = tf.keras.models.load_model(MODEL_PATH)
model.make_predict_function()


def model_predict(img, model):
    # Resize image
    img = img.resize((200, 200))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # Predict
    preds = model.predict(x)

    print(preds)

    # Convert prediction to a more readable format
    class_name = 'Dog' if preds[0][0] >= 0.5 else 'Cat'

    print(class_name)
    probability = float(preds[0][0]) if preds[0][0] > 0.5 else float(1 - preds[0][0])

    return {
        'result': class_name,
        'probability': probability
    }


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Ensure the request contains JSON data
    if not request.json:
        return jsonify(error='No input data'), 400

    try:
        # Convert base64 to PIL image
        img = base64_to_pil(request.json)

        # Get prediction
        preds = model_predict(img, model)

        print(preds)

        return jsonify(preds)

    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    # Uncomment the next line if you want to run in debug mode
    # app.run(port=5000, debug=True)

    # Serve the app with gevent
    print("Starting server on http://0.0.0.0:5000")
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()

