import streamlit as st
import pandas as pd
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

    df = pd.read_csv("D:\Python Study\Self-tought-projects\Doctor app\Disease Prediction\Training.csv")
    symptroms = sorted(df.columns)


    st.markdown("## **Carefully choose the symptoms!**")

    bar_multiselect = st.multiselect(label="**Selected Symptoms:**", options=symptroms, default=[])

    st.checkbox('''
    I have read and agree to the following:
                
    1. I understant that this are all sensitive information and I am giving all correct information. 
    2. If the predicted disease is wrong because of wrong informations, Authority will not be responsible.
    ''')


    st.button("**Predict**👌", key='enter')



if selected == 'Doctor Recommendation':
    st.title('Doctor Recommendation')





if selected == 'Appointment Schedule':
    st.title('Appointment Schedule')

    name = st.text_input("Patient Name")
    age = st.text_input("Patient Age")
    date_of_birth = st.date_input("Patient Date of Birth")
    doc_name = st.text_input("Enter Doctor's Name")
    
    st.video("C:\Musfique's Folder\index4.mp4")
    st.help()



if selected == "Doctor's Assistant":
    st.title("Doctor's Assistant")

    text = st.chat_input("Char with me")
    st.chat_message()