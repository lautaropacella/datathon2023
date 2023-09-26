import streamlit as st

st.set_page_config(page_title="Datathon 2023", layout="wide", page_icon=":bar_chart:")

st.markdown("<br>", unsafe_allow_html=True)

"""
### **Conclusiones y Futuras Investigaciones**
"""

st.write(
    """
         El objetivo principal de este proyecto fue presentar un ejemplo de análisis para respaldar la toma de decisiones basada en datos. Utilizamos datos abiertos proporcionados por la Municipalidad de Corrientes, Parques Nacionales y datos recopilados mediante técnicas de scraping para realizar un análisis preliminar del mercado de hospedaje en Corrientes.

Entre las observaciones más destacadas, resalta el impacto que la crisis del COVID-19 tuvo en la industria turística, respaldado por datos objetivos. También confirmamos la estacionalidad en la afluencia de visitantes a Corrientes y la preferencia por el turismo de tránsito en lugar de estancias prolongadas.
"""
)
st.markdown("----")
st.write(
    """
Existen oportunidades para investigaciones más exhaustivas sobre este tema, a continuación presentamos solo algunas de ellas:

- Analizar datos del mercado inmobiliario, obteniendo información de fuentes abiertas o mediante scraping en plataformas que ofrezcan venta de bienes raíces. Esto brindaría una visión más precisa sobre las posibilidades de inversión y la creación de emprendimientos de alojamientos temporales.
- Realizar un análisis de las descripciones y opiniones de alojamientos en Airbnb utilizando modelos de lenguaje de última generación (como GPT o Bard) para obtener una descripción más detallada de los principales factores implicados.   
- Análisis comparativo de los precios de alojamiento en Corrientes con respecto a otras ciudades turísticas cercanas y con todo el país.
"""
)
st.markdown("----")
st.write(
    """
El proyecto ha enriquecido nuestra comprensión de las oportunidades emprendedoras en el mercado de Corrientes y ha potenciado nuestras competencias técnicas en análisis y visualización de datos. Tenemos la esperanza de que este proyecto resulte útil para otros interesados, y por esta razón, nos comprometemos a brindar acceso abierto al conjunto de datos obtenido mediante scraping, asegurando que esté disponible para cualquier persona que desee aprovecharlo.
"""
)
