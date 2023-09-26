import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image
from pathlib import Path

airbnb_csv = Path(__file__).parents[1] / "data/airbnb.csv"
description_jpg = Path(__file__).parents[1] / "img/description_wordcloud.jpg"
reviews_jpg = Path(__file__).parents[1] / "img/reviews_wordcloud.jpg"

st.set_page_config(page_title="Datathon 2023", layout="wide", page_icon=":bar_chart:")
st.set_option("deprecation.showPyplotGlobalUse", False)


@st.cache_data
def read_airbnb():
    df = pd.read_csv(airbnb_csv)
    return df


airbnb = read_airbnb()
description_wordcloud = Image.open(description_jpg)
reviews_wordcloud = Image.open(reviews_jpg)

## PAGE FORMAT ##

st.markdown("# Datos de Airbnb")
st.write(
    """En esta sección, presentaremos los datos de alquileres temporarios de la Ciudad de Corrientes que se ofrecen en la
    plataforma Airbnb. Este dataset fue el resultado de un scraping realizado durante la semana del Datathon, por lo que los precios están actualizados
    al mes de septiembre de 2023. El dataset cuenta con 22 columnas que describen características propias del alojamiento,
    como también el precio y las opiniones de los húespedes. Contiene alrededor de 260 alojamientos únicos de la Ciudad de Corrientes.
    """
)

###
st.markdown("----")
st.markdown("##### Dataset Hospedajes en Airbnb de la Ciudad de Corrientes")
st.dataframe(airbnb, use_container_width=False)

###
st.markdown("----")


def generate_x_axis_values(dataframe, column_name):
    """Generate X-axis values as a range from min to max of the specified column."""
    # Filter out NaN and convert to integers
    valid_values = dataframe[column_name].dropna().astype(int)
    if valid_values.empty:
        return []

    min_value = valid_values.min()
    max_value = valid_values.max()
    return list(range(int(min_value), int(max_value) + 1))


st.markdown("##### Características de los Alojamientos")
# Generate X-axis values for Guests
x_axis_values_guests = generate_x_axis_values(airbnb, "Guests")

# Create a histogram for Guests using Altair
guests_chart = (
    alt.Chart(airbnb)
    .mark_bar(opacity=0.7)
    .encode(
        alt.X(
            "Guests:O",
            axis=alt.Axis(values=x_axis_values_guests, title="Capacidad de Huéspedes"),
        ),
        alt.Y("count()", stack=None, axis=alt.Axis(title="Cantidad")),
    )
    .properties(title="Histograma de Capacidad de Huéspedes")
)

# Generate X-axis values for Bed
x_axis_values_bed = generate_x_axis_values(airbnb, "Beds")

# Create a histogram for Bed using Altair
bed_chart = (
    alt.Chart(airbnb)
    .mark_bar(opacity=0.7)
    .encode(
        alt.X(
            "Beds:O", axis=alt.Axis(values=x_axis_values_bed, title="Número de Camas")
        ),
        alt.Y("count()", stack=None, axis=alt.Axis(title="Cantidad")),
    )
    .properties(title="Histograma de Camas")
)

# Generate X-axis values for Bedrooms
x_axis_values_bedrooms = generate_x_axis_values(airbnb, "Bedrooms")

# Create a histogram for Bedrooms using Altair
bedrooms_chart = (
    alt.Chart(airbnb)
    .mark_bar(opacity=0.7)
    .encode(
        alt.X(
            "Bedrooms:O",
            axis=alt.Axis(
                values=x_axis_values_bedrooms, title="Número de Habitaciones"
            ),
        ),
        alt.Y("count()", stack=None, axis=alt.Axis(title="Cantidad")),
    )
    .properties(title="Histograma de Habitaciones")
)

# Generate X-axis values for Baths
x_axis_values_baths = generate_x_axis_values(airbnb, "Baths")

# Create a histogram for Baths using Altair
baths_chart = (
    alt.Chart(airbnb)
    .mark_bar(opacity=0.7)
    .encode(
        alt.X(
            "Baths:O",
            axis=alt.Axis(values=x_axis_values_baths, title="Número de Baños"),
        ),
        alt.Y("count()", stack=None, axis=alt.Axis(title="Cantidad")),
    )
    .properties(title="Histograma de Baños")
)

