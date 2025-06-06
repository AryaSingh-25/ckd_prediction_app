from flask import Flask, request, render_template_string, send_from_directory
import joblib
import os

app = Flask(__name__)

# Load model and encoders
model = joblib.load("decision_tree_ckd_model.pkl")
label_encoder = joblib.load("ckd_label_encoder.pkl")
important_features = joblib.load("ckd_important_features.pkl")  # ['hemo', 'sg', 'sc', 'htn', 'sod', 'bgr']

# Route to serve style.css from current directory
@app.route("/style.css")
def serve_css():
    return send_from_directory(directory=os.getcwd(), path="style.css")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            input_values = []
            for feature in important_features:
                value = request.form.get(feature)
                if feature == 'htn':
                    value = 1 if value.lower() in ['yes', '1', 'true'] else 0
                else:
                    value = float(value)
                input_values.append(value)

            prediction_numeric = model.predict([input_values])[0]
            prediction = label_encoder.inverse_transform([prediction_numeric])[0]
        except Exception as e:
            prediction = f"Error in input: {e}"

    # Load HTML and render
    with open("index.html", "r") as f:
        html_content = f.read()

    return render_template_string(html_content, features=important_features, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
