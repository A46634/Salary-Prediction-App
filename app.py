import streamlit as st
import joblib
import numpy as np

model = joblib.load("./salary_predictor.joblib")

st.title("💰 Salary Prediction App ")

experience = st.selectbox("🐱‍💻 Experience Level", ["Entry Level", "Mid Level", "Senior Level", "Executive Level"])
employment = st.selectbox("📃 Employment Type", ["Full Time", "Part Time", "Contract", "Freelance"])
job_title = st.selectbox("👔 Job Title ", ['3D Computer Vision Researcher', 'AI Scientist', 'Analytics Engineer', 'Applied Data Scientist', 'Applied Machine Learning Scientist', 'BI Data Analyst', 'Big Data Architect', 'Big Data Engineer', 'Business Data Analyst', 'Cloud Data Engineer', 'Computer Vision Engineer', 'Data Analyst', 'Data Analytics Engineer', 'Data Analytics Lead', 'Data Analytics Manager', 'Data Architect', 'Data Engineer', 'Data Engineering Manager', 'Data Science Consultant', 'Data Science Engineer', 'Data Science Manager', 'Data Scientist', 'Data Specialist', 'Director of Data Engineering', 'Director of Data Science', 'ETL Developer', 'Financial Data Analyst', 'Head of Data Science', 'Head of Machine Learning', 'Lead Data Analyst', 'Lead Data Engineer', 'Lead Data Scientist', 'Lead Machine Learning Engineer', 'Machine Learning Developer', 'Machine Learning Engineer', 'Machine Learning Infrastructure Engineer', 'Machine Learning Manager', 'Machine Learning Scientist', 'Marketing Data Analyst', 'Principal Data Scientist', 'Product Data Analyst', 'Research Scientist', 'Staff Data Scientist'])
residence = st.selectbox("🏡 Employee Residence", ["United Arab Emirates", "Argentina", "Austria", "Australia", "Belgium", "Bulgaria", "Bolivia", "Brazil", "Canada", "Switzerland", "Chile", "Canada", "Colombia", "Czechia", "Germany", "Denmark", "Algeria", "Estonia", "Spain", "France", "United Kingdom","Greece", "Hong Kong", "Honduras", "Croatia", "Hungary", "Ireland", "India", "Iraq", "Iran", "Italy", "Jersey", "Japan", "Kenya", "Luxembourg", "Moldova", "Malta", "Mexico", "Malaysia", "Nigeria", "Netherlands", "New Zealand", "Philippines", "Pakistan", "Poland", "Puerto Rico", "Portugal", "Romania", "Serbia", "Russia", "Singapore", "Slovenia", "Tunisia", "Turkey", "Ukraine", "United States", "Vietnam"])
remote_ratio = st.selectbox("🌓 Remote Ratio", [0, 50, 100])
company_location = st.selectbox("🏢 Company Location", ["United Arab Emirates", "American Samoa", "Austria", "Australia", "Belgium", "Brazil", "Canada", "Switzerland", "Chile", "China", "Colombia", "Czechia", "Germany", "Denmark", "Algeria", "Estonia", "Spain", "France", "United Kingdom", "Greece", "Honduras", "Croatia", "Hungary", "Ireland", "Israel", "India", "Iraq", "Iran", "Italy", "Japan", "Kenya", "Luxembourg", "Moldova", "Malta", "Mexico", "Malaysia", "Nigeria", "Netherlands", "New Zealand", "Pakistan", "Poland", "Portugal", "Romania", "Russia", "Singapore", "Slovenia", "Turkey", "Ukraine", "United States", "Vietnam"])
company_size = st.selectbox("🏗 Company Size (ie Small, Medium, Large)", ["S", "M", "L"])

if st.button("Predict Salary"):
    data = {
        "experience_level": [experience],
        "employment_type": [employment],
        "job_title": [job_title],
        "employee_residence": [residence],
        "remote_ratio": [remote_ratio],
        "company_location": [company_location],
        "company_size": [company_size]
    }

    import pandas as pd

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]
    st.success(f"Estimated Salary 🤑: ${prediction:,.2f} USD")

