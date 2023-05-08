import streamlit as st
from PIL import Image
from numpy import asarray
import numpy as np
import pandas as pd
from helping_functions import load_models, crop
import sklearn

st.set_page_config(layout='wide')

def load_css():
    css_file = open('assets/style.css', 'r')
    st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)
    css_file.close()
load_css()

    
#st.title('Image Classifier')

with st.spinner("Loading Models...."):
    vgg_model, classifier = load_models()

col1,col2 = st.columns(2)
with col1:
    #ask user to upload image
    file = st.file_uploader("Upload an image ", type=['bmp','png','jpg'])   

if file is not None:
    image = Image.open(file) #open uploaded image
    image_temp = asarray(image)
    cropped_img=crop(image_temp) 
    img_preprocessed = np.expand_dims(cropped_img, axis=0)
    col3,col4 = st.columns(2)
    with col3:
        st.subheader('Raw Image')
        st.image(image_temp)
        st.write("Image dimensions:",image_temp.shape)
        st.write("Max pixel values:",np.amax(image_temp))
    with col4:
        st.subheader('Preprocessed Image')
        st.image(img_preprocessed)
        st.write("Image dimensions:",img_preprocessed.shape)
        st.write("Max pixel value",np.amax(img_preprocessed))

    with st.spinner("Extracting Features.."):
        features = vgg_model.predict(img_preprocessed)
        feats = features.reshape(features.shape[0], -1)
        feats_df = pd.DataFrame(feats)
        st.subheader("Extracted Features")
        st.write(feats_df.head())
            
    with st.spinner("Classifying.. "):
        y_pred = classifier.predict(feats_df)
        if y_pred[0]==1:
            st.subheader("Image Classified as")
            st.metric(label="",value="ALL")  
        elif y_pred[0]==0:
            st.subheader("Image Classified as")
            st.metric(label="",value="Hem")