import streamlit as st
from PIL import Image
from pathlib import Path

logo_path = Path(__file__).parents[0] / "img/logo_CD.png"
logo = Image.open(logo_path)

st.set_page_config(page_title="Datathon 2023", layout="wide", page_icon=":bar_chart:")

## Web App Format ##

st.markdown(
    "<h1 style='text-align: center; color: white;'>CtesBnb</h1>",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

"""
[![Star](https://img.shields.io/github/stars/lautaropacella/datathon2023.svg?logo=github&style=social)](https://github.com/lautaropacella/datathon2023)
"""

st.image(logo, width=500)

st.markdown("<br>", unsafe_allow_html=True)

"""
### **Proyecto para el Datathon 2023**
"""

st.markdown("<br>", unsafe_allow_html=True)
""" 
    La motivación principal de este proyecto radica en aprovechar la disponibilidad de datos abiertos proporcionados
    por la municipalidad de Corrientes y combinarlos con información obtenida de Airbnb para mostrar
    un breve análisis  y proporcionar visualizaciones informativas que pudiera servir de ejemplo sobre el uso de los datos
    para la toma de decisiones financieras. La iniciativa de este proyecto se basa creciente demanda de los servicios
    de hospedajes y las potenciales oportunidades en la industria.
"""

st.markdown("<br>", unsafe_allow_html=True)
""" 
    Para el presente proyecto se han utilizado las siguientes fuentes:
    - [Oferta de Alojamiento en la Ciudad de Corrientes - Serie 2016-2022. Municipalidad de Corrientes, 2023.](https://datos.ciudaddecorrientes.gov.ar/dataset/oferta-alojamiento)
    - [Ocupación Hotelera en la Ciudad de Corrientes - Serie 2016-2022. Municipalidad de Corrientes, 2023.](https://datos.ciudaddecorrientes.gov.ar/dataset/ocupac_hotelera)
    - [Visitantes en APN - Serie 2003-2020. APN, 2021.](https://docs.google.com/spreadsheets/d/1fT_kIOwEylGtsv6pMZYLeMNgYA3eb0TE/edit#gid=295715960)
    - [Dataset de Alojamientos en Airbnb de la Ciudad de Corrientes.](https://github.com/lautaropacella/datathon2023/blob/main/data/airbnb.csv)
"""
