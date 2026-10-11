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
coste_por_metro = (
    ultimo["coste_acumulado"] /
    ultimo["md"]
)
coste_por_dia = (
    ultimo["coste_acumulado"] /
    ultimo["dia_campania"]
)
depth_df = pd.read_csv(
    "data/tsa01_depth_history.csv"
)
events_df = pd.read_csv(
    "data/tsa01_events.csv"
)
cost_df = pd.read_csv(
    "data/tsa01_cost_history.csv"
)
cost_df = pd.read_csv(
    "data/tsa01_cost_history.csv"
)

numero_eventos = len(events_df)

if numero_eventos >= 5:
    semaforo_riesgo = "🔴 RIESGO OPERATIVO"
elif numero_eventos >= 3:
    semaforo_riesgo = "🟠 RIESGO OPERATIVO"
else:
    semaforo_riesgo = "🟢 RIESGO OPERATIVO"

st.title("🌋 EGT GeoControl")
st.subheader("Geothermal Project Control Center")
st.markdown("---")

st.header("🚦 Estado Ejecutivo")
st.info(
    """
    Estado general del proyecto basado en:
    plazo, coste, seguridad e incidencias operativas.
    """
)

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    st.success("🟢 PLAZO")

with col_b:
    st.success("🟢 COSTE")

with col_c:
    st.success("🟢 SEGURIDAD")

with col_d:
    st.warning(semaforo_riesgo)
st.markdown("---")

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

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
with col7:

    st.metric(

        "$/m",

        f"{coste_por_metro:,.0f}"

    )
with col8:
    st.metric(
        "$/día",
        f"{coste_por_dia:,.0f}"
    )
st.markdown("---")
avance_pct = (
    ultimo["md"] / 3000
) * 100

st.header("🎯 Objetivos del Proyecto")

fig_gauge = px.pie(
    values=[avance_pct, 100 - avance_pct],
    names=["Avance", "Pendiente"],
    hole=0.75,
    color_discrete_sequence=[
        "#0F4C81",
        "#E6E6E6"
    ]
)

fig_gauge.update_traces(
    textinfo="none"
)

fig_gauge.update_layout(
    showlegend=False,
    height=300,
    margin=dict(
        t=20,
        b=20,
        l=20,
        r=20
    ),
    annotations=[
        dict(
            text=f"{avance_pct:.1f}%<br>{ultimo['md']} m",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=22)
        )
    ]
)

st.plotly_chart(
    fig_gauge,
    use_container_width=True
)
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
    title="Evolución de profundidad TSA-01",
    color_discrete_sequence=["#0F4C81"]
)

fig.update_traces(
    line=dict(width=4),
    marker=dict(size=8),
    fill="tozeroy"
)

fig.update_layout(
    xaxis_title="Día de Campaña",
    yaxis_title="Profundidad MD (m)",
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=500,
    title_x=0.5,
    font=dict(size=14)
)
fig.update_xaxes(
    showgrid=True,
    gridcolor="#E6E6E6"
)

fig.update_yaxes(
    showgrid=True,
    gridcolor="#E6E6E6"
)
st.plotly_chart(
    fig,
    use_container_width=True
)
st.header("💰 Coste Acumulado vs Día de Campaña")

fig_cost = px.line(
    cost_df,
    x="dia",
    y="coste",
    markers=True,
    title="Evolución económica TSA-01",
    color_discrete_sequence=["#4FAF4F"]
)

fig_cost.update_traces(
    line=dict(width=4),
    marker=dict(size=8),
    fill="tozeroy"
)

fig_cost.update_layout(
    xaxis_title="Día de Campaña",
    yaxis_title="Coste Acumulado ($)",
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=500,
    title_x=0.5,
    font=dict(size=14)
)
fig_cost.update_xaxes(
    showgrid=True,
    gridcolor="#E6E6E6"
)

fig_cost.update_yaxes(
    showgrid=True,
    gridcolor="#E6E6E6"
)
fig_cost.update_yaxes(
    tickprefix="$",
    separatethousands=True
)
st.plotly_chart(
    fig_cost,
    use_container_width=True
)
st.header("⚠️ Incidencias Relevantes")

st.dataframe(
    events_df[
        [
            "profundidad",
            "tipo",
            "categoria",
            "criticidad"
        ]
    ],
    use_container_width=True,
    hide_index=True
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