# Display the plots in two columns
col1, col2 = st.columns(2)

with col1:
    st.altair_chart(guests_chart, use_container_width=True)
    st.markdown("----")
    st.altair_chart(bed_chart, use_container_width=True)
with col2:
    st.altair_chart(bedrooms_chart, use_container_width=True)
    st.markdown("----")
    st.altair_chart(baths_chart, use_container_width=True)

st.write(
    """Se observa que la mayoría de los alojamientos temporarios ofrecidos en la Ciudad de Corrientes son relativamente "pequeños"
    con un promedio de 3.8 en la capacidad de huéspedes, 1.4 en la cantidad de habitaciones, 2.6 camas promedio y 1.1 en baños.
    """
)

###
st.markdown("----")

st.markdown("##### Comparación de Distribución de los Puntajes de Alojamientos")

key_order = [
    "Limpieza",
    "Veracidad",
    "Comunicación",
    "Ubicación",
    "Check-In",
    "Precio-Calidad",
    "Estrellas",
]

spanish_labels = {
    "Cleanliness_Score": "Limpieza",
    "Accuracy_Score": "Veracidad",
    "Communication_Score": "Comunicación",
    "Location_Score": "Ubicación",
    "Check_In_Score": "Check-In",
    "Value_Score": "Precio-Calidad",
    "Stars": "Estrellas",
}
translated_columns = [spanish_labels.get(col, col) for col in airbnb.columns]
airbnb.columns = translated_columns


# Create a custom sorting function based on the order of keys
def custom_sort(arr, key_order):
    key_to_index = {key: index for index, key in enumerate(key_order)}
    return sorted(arr, key=lambda x: key_to_index[x])


# Create the Altair chart with horizontal boxplots
scores = (
    alt.Chart(airbnb)
    .transform_fold(key_order, as_=["Tipo de Puntajes", "Valores"])
    .mark_boxplot()
    .encode(
        x=alt.X("Valores:Q", scale=alt.Scale(domain=[5, 3])),
        y=alt.Y(
            "Tipo de Puntajes:N",
            sort=key_order,
            axis=alt.Axis(),
        ),
    )
)

st.altair_chart(scores, use_container_width=True)

st.write(
    """En base a la comparación del gráfico de cajas, podemos ver que los valores de los puntajes para alojamientos en Airbnb se mantienen muy cerca del límite superior (5)
    y los puntajes mínimos otorgados solo llegan al 3.3, aunque el mínimo real de la escala es de 1.
    """
)

###
st.markdown("----")

st.markdown(
    "##### Distribucion de Precio Final Mensual en Dólares (luego de descuentos y tasas)"
)
price_dist = (
    alt.Chart(airbnb)
    .mark_bar()
    .encode(
        x=alt.X("Total:Q", bin=alt.Bin(maxbins=50), title="Precio Final"),
        y=alt.Y("count():Q", title="Cantidad"),
    )
)
st.altair_chart(price_dist, use_container_width=True)
st.write(
    """Se observa que en su mayoría, los precios finales de alquiler mensual en la ciudad de Corrientes ronda entre los 400 y 1000 USD luego de restar
    descuentos por estadía mensual y añadir tasas de limpieza y servicio de la plataforma. El promedio del precio es de 934 USD, con el mínimo valor siendo 23 USD (que estimamos es un error en la recolección de los datos) y un máximo de 3548 USD.
    """
)
###
st.markdown("----")

st.markdown("##### Nube de Palabras de las Descripciones de Alojamientos")
st.image(
    description_wordcloud, width=700, caption="Palabras más repetidas en la descripción"
)

st.markdown("##### Nube de Palabras de las Opiniones sobre los Alojamientos")
st.image(
    reviews_wordcloud, width=700, caption="Palabras más repetidas en las opiniones"
)

st.write(
    """Se observa que las palabras más frecuentes guardan una relación directa con la ubicación (lugar, cercanía, ubicado, zona, buena ubicación).En segundo lugar, notamos que en las descripciones se mencionan ventajas particulares, tales como aire acondicionado, acceso a internet, cama doble, parrilla, ropa de cama y bien equipado. Por otro lado, al analizar las opiniones, predominan términos relativos a la comunicación, la atención, la seguridad y el servicio.
    """
)
