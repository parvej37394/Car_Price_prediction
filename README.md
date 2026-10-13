-----------## Car Price Predictor

An end-to-end Machine Learning web application built with **Flask**, **Pandas**, and **Scikit-learn** to estimate the selling price of used cars based on user inputs such as company, model, purchase year, kilometers driven, and fuel type.

---

##  Tech Stack & Tools

* **Programming Language:** Python 3.x
* **Machine Learning & Data Analysis:** Pandas, NumPy, Scikit-Learn
* **Web Framework:** Flask, Jinja2 Templates
* **Frontend:** HTML5, CSS3, JavaScript

---

------- Project Structure------------------------

```text
├── templates/
│   ├── index.html       # Base layout & input form
│   └── predict.html     # Results display page
├── static/
│   ├── css/
│   │   └── style.css    # Custom styling
│   └── js/
│       └── script.js    # Dynamic dropdown logic
├── app.py               # Flask application server
├── LinearRegressionmodel (1).pkl # Pre-trained ML model
└── clend_data (3).csv   # Cleaned dataset
