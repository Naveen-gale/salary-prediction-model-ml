
import streamlit as st
import pandas as pd
import joblib


st.title("salary prediction model")

model = joblib.load("Salary_model.pkl")

age = st.slider("Select your age:", 0, 100, 25)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
Job_title = st.text_input("Enter your job title:")
education = st.selectbox("Select your education level:", ["High School", "Bachelor's", "Master's", "PhD"])
experience = st.slider("Enter your years of experience:", 0, 50, 5)



 

if st.button("Predict Salary"):

    # Update these values based on your training encoding
    gender_map = {
        "Male": 1,
        "Female": 0
    }

    education_map = {
        "Bachelor's": 0,
        "Master's": 1,
        "PhD": 2
    }

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_map[gender]],
        "Education Level": [education_map[education]],
        "Job Title": [0],  # temporary
        "Years of Experience": [experience]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")