import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="EGT GeoControl",
    page_icon="🌋",
    layout="wide"
)
df = pd.read_csv("data/tsa01_dashboard.csv")

ultimo = df.iloc[-1]
depth_df = pd.read_csv(
    "data/tsa01_depth_history.csv"
)
events_df = pd.read_csv(
    "data/tsa01_events.csv"
)
st.title("🌋 EGT GeoControl")
st.subheader("Geothermal Project Control Center")

st.markdown("---")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(
    "Profundidad",
    f"{ultimo['md']} m"
)

with col2:
    st.metric(
    "Avance",
    f"{ultimo['afe_pct']} %"
)

with col3:
    st.metric(
    "Días",
    int(ultimo['dia_campania'])
)

with col4:
    st.metric(
    "Coste",
    f"{ultimo['coste_acumulado']/1000000:.1f} M$"
)

with col5:
    st.metric(
    "ROP",
    f"{ultimo['rop']} m/h"
)

with col6:
    st.metric(
    "NPT",
    f"{ultimo['npt']} h"
)

st.markdown("---")

st.header("📊 Estado General")

st.info(
    """
    Bienvenido a EGT GeoControl.

    Plataforma de supervisión, control y análisis
    de campañas geotérmicas de EGT.
    """
)
st.header("📈 Profundidad vs Día de Campaña")

fig = px.line(
    depth_df,
    x="dia",
    y="md",
    markers=True,
    title="Evolución de profundidad TSA-01"
)

fig.update_layout(
    xaxis_title="Día de Campaña",
    yaxis_title="Profundidad MD (m)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.header("⚠️ Mapa de Incidencias por Profundidad")

fig_events = px.scatter(
    events_df,
    x="criticidad",
    y="profundidad",
    color="categoria",
    hover_data=["tipo", "descripcion"],
    title="Eventos TSA-01"
)

fig_events.update_layout(
    yaxis_title="Profundidad (m)",
    xaxis_title="Criticidad"
)

st.plotly_chart(
    fig_events,
    use_container_width=True
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
