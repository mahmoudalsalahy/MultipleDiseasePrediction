
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',key="Number of Pregnancies")        
        
    with col2:
        Glucose = st.number_input('Glucose Level',key="Glucose Level")
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value',key="Blood Pressure value")
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value',key="Skin Thickness value")
    
    with col2:
        Insulin = st.number_input('Insulin Level',key="Insulin Level")
    
    with col3:
        BMI = st.number_input('BMI value',key="BMI value")
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value',key="Diabetes Pedigree Function value")
    
    with col2:
        Age = st.number_input('Age of the Person',key="Age of the Person")
    

    def clear_text():
        st.session_state["Number of Pregnancies"] = ""
        st.session_state["Glucose Level"] = ""
        st.session_state["Blood Pressure value"] = ""
        st.session_state["Skin Thickness value"] = ""
        st.session_state["Insulin Level"] = ""
        st.session_state["BMI value"] = ""
        st.session_state["Diabetes Pedigree Function value"] = ""
        st.session_state["Age of the Person"] = ""
        
    st.button("Reset", on_click=clear_text)
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            st.markdown(f'<p style="background-color:#ff4b4b;text-align:center;color:#ffffff;font-size:24px;border-radius:2%;">CHECK YOUR RESULTS</p>', unsafe_allow_html=True)
        
            st.markdown(f'<p style="text-align:center;color:#ff4b4b;font-size:16px;">You are suffered from Diabetes</p>', unsafe_allow_html=True)
        
            st.markdown(f'<p style="text-align:center;font-size:12px;">I am sorry to hear that you are suffering from diabetes. It must be challenging to manage your health condition, but please know that you are not alone, and there is help available to you. It takes a lot of courage and strength to deal with this, and I wish you all the best in your journey towards better health.</p>', unsafe_allow_html=True)


             ##################################################################################################################
            def load_data():
                return pd.DataFrame(
                    {
                        "Label": ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"],
                        "Value": [Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age],
                    }
                )    
            df = load_data()
            st.dataframe(df)
            
            img1 = Image.open("diabetes/Bhujangasana.jpg")
            img2 = Image.open("diabetes/Dhanurasana.jpg")
            img3 = Image.open("diabetes/Mandukasana.jpg")
            img4 = Image.open("diabetes/Paschimottanasana.jpg")
            img5 = Image.open("diabetes/Pawanmuktasana.jpg")
            img6 = Image.open("diabetes/Purvottanasana.jpg")
            img7 = Image.open("diabetes/Sarvangasana.jpg")
            img8 = Image.open("diabetes/Shavasana.jpg")
            img9 = Image.open("diabetes/Surya Namaskar.jpg")
            img10 = Image.open("diabetes/Viparita Karani.jpg")


            st.subheader('Yoga Poses for Diabetes: Asanas to Help Control Blood Sugar Levels')

            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(img1,caption='Bhujangasana')        

            with col2:
                st.image(img2,caption='Dhanurasana')

            with col3:
                st.image(img3,caption='Mandukasana')

            with col1:
                st.image(img4,caption='Paschimottanasana')        

            with col2:
                st.image(img5,caption='Pawanmuktasana')

            with col3:
                st.image(img6,caption='Purvottanasana')

            with col1:
                st.image(img7,caption='Sarvangasana')        

            with col2:
                st.image(img8,caption='Shavasana')

            with col3:
                st.image(img9,caption='Surya Namaskar')

            with col1:
                st.image(img10,caption='Viparita Karani')

            st.video("https://youtu.be/2Ij3i295XLE")
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age',key='Age')
        
    with col2:
        sex = st.number_input('Sex',key='Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types',key='Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',key='Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',key='Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',key='Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',key='Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',key='Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina',key='Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',key='ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',key='Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',key='Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',key='thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
            
            st.markdown(f'<p style="background-color:#ff4b4b;text-align:center;color:#ffffff;font-size:24px;border-radius:2%;">CHECK YOUR RESULTS</p>', unsafe_allow_html=True)
        
            st.markdown(f'<p style="text-align:center;color:#ff4b4b;font-size:16px;">You are suffered from Heart Disease</p>', unsafe_allow_html=True)
                
            st.markdown(f'<p style="text-align:center;font-size:12px;">I am sorry to hear that you are suffering from heart disease. Please know that my thoughts are with you during this difficult time. It must be challenging to cope with such a serious health condition, but I hope that you have the support and resources you need to manage your symptoms and improve your overall health. Do not hesitate to reach out to your healthcare provider or loved ones for help and guidance. Take care of yourself and know that you are not alone in this journey.</p>', unsafe_allow_html=True)

            ##################################################################################################################
            def load_data():
                return pd.DataFrame(
                    {
                        "Label": ["Age", "Sex","Chest Pain types","Resting Blood Pressure","Serum Cholestoral in mg/dl","Fasting Blood Sugar > 120 mg/dl","Maximum Heart Rate achieved","Maximum Heart Rate achieved","Exercise Induced Angina","ST depression induced by exercise","Slope of the peak exercise ST segment","Major vessels colored by flourosopy","thal: 0 = normal; 1 = fixed defect; 2 = reversable defect"],
                        "Value": [age, sex, cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal],
                    }
            )    
            df = load_data()
            st.dataframe(df)
            
            img1 = Image.open("heart/Bhujangasana.png")
            img2 = Image.open("heart/Padangusthasana.png")
            img3 = Image.open("heart/Paschimottanasana.png")
            img4 = Image.open("heart/Savasana.png")
            img5 = Image.open("heart/Setu Bandhasana.png")
            img6 = Image.open("heart/Svanasana.png")
            img7 = Image.open("heart/Tadasana.png")
            img8 = Image.open("heart/Utkatasana.png")
            img9 = Image.open("heart/Uttanasana.png")
            img10 = Image.open("heart/Vrikshasana.png")


            st.subheader('Breathwork for Heart Health: Using Pranayama Techniques to Improve Cardiovascular Function')
            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(img1,caption='Bhujangasana')        

            with col2:
                st.image(img2,caption='Padangusthasana')

            with col3:
                st.image(img3,caption='Paschimottanasana')

            with col1:
                st.image(img4,caption='Savasana')        

            with col2:
                st.image(img5,caption='Setu Bandhasana')

            with col3:
                st.image(img6,caption='Svanasana')

            with col1:
                st.image(img7,caption='Tadasana')        

            with col2:
                st.image(img8,caption='Utkatasana')

            with col3:
                st.image(img9,caption='Uttanasana')

            with col1:
                st.image(img10,caption='Vrikshasana')

            st.video("https://youtu.be/dAHrFEGxuS4")
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.number_input('MDVP:RAP')
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ')
        
    with col3:
        DDP = st.number_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.number_input('MDVP:APQ')
        
    with col4:
        DDA = st.number_input('Shimmer:DDA')
        
    with col5:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('spread1')
        
    with col5:
        spread2 = st.number_input('spread2')
        
    with col1:
        D2 = st.number_input('D2')
        
    with col2:
        PPE = st.number_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
            st.markdown(f'<p style="background-color:#ff4b4b;text-align:center;color:#ffffff;font-size:24px;border-radius:2%;">CHECK YOUR RESULTS</p>', unsafe_allow_html=True)
        
            st.markdown(f'<p style="text-align:center;color:#ff4b4b;font-size:16px;">You are suffered from Parkinson Disease</p>', unsafe_allow_html=True)
                
            st.markdown(f'<p style="text-align:center;font-size:12px;">I am sorry to hear that you are suffering from parkinson disease. Please know that my thoughts are with you during this difficult time. It must be challenging to cope with such a serious health condition, but I hope that you have the support and resources you need to manage your symptoms and improve your overall health. Do not hesitate to reach out to your healthcare provider or loved ones for help and guidance. Take care of yourself and know that you are not alone in this journey.</p>', unsafe_allow_html=True)

            ##################################################################################################################
            def load_data():
                return pd.DataFrame(
                    {
                        "Label": ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)","MDVP:Flo(Hz)","MDVP:Jitter(%)","MDVP:Jitter(Abs)","MDVP:RAP","MDVP:PPQ","Jitter:DDP","MDVP:Shimmer","MDVP:Shimmer(dB)","Shimmer:APQ3","Shimmer:APQ5","MDVP:APQ","Shimmer:DDA","NHR","HNR","RPDE","DFA","spread1","spread2","D2","PPE"],
                        "Value": [fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE],
                    }
            )    
            df = load_data()
            st.dataframe(df)
            img1 = Image.open("parkinson/Supta Baddha Konasana.png")
            img2 = Image.open("parkinson/tasasana.jpg")
            img3 = Image.open("parkinson/uttanasana.jpg")
            img4 = Image.open("parkinson/Virabhadrasana II.jpg")

            st.subheader('Yoga as a Tool for Stress Reduction and Improved Quality of Life in Parkinson Disease')
            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(img1,caption='Supta Baddha Konasana')        

            with col2:
                st.image(img2,caption='Tasasana')

            with col3:
                st.image(img3,caption='Uttanasana')

            with col1:
                st.image(img4,caption='Virabhadrasana II')       

            st.video("https://youtu.be/g6ocPtR_uZ8")
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

    
