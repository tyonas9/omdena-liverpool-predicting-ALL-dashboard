import streamlit as st
import pandas as pd
from PIL import Image
from helping_functions import load_css
st.set_page_config(page_title='The Team', layout='wide')

load_css()

fa_li = """
<i class="fab fa-linkedin"></i>
"""
fa_em = """
<i class="far fa-envelope"></i>
"""

col1, col2 = st.columns((1, 5))
st.subheader('“A safe space to practice”')
st.write('Omdena Liverpool chapter was made up of a team from over 10 different timezones. \
    Despite the distances and time separations we manged to get together and successfully \
    collaborate and produce some ecxcellent work.')
st.write('All involved played an important role to the outcomes of the project.')

col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

with col1:
    rich = Image.open('assets/images/rich.jpg')
    st.image(rich)
    st.header('Rich')
    st.subheader('Chapter Lead')
    st.write('I am an accomplished Data Scientist & Analyst with 10+ years of experience. I am well \
        versed in Data Science and Machine Learning using advanced data methodologies to reach \
        useful business insights. I am proficient in data preprocessing, statistical method \
        application, predictive modeling, data visualisation and result communication.')
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write(
        fa_li,
        '[linkedin.com/in/rich-gregson](https://www.linkedin.com/in/rich-gregson/)',
        unsafe_allow_html=True
    )
with col2:
    salman = Image.open('assets/images/salman.jpg')
    st.image(salman)
    st.header('Salman')
    st.subheader('Chapter Lead')
    st.write("My machine learning journey began in 2008, implementing numerical methods and \
        conducting research on predictive modeling for time series data. I developed projects \
        predicting rainfall and heart attacks, supervised projects predicting ECG and EMG \
        results, and designed mathematical models for neurons and Alzheimer's behavior.")
    st.write(fa_li, '[linkedin.com/in/salmankhaliq22](https://www.linkedin.com/in/salmankhaliq22/)', unsafe_allow_html=True)
with col3:
    owais = Image.open('assets/images/owais.jpg')
    st.image(owais)
    st.header('Owais')
    st.subheader('Team Lead')
    st.write(" I'm a data geek with a passion for solving complex problems and a track record of \
        delivering results. With experience working on collaborative projects, I've developed a \
        strong team player mindset and a keen eye for detail. I believe in continuous learning \
        and have been working on building my skillset for the past 3 years. Currently focusing \
        on  NLP and Computer Vision. ")
    st.write(
        fa_li,
        '[linkedin.com/in/owais-tahir-a049b6233](https://www.linkedin.com/in/owais-tahir-a049b6233/)',
        unsafe_allow_html=True
    )
with col4:
    damir = Image.open('assets/images/damir.jpg')
    st.image(damir)
    st.header("Damir")
    st.subheader('Team Member')
    st.write("I'm a data professional with experience in physics, seismic data analysis, and \
        flight planning. I transitioned to data science and machine learning, leveraging \
        mathematical theory to uncover hidden value in data. I'm passionate about telling \
        data stories through engaging and intuitive visualizations to provide insights that \
        positively impact businesses.")
    st.write(
        fa_li, '[www.linkedin.com/in/damirzunic/](https://www.linkedin.com/in/damirzunic/)',
        unsafe_allow_html=True
    )

with col1:
    wallace = Image.open('assets/images/wallace.jpg')
    st.image(wallace)
    st.header('Wallace')
    st.subheader('Team Member')
    st.write("I consult and conduct scientific research in data-driven methods for business, \
        engineering simulation, and optimization. I have experience as a consultant in data \
        science and business intelligence projects, and volunteered as a data scientist in \
        open-source projects. I hold a Ph.D. in ensembles of supervised methods for engineering \
        optimization, have automotive industry experience, and have taught at universities.")
    st.write(
        fa_li, '[www.linkedin.com/in/wallace-g-ferreira-69065910/](https://www.linkedin.com/in/wallace-g-ferreira-69065910/ )',
        unsafe_allow_html=True
    )
    st.write("\n")
    st.write("\n")
with col2:
    neville = Image.open('assets/images/neville.jpg')
    st.image(neville)
    st.header('Neville')
    st.subheader('Team Member')
    st.write("Recently completed a master’s degree in Artificial Intelligence from Loughborough \
        University, UK. My main skills include Python, Machine Learning, big data technologies \
        and frameworks. I am a current Golden Visa holder within the UAE. My aim is to work in \
        the field of data analytics/science, machine learning or statistics while learning new \
        skills which will benefit me and my employer.")
    st.write(
        fa_li,
        '[www.linkedin.com/in/nevillemathew/](https://www.linkedin.com/in/nevillemathew/)',
        unsafe_allow_html=True
    )
    st.write("\n")
    st.write("\n")
    st.write("\n")
with col3:
    soumya = Image.open('assets/images/soumya.jpg')
    st.image(soumya)
    st.header('Soumya')
    st.subheader('Team Member')
    st.write("With a master's degree in physics, I focus on studying 2D materials like graphene \
        and their heterostructures using simulations and theoretical models. I have experience in \
        neutrino detector simulations, teaching physics and mathematics, and expertise in Python, \
        Scikit-Learn, and Tensorflow/Keras. My goal is to use data analytics and machine learning \
        to solve real-world problems and make a positive impact on society.")
    st.write(
        fa_li,
        '[www.linkedin.com/in/saleh-ahmed-rony](https://www.linkedin.com/in/saleh-ahmed-rony-135493156/)',
        unsafe_allow_html=True
    )
with col4:
    varun = Image.open('assets/images/varun.jpg')
    st.image(varun)
    st.header('Varun')
    st.subheader('Team Member')
    st.write("A Data enthusiast, helping startups in making data-driven decisions and achieving \
        their goals. Experience in ETL processing, data automation, financial and BI analysis, \
        and reporting. Knowledge of database management, machine learning algorithms, and cloud \
        architecture.")
    st.write(
        fa_li,
        '[www.linkedin.com/in/varun-yadav/](https://www.linkedin.com/in/varun-yadav/)',
        unsafe_allow_html=True
    )
    
with col1:
    darshan = Image.open('assets/images/darshan.jpg')
    st.image(darshan)
    st.header("Darshan Pai")
    st.subheader("Team Member")
    st.write("I am a software engineer with expertise in image analysis and visualization, \
        focused on applied research. My skills include programming languages such as C++, Java, \
        and Python, as well as libraries like OpenGL and VTK. I have experience in scientific \
        visualization, computer graphics, and image analysis, with knowledge of artificial \
        intelligence and deep learning. Some of my projects include virtual colonoscopy, brain \
        mapping, and neuroimaging analysis.")
    st.write(
        fa_li,
        '[https://www.linkedin.com/in/darshanpai/](https://www.linkedin.com/in/darshanpai/)',
        unsafe_allow_html=True
    )
    
with col2:
    dounia = Image.open("assets/images/dounia.jpg")
    st.image(dounia)
    st.header("Dounia")
    st.subheader("Team Member")
    st.write("I'm an engineer in data engineering and business intelligence, graduated from the \
        National Institute of Statistics and Applied Economics (INSEA) of Rabat. I'm passionate \
        about Machine Learning, Artificial intelligence, Data science, Mathematics and programming.")
    st.write(
        fa_li,
        '[https://www.linkedin.com/in/dounia-sadiky-56a729204/](https://www.linkedin.com/in/dounia-sadiky-56a729204/)',
        unsafe_allow_html=True
    )

with col3:
    st.write(' ')
with col4:
    st.write(' ')