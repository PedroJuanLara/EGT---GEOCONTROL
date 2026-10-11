import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

objetivo_md = 3000

objetivo_coste = 11591535

objetivo_dias = 65

avance_md_pct = (
    ultimo["md"] /
    objetivo_md
) * 100

avance_coste_pct = (
    ultimo["coste_acumulado"] /
    objetivo_coste
) * 100

avance_tiempo_pct = (
    ultimo["dia_campania"] /
    objetivo_dias
) * 100

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

obj1, obj2, obj3 = st.columns(3)

with obj1:

    st.subheader("🌋 Profundidad")

    st.write(
        f"Actual: {ultimo['md']} m"
    )

    st.write(
        f"Objetivo: {objetivo_md} m"
    )

    st.progress(
        avance_md_pct / 100
    )

    st.caption(
        f"{avance_md_pct:.1f}% completado"
    )

with obj2:

    st.subheader("💰 Presupuesto")

    st.write(
        f"Actual: {ultimo['coste_acumulado']/1000000:.1f} M$"
    )

    st.write(
        f"Objetivo: {objetivo_coste/1000000:.1f} M$"
    )

    st.progress(
        avance_coste_pct / 100
    )

    st.caption(
        f"{avance_coste_pct:.1f}% consumido"
    )

with obj3:

    st.subheader("📅 Plazo")

    st.write(
        f"Actual: {ultimo['dia_campania']} días"
    )

    st.write(
        f"Objetivo: {objetivo_dias} días"
    )

    st.progress(
        avance_tiempo_pct / 100
    )

    st.caption(
        f"{avance_tiempo_pct:.1f}% consumido"
    )
    st.header("📊 Indicadores Ejecutivos")

g1, g2, g3, g4 = st.columns(4)
with g1:
    fig_avance = go.Figure()
    
    fig_avance.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=avance_md_pct,
            number={
    "suffix": "%",
    "font": {
        "size": 24
    }
},
            title={
                "text": "🌋 Avance Físico"
            },
            gauge={
                "axis": {
    "range": [0, 100],
    "showticklabels": False
},
                "bar": {
                    "color": "#0F4C81"
                },
                "bgcolor": "white",
                "steps": [
                    {
                        "range": [0, 100],
                        "color": "#E6E6E6"
                    }
                ]
            }
        )
    )
    
    fig_avance.update_layout(
        height=180,
        margin=dict(
            t=20,
            b=20,
            l=20,
            r=20
        )
    )
    
    st.plotly_chart(
        fig_avance,
        use_container_width=True
    )
    
    st.caption(
        f"{ultimo['md']} m de {objetivo_md} m"
    )
    

    st.caption("🌋 Avance Físico")
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
col_inc, col_pozo = st.columns([2,1])
with col_inc:

    st.subheader("⚠️ Incidencias Relevantes")

    incidencias_df = events_df.sort_values(
    by="profundidad",
    ascending=True
)

    for _, row in incidencias_df.iterrows():

        if row["criticidad"] == "Alta":
            icono = "🔴"
            color_fondo = "#FDECEC"
            color_borde = "#D64541"
    
        elif row["criticidad"] == "Media":
            icono = "🟠"
            color_fondo = "#FFF4E5"
            color_borde = "#F5A623"
    
        else:
            icono = "🟢"
            color_fondo = "#EAF7EA"
            color_borde = "#4FAF4F"
    
        st.markdown(
            f"""
    <div style="
    background-color:{color_fondo};
    border-left:8px solid {color_borde};
    padding:15px;
    margin-bottom:15px;
    border-radius:10px;
    ">
    
    <b>{icono} {row['tipo']}</b><br><br>
    
    📍 <b>Profundidad:</b> {row['profundidad']} m<br>
    
    📂 <b>Categoría:</b> {row['categoria']}<br><br>
    
    📝 {row['descripcion']}
    
    </div>
    """,
            unsafe_allow_html=True
        )
with col_pozo:

    st.subheader("🛢 Perfil del Pozo")

    st.markdown("🌋 Superficie")
    st.markdown("│")

    perfil_df = events_df.sort_values(
        by="profundidad",
        ascending=True
    )

    for _, row in perfil_df.iterrows():

        if row["criticidad"] == "Alta":
            icono = "🔴"

        elif row["criticidad"] == "Media":
            icono = "🟠"

        else:
            icono = "🟢"

        st.markdown("│")

        st.markdown(
            f"├─ {icono} {row['profundidad']} m"
        )

        st.caption(
            row["tipo"]
        )

    st.markdown("│")
    st.markdown("⬇️ Fondo del pozo")

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
