import streamlit as st
from Fun import *
import os
from pymongo import MongoClient
import base64
import re
#datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
from datetime import datetime

client=MongoClient("mongodb+srv://santhosh:sam123@cluster0.mvgwd.mongodb.net/?retryWrites=true&w=majority")
db=client['Guvi']
coll=db['Gemini-Vision']
Side_option=st.sidebar.selectbox("Choose your option",("Home","Image Q&A","Image Description"))

st.sidebar.markdown("""## Welcome Gemini-Vision to Guvi-AI""")
st.sidebar.image("guvi.png")
st.sidebar.write("Made with ❤️ by Guvi-AI  https://www.guvi.in/")
Prompt=""
if Side_option=="Home":
    Home()
elif Side_option=="Image Q&A":
    st.title("Image Q&A")
    Image=upload_file()
    
    
    try:
        st.image(Image, width=300)
    except:
        pass
    Prompt=st.text_input("Ask your Question From Image")
   
    if st.button("submit"):
        response=Image_Predictiion(Image,Prompt)
        st.markdown(response.text)
        # save the image, prompt input and response to upload into mongoDB
        Image=open("image.jpeg","rb").read()
        coll.insert_one({"Date":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"image":base64.b64encode(Image),"prompt":Prompt,"response":response.text})

        os.remove("image.jpeg")

    
elif Side_option=="Image Description":
    st.title("Image Description")
    Image=upload_file()
    try:
        st.image(Image, width=300)
    except:
        pass
    Prompt="Describe the Image and its Background Image with 8 bullet points"
    # validate Email

    if st.button("Describe the Image"):
        response=Image_Predictiion(Image,Prompt)
    
        
        st.markdown(response.text)
        Image=open("image.jpeg","rb").read()
        coll.insert_one({"Date":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"image":base64.b64encode(Image),"prompt":Prompt,"response":response.text})
        
        os.remove("image.jpeg")
