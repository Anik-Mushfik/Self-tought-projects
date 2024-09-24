import streamlit as st
import pandas as pd
import joblib
import os
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        "Our Services:", 
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

    df = pd.read_csv("Disease Prediction/Training.csv")
    df.drop(["Unnamed: 133", "prognosis"], axis=1, inplace=True)
    symptoms = df.columns

    st.markdown("## **Carefully choose the symptoms!**")

    bar_multiselect = st.multiselect(label="**Selected Symptoms:**", options=symptoms, default=[])

    st.checkbox('''
    I have read and agree to the following:
                
    1. I understand that this is sensitive information, and I am providing accurate details.
    2. If the predicted disease is wrong due to incorrect information, the authority will not be responsible.
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

        # Store prediction result in session state for doctor recommendation
        st.session_state.predicted_disease = predictions[0]


if selected == 'Doctor Recommendation':
    st.title('Doctor Recommendation')

    # Example dataset for doctor recommendations
    doctor_df = pd.DataFrame({
        "Disease": ["Disease A", "Disease B", "Disease C", "Disease D"],
        "Recommended Doctor": ["Dr. Alice", "Dr. Bob", "Dr. Clara", "Dr. Dave"],
        "Specialization": ["Cardiologist", "Neurologist", "Orthopedic", "Dermatologist"]
    })

    if 'predicted_disease' in st.session_state:
        predicted_disease = st.session_state.predicted_disease
        recommended_doctors = doctor_df[doctor_df["Disease"] == predicted_disease]
        
        if not recommended_doctors.empty:
            st.markdown(f"### Doctors recommended for **{predicted_disease}**:")
            for index, row in recommended_doctors.iterrows():
                st.write(f"- **{row['Recommended Doctor']}** ({row['Specialization']})")
        else:
            st.markdown("No doctors found for this disease.")
    else:
        st.markdown("No disease predicted yet. Please complete the disease prediction first.")



# Define file path for storing appointment data
appointment_file = 'appointments.csv'

if selected == 'Appointment Schedule':
    st.title('Appointment Schedule')

    with st.form("appointment_form"):
        name = st.text_input("Patient Name")
        age = st.text_input("Patient Age")
        dob = st.date_input("Date of Birth")
        email = st.text_input("Email Address")
        doc_name = st.text_input("Enter Doctor's Name (or choose from recommendation)")
        appointment_date = st.date_input("Preferred Appointment Date")
        appointment_time = st.time_input("Preferred Appointment Time")

        submit = st.form_submit_button("Submit Appointment")

        if submit:
            if not name or not email or not doc_name:
                st.error("Please complete all required fields.")
            else:
                # Prepare appointment data
                appointment_data = {
                    'Patient Name': [name],
                    'Age': [age],
                    'Date of Birth': [dob],
                    'Email': [email],
                    'Doctor Name': [doc_name],
                    'Appointment Date': [appointment_date],
                    'Appointment Time': [appointment_time]
                }

                # Convert data to a DataFrame
                appointment_df = pd.DataFrame(appointment_data)

                # Check if the file exists, and append if it does, or create a new one
                if os.path.exists(appointment_file):
                    appointment_df.to_csv(appointment_file, mode='a', index=False, header=False)
                else:
                    appointment_df.to_csv(appointment_file, mode='w', index=False, header=True)

                # Success message
                st.success(f"Appointment scheduled for {name} with Dr. {doc_name} on {appointment_date} at {appointment_time}.")
                st.info(f"A confirmation has been sent to {email}.")

# if selected == 'Appointment Schedule':
#     st.title('Appointment Schedule')

#     with st.form("appointment_form"):
#         name = st.text_input("Patient Name")
#         age = st.text_input("Patient Age")
#         dob = st.date_input("Date of Birth")
#         email = st.text_input("Email Address")
#         doc_name = st.text_input("Enter Doctor's Name (or choose from recommendation)")
#         appointment_date = st.date_input("Preferred Appointment Date")
#         appointment_time = st.time_input("Preferred Appointment Time")
        
#         submit = st.form_submit_button("Submit Appointment")
        
#         if submit:
#             if not name or not email or not doc_name:
#                 st.error("Please complete all required fields.")
#             else:
#                 st.success(f"Appointment scheduled for {name} with Dr. {doc_name} on {appointment_date} at {appointment_time}.")
#                 st.info(f"A confirmation has been sent to {email}.")
#                 # Additional functionality for sending email confirmations could be added here
            

if selected == "Doctor's Assistant":
    st.title("Doctor's Assistant")

    text = st.chat_input("Chat with me")
    st.chat_message(text)
