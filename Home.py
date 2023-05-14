import streamlit as st
from PIL import Image
from numpy import asarray
import numpy as np
import pandas as pd
from helping_functions import load_models, crop, load_css
import sklearn
import scikeras

st.set_page_config(layout='wide')
load_css()

with st.spinner("Loading Models...."):
    vgg_model, classifier = load_models()
    
col1,col2 = st.columns(2)
with col1:
    #ask user to upload image
    file = st.file_uploader("Upload an image ", type=['bmp','png','jpg'])
    url = "https://github.com/liskibruh/omdena-liverpool-predicting-ALL-dashboard/blob/main/assets/images/example_img1.bmp"
    st.markdown("Download [example image](%s)" % url) 
    
with col2:
    flowchart = Image.open('assets/images/flowchart2.png')
    st.image(flowchart)
    
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
        
if file is not None:
    if 'feats_df' not in st.session_state:
        st.session_state['feats_df']=None
        
    if st.button("Extract Features", key=1):
        with st.spinner("Extracting Features.."):
            features = vgg_model.predict(img_preprocessed)
            feats = features.reshape(features.shape[0], -1)
            st.session_state['feats_df'] = pd.DataFrame(feats)
            st.subheader("Extracted Features")
            st.write(st.session_state['feats_df'].head())
            
    if st.button("Classify Image", key=2): 
        st.write(st.session_state['feats_df'].head())
        if st.session_state['feats_df'] is None:
            st.warning("Please extract features first.")
        else:
            with st.spinner("Classifying.. "):
                y_pred = classifier.predict(st.session_state['feats_df'])
                if y_pred[0]==1:
                    st.subheader("Image Classified as")
                    st.metric(label="",value="ALL")  
                elif y_pred[0]==0:
                    st.subheader("Image Classified as")
                    st.metric(label="",value="Hem")