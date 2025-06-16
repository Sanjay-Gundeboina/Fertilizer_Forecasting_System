from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pickle
import numpy as np

app = Flask(__name__)

# Load ML model and fertilizer label encoder
model1 = pickle.load(open('classifier.pkl', 'rb'))
ferti = pickle.load(open('fertilizer.pkl', 'rb'))

# Flask config
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and encryption
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    plain_password = db.Column(db.String(200), nullable=False)

# Prediction model
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    crop = db.Column(db.String(80), nullable=False)
    soil = db.Column(db.String(80), nullable=False)
    nitrogen = db.Column(db.Integer, nullable=False)
    phosphorous = db.Column(db.Integer, nullable=False)
    potassium = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    moisture = db.Column(db.Integer, nullable=False)
    predicted_fertilizer = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())

# Home route
@app.route('/')
def home():
    return render_template('home.html', logged_in='user' in session)

# Model prediction page
@app.route('/model')
def model():
    if 'user' not in session:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('login'))
    return render_template('model.html')

# Detail route
@app.route('/detail')
def detail():
    return render_template('detail.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        raw_password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(raw_password).decode('utf-8')

        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash('Username or email already exists.', 'danger')
        else:
            new_user = User(
                username=username,
                email=email,
                password=hashed_password,
                plain_password=raw_password
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('model'))
        else:
            flash('Invalid credentials.', 'danger')

    return render_template('login.html')

# Guest login
@app.route('/guest_login')
def guest_login():
    session['user'] = 'Guest'
    flash('Logged in as Guest!', 'info')
    return redirect(url_for('model'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = request.form.get('temp')
        humi = request.form.get('humid')
        mois = request.form.get('mois')
        soil = request.form.get('soil')
        crop = request.form.get('crop')
        nitro = request.form.get('nitro')
        pota = request.form.get('pota')
        phosp = request.form.get('phos')
        
        values = [temp, humi, mois, soil, crop, nitro, pota, phosp]

        if None in values or any(v.strip() == '' for v in values):
            return render_template('model.html', x='Please fill all the fields.')

        inputs = [int(v) for v in values]
        prediction = model1.predict([inputs])[0]

        # Decode label
        try:
            result = ferti.inverse_transform([prediction])[0]
        except:
            result = ferti.classes_[prediction] if hasattr(ferti, 'classes_') else str(prediction)

        # Save prediction
        if 'user' in session:
            new_prediction = Prediction(
                username=session['user'],
                crop=crop,
                soil=soil,
                nitrogen=int(nitro),
                phosphorous=int(phosp),
                potassium=int(pota),
                temperature=int(temp),
                humidity=int(humi),
                moisture=int(mois),
                predicted_fertilizer=result
            )
            db.session.add(new_prediction)
            db.session.commit()

        return render_template('model.html', x=result)

    except Exception as e:
        return render_template('model.html', x=f"Error: {str(e)}")

# Run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
