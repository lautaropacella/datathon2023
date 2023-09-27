import streamlit as st
import altair as alt
import folium
from streamlit_folium import st_folium
import pandas as pd
from pathlib import Path

alojamiento_csv = Path(__file__).parents[1] / "data/alojamiento.csv"
ocupacion_csv = Path(__file__).parents[1] / "data/ocupacion.csv"
ibera_coord_csv = Path(__file__).parents[1] / "data/ibera coordenadas.csv"
APN_csv = Path(__file__).parents[1] / "data/parques_visitantes.csv"

st.set_page_config(page_title="Datathon 2023", layout="wide", page_icon=":bar_chart:")


@st.cache_data
def read_alojamientos():
    df = pd.read_csv(alojamiento_csv)
    return df


@st.cache_data
def read_ocupacion():
    df = pd.read_csv(ocupacion_csv)
    return df


@st.cache_data
def read_ibera_coord():
    df = pd.read_csv(ibera_coord_csv)
    return df


@st.cache_data
def read_ibera():
    df = pd.read_csv(APN_csv)
    ibera = df[df["name"] == "Iberá"]
    return ibera


alojamiento = read_alojamientos()
ocupacion = read_ocupacion()
ibera_coord = read_ibera_coord()
ibera = read_ibera()


def create_esteros_map(ibera_coord):
    # Coordinates of 5 provinces in Esteros del Ibera, Corrientes
    lat = list(ibera_coord["lat"])
    lon = list(ibera_coord["lon"])
    names = list(ibera_coord["Nombre"])

    # Create a folium map centered around Esteros del Ibera
    esteros_center = (
        -28.32641799784776,
        -57.34674731559198,
    )  # Esteros del Ibera coordinates
    # Create a Streamlit app
    st.markdown("### Esteros del Iberá")

    # Create a map
    m = folium.Map(location=esteros_center, zoom_start=8, tiles="openstreetmap")

    # Add markers for each province
    for i, row in ibera_coord.iterrows():
        folium.Marker(
            location=[float(row["lat"]), float(row["lon"])],
            popup=row["Nombre"],
            icon=folium.Icon(color="blue"),
        ).add_to(m)
    return m


## PAGE FORMAT ##

st.markdown("# Datos Abiertos de Corrientes")
st.write(
    """A continuación, presentaremos un breve análisis sobre alojamientos disponibles, ocupación
      hotelera y turismo en base a datos abiertos proporcionados por el Municpio de Corrientes y la Administración de Parques Nacionales.
        """
)
st.markdown("----")
st.markdown(
    "##### Cantidad de Habitaciones de Alojamientos (Hoteles y para-Hoteles) en la Ciudad de Corrientes"
)

st.line_chart(
    data=alojamiento, x="Fecha", y="Habitaciones Total", use_container_width=True
)

st.write(
    """A simple vista, es evidente que la cantidad de habitaciones en hoteles y establecimientos similares se
    mantuvo relativamente constante hasta el año 2020, momento en el cual se produjo una marcada disminución en 
    la cantidad de alojamientos disponibles. Presumimos que este descenso se debe a la crisis desencadenada por la 
    pandemia de COVID-19 y su impacto significativo en la industria turística."""
)
st.write(
    """También se observa que, a partir de la mitad del año 2020, la cantidad de habitaciones disponibles ha ido en aumento,
      **aunque aún no ha logrado recuperar el nivel previo a la crisis del COVID-19**. Esto podría representar una
     oportunidad del sector."""
)

###
st.markdown("----")

st.markdown("##### Cantidad de Habitaciones Disponibles por Tipo de Alojamiento")
st.line_chart(
    data=alojamiento,
    x="Fecha",
    y=["Habitaciones Hoteles", "Habitaciones Para-Hoteles"],
    use_container_width=True,
)
st.write(
    """
Aunque la crisis derivada de la pandemia de COVID-19 ha tenido un impacto significativo en el sector del hospedaje, 
al analizarlo detenidamente, resulta evidente que la industria hotelera ha sido la más perjudicada. Esto lo atribuimos, 
en gran medida, a que los costos asociados con la operación de alojamientos alternativos, como pequeños establecimientos
 o alquileres de corta duración, son considerablemente menores en comparación con los gastos de mantener un hotel en funcionamiento.
 Esto permite a los establecimientos alternativos resistir las épocas de crisis con mayor resiliencia que los grandes hoteles."""
)

###
st.markdown("----")

percentage_hoteles = sum(
    alojamiento["Habitaciones Hoteles"] / alojamiento["Habitaciones Total"]
) / len(alojamiento)
percentage_para_hoteles = sum(
    alojamiento["Habitaciones Para-Hoteles"] / alojamiento["Habitaciones Total"]
) / len(alojamiento)

alojamiento_pie = pd.DataFrame(
    {
        "Tipo de Alojamiento": ["Hoteles", "Otros"],
        "Porcentaje": [percentage_hoteles, percentage_para_hoteles],
    }
)
tipo_alojamiento = (
    alt.Chart(alojamiento_pie)
    .mark_arc()
    .encode(theta="Porcentaje", color="Tipo de Alojamiento")
)
st.markdown(
    "##### Porcentaje de Habitaciones de Cada Tipo de Alojamiento Sobre Total de Habitaciones Disponibles"
)
col1, col2 = st.columns(2)
with col1:
    st.altair_chart(tipo_alojamiento, use_container_width=True)
