# Fertilizer_Forecasting_System
🌾 **Fertilizer Recommendation System**
This project is a Fertilizer Recommendation System that assists farmers in selecting the most appropriate fertilizers for their crops. It considers various environmental and soil parameters to make precise fertilizer suggestions, ultimately helping improve crop yield and reduce the cost of excessive or unnecessary fertilizer usage.

**🔐 User Authentication (Login System)**
A user login page is implemented to provide personalized access to the system. Users must log in to submit their data and receive fertilizer recommendations.

✅ Features:
Secure login form

Username and password validation

Basic session management using Flask

Redirect to home page after successful login

This feature allows only authorized users to access the model interface and submit input, adding a layer of security and personalization to the system.
**
📌 Fertilizer Recommendation**
Fertilizer recommendation involves suggesting the best types and quantities of fertilizers based on:

Soil composition

Temperature

Humidity

Moisture levels

Crop type

This project automates the recommendation process using machine learning, providing quick, personalized guidance for farmers and agricultural experts.

📊 Dataset Information
The project uses a structured dataset containing key agricultural variables:

Nitrogen – Nitrogen content in soil

Phosphorus – Phosphorus content in soil

Potassium – Potassium content in soil

Temperature – Ambient temperature

Humidity – Relative humidity

Moisture – Soil moisture

Soil Type – Type of soil (e.g., clay, sandy)

Crop Type – Type of crop (e.g., rice, wheat)

Fertilizer Name – Suitable fertilizer recommendation

🧠 Machine Learning Algorithms Used
Several algorithms were tested for this system:

Logistic Regression

Naive Bayes

Random Forest (✅ Used in final model)

Decision Tree

Support Vector Machine (SVM)

Random Forest achieved high accuracy and was chosen for model deployment.

🛠️ Main Python Script
Built with Flask, the app handles:

User login

Input form submission

ML prediction logic

Result display

Run the app:

bash
Copy
Edit
python app.py
Then visit http://127.0.0.1:5000/.

🌐 Website Features
🏠 Home Page
Overview of the system

Form to enter:

Nitrogen, Phosphorus, Potassium

Temperature, Humidity, Moisture

Soil and Crop types

🔐 Login Page
Simple login form

Redirect to home page after login

Basic authentication logic

📈 Result Page
Displays recommended fertilizer

Personalized output

🧰 Technologies Used
Technology	Purpose
Python	Backend logic, ML modeling
Flask	Web framework
HTML/CSS	Structure and style
Bootstrap	Responsive design
JavaScript	Interactivity
NumPy & pandas	Data manipulation
Matplotlib & Seaborn	Visualization
SQLite / File-based Auth	(Optional) User data storage

📁 Project Structure
csharp
Copy
Edit
Fertilizer_Recommendation_System/
│
├── app.py                     # Flask application
├── templates/
│   ├── login.html             # Login Page
│   ├── home.html             # Input Form
│   └── model.html             # Result Page
├── static/
│   └── images           
├── model/
│   └── fertilizer_model.pkl   # Trained ML model
├── dataset/
│   └── fertilizer_data.csv    # Dataset
├── requirements.txt
└── README.md
**📦 Requirements**
Install all dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Sample requirements.txt:

nginx
Copy
Edit
Flask
numpy
pandas
scikit-learn
matplotlib
seaborn

