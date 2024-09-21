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

    # 5. Explain the two approaches: Survey vs Selection Box
    st.write("""
    We offer two methods to check if you might have Monkeypox based on symptoms:
    
    - **Survey-style**: You'll be asked a series of Yes/No questions about specific symptoms. 
      - **Pros**: Guided and detailed, ensures no symptoms are missed.
      - **Cons**: Takes more time as each symptom has to be answered individually.
    
    - **Selection Box**: You'll simply select from a list of symptoms that you are experiencing.
      - **Pros**: Quicker and more compact.
      - **Cons**: You need to remember all your symptoms and select them carefully.

    Please choose which method you prefer:
    """)

    # 6. Let the user choose between Survey or Selection Box
    choice = st.radio('Which method would you prefer?', ('Survey', 'Selection Box'))

    # 7. Proceed based on the user's choice
    if choice == 'Survey':
        st.write("You selected the **Survey-style** method. Please answer the following questions.")
        
        # 8. Organize the symptoms into columns (for better layout in survey-style)
        symptoms_questions = [
            'Rash', 'Skin lesions', 'Fever', 'Headache', 'Swollen lymph nodes', 'Fatigue', 
            'Loss of appetite', 'Muscle aches', 'Genital ulcers', 'Back pain', 'Cough', 
            'Sore throat', 'Nausea', 'Vomiting', 'Diarrhea', 'Chest pain', 'Abdominal pain', 
            'Shortness of breath', 'Joint pain', 'Conjunctivitis', 'Ear pain', 'Nasal congestion',
            'Bleeding gums', 'Night sweats', 'Dizziness', 'Chills', 'Runny nose', 'Difficulty swallowing',
            'Swelling in arms/legs', 'Blisters', 'Peeling skin', 'Red eyes', 'Dark urine', 'Light stools', 
            'Itchy skin', 'Difficulty breathing', 'Bruising', 'Hearing loss', 'Severe itching', 'Scabs', 
            'Vision loss', 'Dehydration', 'Fever with chills', 'Burning sensation', 'Eye discharge', 
            'Ulcers in mouth'
        ]

        columns = st.columns(3)
        symptom_answers = []
        for i, symptom in enumerate(symptoms_questions):
            col = columns[i % 3]  # Distribute questions across 3 columns
            answer = col.radio(f"Do you have {symptom.lower()}?", ('No', 'Yes'), index=0)
            symptom_answers.append(answer)
        
        symptoms = np.array(symptom_answers)
        symptoms = np.where(symptoms == 'Yes', 1, 0).reshape(1, -1)  # Convert 'Yes' to 1 and 'No' to 0
    
    elif choice == 'Selection Box':
        st.write("You selected the **Selection Box** method. Please select your symptoms from the list.")

        # 9. List of symptoms for multi-selection box
        symptoms_list = [
            'Rash', 'Skin lesions', 'Fever', 'Headache', 'Swollen lymph nodes', 'Fatigue', 
            'Loss of appetite', 'Muscle aches', 'Genital ulcers', 'Back pain', 'Cough', 
            'Sore throat', 'Nausea', 'Vomiting', 'Diarrhea', 'Chest pain', 'Abdominal pain', 
            'Shortness of breath', 'Joint pain', 'Conjunctivitis', 'Ear pain', 'Nasal congestion',
            'Bleeding gums', 'Night sweats', 'Dizziness', 'Chills', 'Runny nose', 'Difficulty swallowing',
            'Swelling in arms/legs', 'Blisters', 'Peeling skin', 'Red eyes', 'Dark urine', 'Light stools', 
            'Itchy skin', 'Difficulty breathing', 'Bruising', 'Hearing loss', 'Severe itching', 'Scabs', 
            'Vision loss', 'Dehydration', 'Fever with chills', 'Burning sensation', 'Eye discharge', 
            'Ulcers in mouth'
        ]
        
        selected_symptoms = st.multiselect('Select your symptoms:', symptoms_list)
        symptoms_input = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]
        symptoms = np.array(symptoms_input).reshape(1, -1)  # Convert to numpy array
    
    # 10. Make prediction if symptoms are provided
    if st.button('Predict'):
        prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
        prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
        if prediction == 1:
            st.error(f"Based on the symptoms, you might have Monkeypox!")
            st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
        else:
            st.success(f"You are likely not infected with Monkeypox.")
            st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# 11. Run the app
if __name__ == '__main__':
    main()
