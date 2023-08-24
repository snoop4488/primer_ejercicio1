import streamlit as st 
from PIL import Image
st.title("mi primer app")



st.header("en este espacio desarrollo mi app")
image= Image.open("nacional.png")

st.image(image,caption ='nacional')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("El nacional es el mejor equipo de colombia")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Cuantas copas libertadores tiene el nacional", ('2', '0', '1'))
    if modo == '2':
       st.write('es correcto el nacional tiene 2 liberadores')
    if modo == '0':
       st.write('0? como creees sapo')
    if modo == '1':
       st.write('equivocado pa')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
