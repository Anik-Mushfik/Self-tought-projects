import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu





with st.sidebar:
    selected = option_menu(
        "Our Sirvices:", 
        [   
            'Disease Prediction',
            'Doctor Recommendation', 
            'Appointment Schedule',
            "Doctor's Assistant"
        ], 
        default_index=0
    )


if selected == 'Disease Prediction':
    st.title('Disease Prediction')

    df = pd.read_csv("Disease Prediction\Training.csv")
    df.drop(["Unnamed: 133", "prognosis"], axis=1, inplace= True)
    symptoms = df.columns


    st.markdown("## **Carefully choose the symptoms!**")

    bar_multiselect = st.multiselect(label="**Selected Symptoms:**", options=symptoms, default=[])

    st.checkbox('''
    I have read and agree to the following:
                
    1. I understant that this are all sensitive information and I am giving all correct information. 
    2. If the predicted disease is wrong because of wrong informations, Authority will not be responsible.
    ''')


    pre_but = st.button("**Predict**👌", key='enter')
    if pre_but:

        option_dict = {symptom: (1 if symptom in bar_multiselect else 0) for symptom in symptoms}


        # Load the model and scaler
        model = joblib.load('decision_tree_model.pkl')
        scaler = joblib.load('scaler_model.pkl')

        # User data (ensure this matches the features used in training)
        user_data = option_dict
        

        # Convert user data to DataFrame
        user_df = pd.DataFrame([user_data])

        # Apply the same preprocessing as during training
        user_df_scaled = scaler.transform(user_df)

        # Make predictions
        predictions = model.predict(user_df_scaled)

        
        st.markdown(f"## **Predictions: {predictions}!**")









if selected == 'Doctor Recommendation':
    st.title('Doctor Recommendation')





if selected == 'Appointment Schedule':
    st.title('Appointment Schedule')

    name = st.text_input("Patient Name")
    age = st.text_input("Patient Age")
    date_of_birth = st.date_input("Patient Date of Birth")
    doc_name = st.text_input("Enter Doctor's Name")
    
    # st.video("C:\Musfique's Folder\index4.mp4")
    # st.help()



if selected == "Doctor's Assistant":
    st.title("Doctor's Assistant")

    text = st.chat_input("Char with me")
    st.chat_message()