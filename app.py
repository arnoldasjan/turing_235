from flask import Flask, request, redirect
import pickle
import numpy as np
import json

app = Flask(__name__)

SAVED_MODEL_PATH = "classifier.pkl"

classifier = pickle.load(open(SAVED_MODEL_PATH, "rb"))


def __process_input(request_data: str) -> np.array:
    list_of_dicts = json.loads(request_data)["inputs"]
    list_of_lists = [list(d.values()) for d in list_of_dicts]
    parsed_body = np.asarray(list_of_lists)
    return parsed_body


@app.route('/')
def hello_world():
    return redirect("https://github.com/arnoldasjan/turing_235")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_params = __process_input(request.data)
        predictions = classifier.predict(input_params)

        return json.dumps({"Predicted prices in $1000's": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500


if __name__ == '__main__':
    app.run()
