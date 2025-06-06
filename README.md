---

````markdown
# 🧠 Chronic Kidney Disease (CKD) Prediction Web App

This is a lightweight web application built with **Flask** that predicts the presence of **Chronic Kidney Disease (CKD)** based on key clinical features. It uses a trained **Decision Tree model** and is part of the larger project:  
👉 [Multi-Disease Prediction System](https://github.com/deoprakash/multi_disease_prediction)

---

## 📊 Dataset

- **Source:** Kaggle  
  [Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease)
- A subset of features from the original dataset was selected for better performance:
  - `hemo` (Hemoglobin)
  - `sg` (Specific Gravity)
  - `sc` (Serum Creatinine)
  - `htn` (Hypertension)
  - `sod` (Sodium)
  - `bgr` (Blood Glucose Random)

---

## 🚀 Features

- Web-based CKD prediction from user input
- Trained Decision Tree model
- Clean HTML/CSS frontend using Flask templates
- Label encoding for categorical values (e.g., hypertension)
- Error handling for invalid inputs

---

## 🗂️ Project Structure

```markdown
ckd_prediction_app/
├── static/                      # CSS and static assets
├── templates/                   # HTML templates (index.html)
├── venv/                        # Virtual environment (optional)
├── app.py                       # Flask application
├── ckd_important_features.pkl   # Selected feature list
├── ckd_label_encoder.pkl        # Encoded labels for prediction
├── decision_tree_ckd_model.pkl  # Trained model file
├── kidney_disease.xlsx          # Original dataset file (optional)
└── requirements.txt             # Dependencies
````

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ckd_prediction_app.git
cd ckd_prediction_app
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

Then open your browser and go to:
[http://localhost:5000](http://localhost:5000)

---

## 🌐 Hosting Options

You can deploy this Flask app using:

* [Render](https://render.com/)
* [Railway](https://railway.app/)
* [Streamlit Cloud (if converted)](https://streamlit.io/cloud)
* \[Heroku (deprecated free tier)]

---

## 🔗 Related Project

This app is part of a larger system for multiple disease predictions:
➡️ [Multi-Disease Prediction Main Project](https://github.com/deoprakash/multi_disease_prediction)

---

## 👩‍💻 Author

Made with ❤️ by **Arya Singh**

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

```

---
```
