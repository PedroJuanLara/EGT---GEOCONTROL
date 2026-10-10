import streamlit as st

st.set_page_config(
    page_title="EGT GeoControl",
    page_icon="🌋",
    layout="wide"
)

st.title("🌋 EGT GeoControl")
st.subheader("Geothermal Project Control Center")

st.markdown("---")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Profundidad", "430 m")

with col2:
    st.metric("Avance", "14.3 %")

with col3:
    st.metric("Días", "30")

with col4:
    st.metric("Coste", "4.3 M$")

with col5:
    st.metric("ROP", "1.29 m/h")

with col6:
    st.metric("NPT", "42 h")

st.markdown("---")

st.header("📊 Estado General")

st.info(
    """
    Bienvenido a EGT GeoControl.

    Plataforma de supervisión, control y análisis
    de campañas geotérmicas de EGT.
    """
)

st.header("⚠️ Alertas")

st.warning(
    """
    Zona de pérdidas detectada entre 405 m y 430 m.
    """
)

st.success(
    """
    Sin incidentes HSE activos.
    """
)

st.header("📈 Próximos módulos")

st.write("✅ Dashboard Ejecutivo")
st.write("✅ Plazo")
st.write("✅ Economía")
st.write("✅ Operaciones")
st.write("✅ Riesgos")
st.write("✅ Comparador")
