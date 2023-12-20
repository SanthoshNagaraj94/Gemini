import google.generativeai as genai
import json
import pathlib
import pprint
import requests
import streamlit as st

from pathlib import Path
import google.generativeai as genai

# Configure the client library by providing your API key.
API_KEY="AIzaSyB9M5r5VZhRlhxNpaZjTANacTD4SVoNvRc"     #Use Your Secret key Name
genai.configure(api_key=API_KEY)
def Image_Predictiion(Image,Prompt):
    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
    }

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                generation_config=generation_config,
                                )

    # Validate that an image is present
    if not (img := Path(Image)).exists():           #Replace your Image Path
        raise FileNotFoundError(f"Could not find image: {img}")

    image_parts = [
    {
        "mime_type": "image/jpeg",                                  #Replace your Image Path
        "data": Path(Image).read_bytes()
    },
    ]

    prompt_parts = [
    Prompt,
    image_parts[0],
    ]

    response = model.generate_content(prompt_parts)

    return response

def upload_file():
    # save uploaded file to /tmp in name of image.jpeg
    file=st.file_uploader("Here you can upload your image and get its description",type=["png","jpg","jpeg"])
    if file:
        with open("image.jpeg", "wb") as f:
            f.write(file.getbuffer())
    return "image.jpeg"

def Home():
    
    st.image("Background.jpg")