import streamlit as st
import numpy as np
import pickle
import base64

# Set background image with a .gif and dark theme
def set_bg():
    with open("heart_background.gif", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/gif;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #111111 !important;
        }}

        /* Make all form labels and text dark */
        label, .css-1v3fvcr, .css-1d391kg, .css-10trblm, .css-15zrgzn, .css-1cpxqw2 {{
            color: #111111 !important;
            font-weight: 600;
        }}

        /* Input, select, textarea */
        .stTextInput > div > div > input,
        .stNumberInput > div > input,
        .stSelectbox > div > div > div,
        .stTextArea > div > textarea {{
            background-color: #f5f5f5 !important;
            color: black !important;
        }}

        /* Button styling */
        .stButton > button {{
            background-color: #dddddd !important;
            color: black !important;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# Load the trained model
model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Title
st.title('❤️ Heart Disease Prediction System')

# Feature Descriptions
with st.expander("ℹ️ Feature Descriptions (click to expand)"):
    st.markdown("""
- **age**: Patient’s age in years  
- **sex**: 1 = Male, 0 = Female  
- **cp (Chest pain type)**:  
  0 = Typical angina, 1 = Atypical angina,  
  2 = Non-anginal pain, 3 = Asymptomatic  
- **trestbps**: Resting blood pressure (mm Hg)  
- **chol**: Serum cholesterol (mg/dl)  
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = True, 0 = False)  
- **restecg**:  
  0 = Normal, 1 = ST-T abnormality, 2 = LV hypertrophy  
- **thalach**: Max heart rate achieved  
- **exang**: Exercise-induced angina (1 = Yes, 0 = No)  
- **oldpeak**: ST depression induced by exercise (in mm)  
- **slope**:  
  0 = Upsloping, 1 = Flat, 2 = Downsloping  
- **ca**: No. of major vessels colored by fluoroscopy (0–3)  
- **thal**: 3 = Normal, 6 = Fixed defect, 7 = Reversible defect  
    """)

# Input Fields
st.markdown("### 🩺 Enter Patient's Medical Details:")

age = st.number_input('Age', min_value=1, max_value=120, value=50)
sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3], format_func=lambda x: [
    'Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
trestbps = st.number_input('Resting Blood Pressure (mm Hg)', 80, 200, 120)
chol = st.number_input('Serum Cholesterol (mg/dl)', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'False' if x == 0 else 'True')
restecg = st.selectbox('Resting ECG Results', [0, 1, 2], format_func=lambda x: [
    'Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'][x])
thalach = st.number_input('Max Heart Rate Achieved', 60, 220, 150)
exang = st.selectbox('Exercise-Induced Angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
oldpeak = st.number_input('ST Depression (Oldpeak)', 0.0, 10.0, 1.0)
slope = st.selectbox('Slope of ST Segment', [0, 1, 2], format_func=lambda x: [
    'Upsloping', 'Flat', 'Downsloping'][x])
ca = st.selectbox('Number of Major Vessels (0–3)', [0, 1, 2, 3])
thal = st.selectbox('Thalassemia', [3, 6, 7], format_func=lambda x: {
    3: 'Normal', 6: 'Fixed defect', 7: 'Reversible defect'}[x])

# Prediction
if st.button('🔍 Predict Heart Disease'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success('✅ The person does NOT have heart disease.')
    else:
        st.error('⚠️ The person HAS heart disease.')

# Footer Signature
st.markdown("---")
st.markdown("<center><b>Developed by YASH SHARMA</b></center>", unsafe_allow_html=True)