with col2:
    st.write(
        """Teniendo en cuenta las fechas correspondientes a los datos analizados, las habitaciones disponibles
        en alojamientos alternativos constituyen, en promedio, el 10% del total de habitaciones disponibles en Corrientes.
        Este dato pone de manifiesto la notable dependencia del turismo en Corrientes respecto a la industria hotelera,
        y la reciente disminución en estas cifras podría presentar una oportunidad para que los alojamientos alternativos
        ganen presencia en el mercado
        """
    )
    st.write(
        """Sin embargo, el lento crecimiento de los alojamientos alternativos durante los años también nos brinda una señal sobre
        la demanda del mercado turístico de corrientes: quizás exista alguna razón por la cuál no han tenido un mayor éxito.
        """
    )

###
st.markdown("----")

st.markdown(
    "##### Porcentaje de Ocupacion de Hoteles en la Ciudad de Corrientes Durante el Año"
)

ciclo_ocupacion = (
    alt.Chart(ocupacion)
    .mark_line()
    .encode(x="Mes", y="Porcentaje Ocupacion", color="Año:N")
)
st.altair_chart(ciclo_ocupacion, use_container_width=True)
st.write(
    """Basándonos en el gráfico de ciclos, como era previsible, se evidencia una estacionalidad
    en la ocupación hotelera en la ciudad de Corrientes. Esta tiende a aumentar durante el verano 
    (enero y febrero), disminuir al punto más bajo en los meses subsiguientes (de marzo a junio),
    experimentar un notorio incremento durante el período de vacaciones de invierno (junio y julio),
    para luego mantenerse en un nivel constante, generalmente por debajo del 50% de ocupación.
        """
)

###
st.markdown("----")
st.markdown(
    "##### Estacia Promedio en Hoteles de la Ciudad de Corrientes (2016-2022)"
)
st.bar_chart(data=ocupacion, x="Fecha", y="Estadia Promedio", use_container_width=True)
st.write(
    """También se puede notar que la duración media de la estancia en hoteles de la Ciudad de Corrientes
     se mantiene en torno a los dos días. Con un promedio total de 1.84 días de estancia, consideramos que
    este factor influye considerablemente en la preferencia de los turistas por los hoteles en Corrientes
    frente a otros tipos de alojamiento. Los alojamientos alternativos suelen ser más atractivos para viajeros
    con estancias prolongadas, pero dado que Corrientes es principalmente un destino de tránsito, los servicios
    ofrecidos por los hoteles parecen ser la elección ideal.
    """
)

###
st.markdown("----")

st.write(
    """No obstante, en la provincia de Corrientes contamos con un atractivo turístico internacional
    de gran envergadura: el Parque Nacional Iberá. A continuación, se destacan las principales ciudades
    cercanas al parque que consideramos representan una oportunidad dada su proximidad a algunos de los portales de acceso y su desarrollo urbano,
    y presentamos un breve análisis acerca de los visitantes al parque.
    """
)

ibera_map = create_esteros_map(ibera_coord)
st_map = st_folium(ibera_map, width=700, height=450)

###
st.markdown("----")

st.markdown("##### Visitantes del Parque por Tipo de Residencia desde 2017-2022")

residentes = ibera[ibera["categoria"] == "Residentes"]["visitantes"].sum()
extranjeros = ibera[ibera["categoria"] == "Extranjeros"]["visitantes"].sum()
visitante_pie = pd.DataFrame(
    {
        "Visitante": ["Residente", "Extranjero"],
        "Cantidad": [residentes, extranjeros],
    }
)
tipo_visitante = (
    alt.Chart(visitante_pie).mark_arc().encode(theta="Cantidad:Q", color="Visitante")
)


st.altair_chart(tipo_visitante, use_container_width=True)
st.write(
    """Podemos observar que el total de visitantes al Parque Nacional Iberá desde el año 2017 hasta el año 2022 fue de 31854,
    y el 12% (3884) de estos visitantes provienen del extranjero.
    """
)

###
st.markdown("----")

st.markdown("##### Total de Visitantes del Parque por Año  (2017-2022)")

residentes_por_ano = ibera.groupby("ano")["visitantes"].sum()
st.bar_chart(data=residentes_por_ano, use_container_width=True)

st.write(
    """La cantidad de visitantes iba en aumento hasta el 2020, cuándo la crisis del COVID golpeó más duramente. Sería interesante poder
    analizar los datos de los años posteriores para ver si el crecimiento sigue vigente.
    """
)

st.markdown("##### Total de Visitantes del Parque Agrupados por Mes Durante 2017-2022")

residentes_por_mes = ibera.groupby("mes")["visitantes"].sum()
st.bar_chart(data=residentes_por_mes, use_container_width=True)

st.write(
    """Se observa que la cantidad de visitantes al Parque Nacional tiene un idéntico patrón de estacionalidad que el porcentaje de ocupación
    hotelera de la ciudad de Corrientes.
    """
)
