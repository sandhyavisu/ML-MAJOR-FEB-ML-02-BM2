import streamlit as st
import sklearn
import scikit_learn==0.24.1
import joblib
model = joblib.load('Email_Class')
st.title('viral/limited Classifier')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
  
