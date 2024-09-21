
# Check box

# # 1. Import necessary libraries
# import streamlit as st
# import numpy as np
# import joblib

# # 2. Load the trained Random Forest model
# model = joblib.load('random_forest_monkeypox_model.pkl')

# # 3. Define the application
# def main():
#     # 4. Title of the app
#     st.title("Monkeypox Prediction App")
#     st.write("Answer the following questions to check if you might have Monkeypox based on symptoms.")

#     # 5. Questions related to Monkeypox symptoms (User inputs using checkboxes)
#     rash = st.checkbox('Do you have a rash?')
#     skin_lesions = st.checkbox('Do you have skin lesions?')
#     fever = st.checkbox('Do you have a fever?')
#     headache = st.checkbox('Do you have headaches?')
#     lymphadenopathy = st.checkbox('Do you have swollen lymph nodes (lymphadenopathy)?')
#     fatigue = st.checkbox('Do you feel fatigued?')
#     loss_of_appetite = st.checkbox('Have you lost your appetite?')
#     muscle_aches = st.checkbox('Do you have muscle aches?')
#     genital_ulcers = st.checkbox('Do you have genital ulcers?')

    
    
#     # 6. Convert the inputs into a format the model can understand (0 for No, 1 for Yes)
#     symptoms = np.array([rash, skin_lesions, fever, headache, lymphadenopathy, fatigue, 
#                          loss_of_appetite, muscle_aches, genital_ulcers]).astype(int).reshape(1, -1)  # Convert booleans to integers
    
#     # 7. Make prediction
#     if st.button('Predict'):
#         prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
#         prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
#         if prediction == 1:
#             st.error(f"Based on the symptoms, you might have Monkeypox!")
#             st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
#         else:
#             st.success(f"You are likely not infected with Monkeypox.")
#             st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# # 8. Run the app
# if __name__ == '__main__':
#     main()




# Radio Button

# # 1. Import necessary libraries
# import streamlit as st
# import numpy as np
# import joblib

# # 2. Load the trained Random Forest model
# model = joblib.load('random_forest_monkeypox_model.pkl')

# # 3. Define the application
# def main():
#     # 4. Title of the app
#     st.title("Monkeypox Prediction App")
#     st.write("Answer the following questions to check if you might have Monkeypox based on symptoms.")

#     # 5. Questions related to Monkeypox symptoms (User inputs using radio buttons)
#     rash = st.radio('Do you have a rash?', ('No', 'Yes'))
#     skin_lesions = st.radio('Do you have skin lesions?', ('No', 'Yes'))
#     fever = st.radio('Do you have a fever?', ('No', 'Yes'))
#     headache = st.radio('Do you have headaches?', ('No', 'Yes'))
#     lymphadenopathy = st.radio('Do you have swollen lymph nodes (lymphadenopathy)?', ('No', 'Yes'))
#     fatigue = st.radio('Do you feel fatigued?', ('No', 'Yes'))
#     loss_of_appetite = st.radio('Have you lost your appetite?', ('No', 'Yes'))
#     muscle_aches = st.radio('Do you have muscle aches?', ('No', 'Yes'))
#     genital_ulcers = st.radio('Do you have genital ulcers?', ('No', 'Yes'))
    
#     # 6. Convert the inputs into a format the model can understand (0 for No, 1 for Yes)
#     symptoms = np.array([
#         rash, skin_lesions, fever, headache, lymphadenopathy, fatigue, 
#         loss_of_appetite, muscle_aches, genital_ulcers
#     ])
    
#     symptoms = np.where(symptoms == 'Yes', 1, 0).reshape(1, -1)  # Convert 'Yes' to 1 and 'No' to 0
    
#     # 7. Make prediction
#     if st.button('Predict'):
#         prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
#         prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
#         if prediction == 1:
#             st.error(f"Based on the symptoms, you might have Monkeypox!")
#             st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
#         else:
#             st.success(f"You are likely not infected with Monkeypox.")
#             st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# # 8. Run the app
# if __name__ == '__main__':
#     main()



# # 1. Import necessary libraries
# import streamlit as st
# import numpy as np
# import joblib

# # 2. Load the trained Random Forest model
# model = joblib.load('random_forest_monkeypox_model.pkl')

# # 3. Define the application
# def main():
#     # 4. Title of the app
#     st.title("Monkeypox Prediction App")
#     st.write("Answer the following questions to check if you might have Monkeypox based on symptoms.")

#     # 5. Questions related to Monkeypox symptoms (User inputs using radio buttons in columns for side-by-side display)
#     col1, col2 = st.columns(2)
    
#     with col1:
#         rash = st.radio('Do you have a rash?', ('No', 'Yes'), index=0)
#         fever = st.radio('Do you have a fever?', ('No', 'Yes'), index=0)
#         lymphadenopathy = st.radio('Swollen lymph nodes (lymphadenopathy)?', ('No', 'Yes'), index=0)
#         fatigue = st.radio('Do you feel fatigued?', ('No', 'Yes'), index=0)
#         muscle_aches = st.radio('Do you have muscle aches?', ('No', 'Yes'), index=0)

