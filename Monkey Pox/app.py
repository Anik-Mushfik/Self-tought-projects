# 1. Import necessary libraries
import streamlit as st
import numpy as np
import joblib

# 2. Load the trained Random Forest model
model = joblib.load('random_forest_monkeypox_model.pkl')

# 3. Define the application
def main():
    # 4. Title of the app
    st.title("Monkeypox Prediction App")
    st.write("Answer the following questions to check if you might have Monkeypox based on symptoms.")

    # 5. Questions related to Monkeypox symptoms (User inputs)
    rash = st.selectbox('Do you have a rash?', ('No', 'Yes'))
    skin_lesions = st.selectbox('Do you have skin lesions?', ('No', 'Yes'))
    fever = st.selectbox('Do you have a fever?', ('No', 'Yes'))
    headache = st.selectbox('Do you have headaches?', ('No', 'Yes'))
    lymphadenopathy = st.selectbox('Do you have swollen lymph nodes (lymphadenopathy)?', ('No', 'Yes'))
    fatigue = st.selectbox('Do you feel fatigued?', ('No', 'Yes'))
    loss_of_appetite = st.selectbox('Have you lost your appetite?', ('No', 'Yes'))
    muscle_aches = st.selectbox('Do you have muscle aches?', ('No', 'Yes'))
    genital_ulcers = st.selectbox('Do you have genital ulcers?', ('No', 'Yes'))
    
    # 6. Convert the inputs into a format the model can understand (0 for No, 1 for Yes)
    symptoms = np.array([rash, skin_lesions, fever, headache, lymphadenopathy, fatigue, 
                         loss_of_appetite, muscle_aches, genital_ulcers])
    symptoms = np.where(symptoms == 'Yes', 1, 0).reshape(1, -1)  # Reshape to 2D array
    
    # 7. Make prediction
    if st.button('Predict'):
        prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
        prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
        if prediction == 1:
            st.error(f"Based on the symptoms, you might have Monkeypox!")
            st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
        else:
            st.success(f"You are likely not infected with Monkeypox.")
            st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# 8. Run the app
if __name__ == '__main__':
    main()
