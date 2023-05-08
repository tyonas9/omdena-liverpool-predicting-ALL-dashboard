import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

def load_css():
    css_file = open('assets/style.css', 'r')
    st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)
    css_file.close()
load_css()

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

st.subheader("Flowchart")
flowchart = Image.open('assets/images/flowchart.png')
st.image(flowchart,width=800)

st.subheader("Data Imbalance")
data_imbalance = Image.open('assets/images/data_imbalance.png')
st.image(data_imbalance,width=500)

st.subheader("Confusion Matrix Comparison")
col1,col2,col3 = st.columns(3)
with col1:
    before_aug = Image.open('assets/images/before_aug.png')
    st.image(before_aug,width=275)
with col2:
    after_aug = Image.open('assets/images/after_aug.png')
    st.image(after_aug)
with col3:
    after_voting = Image.open('assets/images/after_voting.png')
    st.image(after_voting, width=305)
    

st.header("Challenges faced during the project")

st.write("Challenges we faced while working on the project:")
st.markdown("- Imbalanced dataset")
st.markdown("- Computing resources")
st.markdown("- Too many possible ways of approaching the solution which requried a lot of experimentations")
st.markdown("- Use of traditional machine learning algorithms instead of neural networks")


st.header("Future Work")
st.markdown("- Fine Tuning the pre-trained networks for feature extraction")
st.markdown("- We only had enough time to use VGG16 and ResNet for feature extraction, but there are many other pre-trained networks that could be used which may give better results")