#     with col2:
#         skin_lesions = st.radio('Do you have skin lesions?', ('No', 'Yes'), index=0)
#         headache = st.radio('Do you have headaches?', ('No', 'Yes'), index=0)
#         loss_of_appetite = st.radio('Have you lost your appetite?', ('No', 'Yes'), index=0)
#         genital_ulcers = st.radio('Do you have genital ulcers?', ('No', 'Yes'), index=0)

#     # 6. Convert the inputs into a format the model can understand (0 for No, 1 for Yes)
#     symptoms = np.array([
#         rash, skin_lesions, fever, headache, lymphadenopathy, fatigue, 
#         loss_of_appetite, muscle_aches, genital_ulcers
#     ])
    
#     symptoms = np.where(symptoms == 'Yes', 1, 0).reshape(1, -1)  # Convert 'Yes' to 1 and 'No' to 0
    
#     # 7. Make prediction
#     if st.button('Predict'):
#         prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
#         prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
#         if prediction == 1:
#             st.error(f"Based on the symptoms, you might have Monkeypox!")
#             st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
#         else:
#             st.success(f"You are likely not infected with Monkeypox.")
   
# # 8. Run the app
# if __name__ == '__main__':
#     main()




# # 1. Import necessary libraries
# import streamlit as st
# import numpy as np
# import joblib

# # 2. Load the trained Random Forest model
# model = joblib.load('random_forest_monkeypox_model.pkl')

# # 3. Define the application
# def main():
#     # 4. Title of the app
#     st.title("Monkeypox Prediction App")
#     st.write("Answer the following questions to check if you might have Monkeypox based on symptoms.")
    
#     # 5. Organize the symptoms into columns (let's use 3 columns for better layout)
#     symptoms_questions = [
#         'Rash', 'Skin lesions', 'Fever', 'Headache', 'Swollen lymph nodes', 'Fatigue', 
#         'Loss of appetite', 'Muscle aches', 'Genital ulcers', 'Back pain', 'Cough', 'Sore throat', 
#         'Nausea', 'Vomiting', 'Diarrhea', 'Chest pain', 'Abdominal pain', 'Shortness of breath', 
#         'Joint pain', 'Conjunctivitis', 'Ear pain', 'Nasal congestion', 'Bleeding gums', 'Night sweats',
#         'Dizziness', 'Chills', 'Runny nose', 'Difficulty swallowing', 'Swelling in arms/legs', 
#         'Blisters', 'Peeling skin', 'Red eyes', 'Dark urine', 'Light stools', 'Itchy skin', 
#         'Difficulty breathing', 'Bruising', 'Hearing loss', 'Severe itching', 'Scabs', 'Vision loss',
#         'Dehydration', 'Fever with chills', 'Burning sensation', 'Eye discharge', 'Ulcers in mouth'
#     ]

#     # 6. Create columns (3 columns to organize symptoms better)
#     columns = st.columns(3)
    
#     # 7. Ask questions using radio buttons for all symptoms
#     symptom_answers = []
#     for i, symptom in enumerate(symptoms_questions):
#         col = columns[i % 3]  # Distribute questions across 3 columns
#         answer = col.radio(f"Do you have {symptom.lower()}?", ('No', 'Yes'), index=0)
#         symptom_answers.append(answer)
    
#     # 8. Convert the inputs into a format the model can understand (0 for No, 1 for Yes)
#     symptoms = np.array(symptom_answers)
#     symptoms = np.where(symptoms == 'Yes', 1, 0).reshape(1, -1)  # Convert 'Yes' to 1 and 'No' to 0
    
#     # 9. Make prediction
#     if st.button('Predict'):
#         prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
#         prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
#         if prediction == 1:
#             st.error(f"Based on the symptoms, you might have Monkeypox!")
#             st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
#         else:
#             st.success(f"You are likely not infected with Monkeypox.")
#             st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# # 10. Run the app
# if __name__ == '__main__':
#     main()




# Selection box

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
    st.write("Select the symptoms you are experiencing from the list.")

    # 5. Symptoms list for selection
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
    
    # 6. Multi-selection box for symptoms
    selected_symptoms = st.multiselect('Select your symptoms:', symptoms_list)
    
    # 7. Convert selected symptoms to a format the model can understand (0 for No, 1 for Yes)
    symptoms_input = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]
    symptoms = np.array(symptoms_input).reshape(1, -1)  # Convert to numpy array
    
    # 8. Make prediction
    if st.button('Predict'):
        prediction = model.predict(symptoms)  # 0 for not infected, 1 for infected
        prediction_prob = model.predict_proba(symptoms)  # Probability of both classes
        
        if prediction == 1:
            st.error(f"Based on the symptoms, you might have Monkeypox!")
            st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
        else:
            st.success(f"You are likely not infected with Monkeypox.")
            st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# 9. Run the app
if __name__ == '__main__':
    main()
