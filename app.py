import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="EGT GeoControl",
    page_icon="🌋",
    layout="wide"
)

st.sidebar.title("🌋 GeoControl")

sondeo_actual = st.sidebar.selectbox(
    "Seleccionar sondeo",
    [
        "TSA-01",
        "TSA-02"
    ],
    key="selector_sondeo_principal"
)

pagina = st.sidebar.radio(
    "Navegación",
    [
        "Dashboard",
        "Gestión Documental",
        "Sincronización",
        "Procesar DDR"
    ]
)

# --- ASIGNACIÓN DE RUTAS SEGÚN EL SONDEO ---
if sondeo_actual == "TSA-01":
    dashboard_file = "data/TSA_01/dashboard.csv"
    depth_file = "data/TSA_01/depth_history.csv"
    cost_file = "data/TSA_01/cost_history.csv"
    events_file = "data/TSA_01/events.csv"
    estado_file = "data/TSA_01/estado.csv"
elif sondeo_actual == "TSA-02":
    dashboard_file = "data/TSA_02/dashboard.csv"
    depth_file = "data/TSA_02/depth_history.csv"
    cost_file = "data/TSA_02/cost_history.csv"
    events_file = "data/TSA_02/events.csv"
    estado_file = "data/TSA_02/estado.csv"

# --- CARGA DE DATOS SEGURA ---
try:
    df = pd.read_csv(dashboard_file)
except FileNotFoundError:
    st.error(f"No se encontró el archivo de dashboard para {sondeo_actual} en la ruta: {dashboard_file}. Comprueba la carpeta 'data/'.")
    st.stop()

# Si tu dashboard.csv contiene múltiples sondeos o es específico por sondeo:
if "Sondeo" in df.columns:
    df_sondeo = df[df["Sondeo"] == sondeo_actual]
else:
    df_sondeo = df

if df_sondeo.empty:
    st.warning(f"No hay registros de datos disponibles para {sondeo_actual}.")
    st.stop()

ultimo = df_sondeo.iloc[-1]

# Métricas derivadas
coste_por_metro = ultimo["coste_acumulado"] / max(ultimo["md"], 1)
coste_por_dia = ultimo["coste_acumulado"] / max(ultimo["dia_campania"], 1)

objetivo_md = 3000
objetivo_coste = 11591535
objetivo_dias = 65

avance_md_pct = (ultimo["md"] / objetivo_md) * 100
avance_coste_pct = (ultimo["coste_acumulado"] / objetivo_coste) * 100
avance_tiempo_pct = (ultimo["dia_campania"] / objetivo_dias) * 100

# Cargar ficheros históricos secundarios de manera segura
try:
    depth_df = pd.read_csv(depth_file)
except:
    depth_df = pd.DataFrame(columns=["dia", "md"])

try:
    events_df = pd.read_csv(events_file)
except:
    events_df = pd.DataFrame(columns=["criticidad", "tipo", "profundidad", "categoria", "descripcion"])

try:
    cost_df = pd.read_csv(cost_file)
except:
    cost_df = pd.DataFrame(columns=["dia", "coste"])

try:
    estado_df = pd.read_csv(estado_file)
    ddr_detectados = estado_df.iloc[0].get("ddr_detectados", 0)
    ultimo_ddr = estado_df.iloc[0].get("ultimo_ddr", "-")
    ultima_sincronizacion = estado_df.iloc[0].get("ultima_sincronizacion", "-")
    estado_sincronizacion = estado_df.iloc[0].get("estado", "Pendiente")
except:
    ddr_detectados = 0
    ultimo_ddr = "-"
    ultima_sincronizacion = "-"
    estado_sincronizacion = "Pendiente"

numero_eventos = len(events_df)

if numero_eventos >= 5:
    semaforo_riesgo = "🔴 RIESGO OPERATIVO"
elif numero_eventos >= 3:
    semaforo_riesgo = "🟠 RIESGO OPERATIVO"
else:
    semaforo_riesgo = "🟢 RIESGO OPERATIVO"

# --- PÁGINA: GESTIÓN DOCUMENTAL ---
if pagina == "Gestión Documental":
    st.title("📁 Gestión Documental")
    st.subheader(f"Sondeo seleccionado: {sondeo_actual}")
    
    carpeta_sharepoint = "TSA_01" if sondeo_actual == "TSA-01" else "TSA_02"
    st.metric("Carpeta SharePoint", carpeta_sharepoint)
    
    st.link_button(
        "📂 Abrir SharePoint",
        "https://iter365.sharepoint.com/sites/IDAE-GEOTERMIA"
    )
    
    if st.button("🔄 Sincronizar SharePoint"):
        st.info("Sincronización SharePoint en desarrollo")
        
    col_doc4, col_doc5, col_doc6, col_doc7 = st.columns(4)
    with col_doc4:
        st.metric("DDR detectados", ddr_detectados)
    with col_doc5:
        st.metric("Último DDR", ultimo_ddr)
    with col_doc6:
        st.metric("Sincronización", estado_sincronizacion)
    with col_doc7:
        st.metric("Última sincronización", ultima_sincronizacion)
        
    st.text_area(
        "Ruta SharePoint",
        f"353_DAILY_REPORTS/{sondeo_actual.replace('-', '_')}",
        height=120
    )
    st.stop()

# --- PÁGINA: SINCRONIZACIÓN ---
if pagina == "Sincronización":
    st.title("🔄 Sincronización")
    st.metric("Estado SharePoint", "✅ Conectado")
    st.metric("Estado Power Automate", "✅ Activo")
    st.metric("Último DDR Detectado", ultimo_ddr)
    st.metric("Última Sincronización", ultima_sincronizacion)
    st.stop()

# --- PÁGINA: PROCESAR DDR ---
if pagina == "Procesar DDR":
    st.title("⚙️ Procesar Sondeo")
    st.subheader(f"Sondeo seleccionado: {sondeo_actual}")
    
    cantidad_ddr = 111
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("DDR detectados", cantidad_ddr)
    with col_b:
        st.metric("Procesados", 1)
    with col_c:
        st.metric("Pendientes", 110)
        
    if st.button("⚙️ Procesar Sondeo Completo"):
        st.success(f"Procesando {cantidad_ddr} DDR del {sondeo_actual}")
    st.stop()

# --- PÁGINA PRINCIPAL: DASHBOARD ---
st.title("🌋 EGT GeoControl")
st.caption(f"Sondeo activo: {sondeo_actual}")
st.subheader("Geothermal Project Control Center")
st.markdown("---")

st.header("🚦 Estado Ejecutivo")
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

# Métricas principales de la barra superior
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
with col1:
    st.metric("Profundidad", f"{ultimo['md']} m")
with col2:
    st.metric("Avance", f"{ultimo.get('afe_pct', avance_md_pct):.1f} %")
with col3:
    st.metric("Días", int(ultimo['dia_campania']))
with col4:
    st.metric("Coste", f"{ultimo['coste_acumulado']/1000000:.1f} M$")
with col5:
    st.metric("ROP", f"{ultimo.get('rop', 0.0)} m/h")
with col6:
    st.metric("NPT", f"{ultimo.get('npt', 0.0)} h")
with col7:
    st.metric("$/m", f"{coste_por_metro:,.0f}")
with col8:
    st.metric("$/día", f"{coste_por_dia:,.0f}")

st.markdown("---")

# --- OBJETIVOS DEL PROYECTO ---
st.header("🎯 Objetivos del Proyecto")
obj1, obj2, obj3 = st.columns(3)

with obj1:
    st.subheader("🌋 Profundidad")
    st.write(f"Actual: {ultimo['md']} m")
    st.write(f"Objetivo: {objetivo_md} m")
    st.progress(min(avance_md_pct / 100, 1.0))
    st.caption(f"{avance_md_pct:.1f}% completado")

with obj2:
    st.subheader("💰 Presupuesto")
    st.write(f"Actual: {ultimo['coste_acumulado']/1000000:.1f} M$")
    st.write(f"Objetivo: {objetivo_coste/1000000:.1f} M$")
    st.progress(min(avance_coste_pct / 100, 1.0))
    st.caption(f"{avance_coste_pct:.1f}% consumido")

with obj3:
    st.subheader("📅 Plazo")
    st.write(f"Actual: {int(ultimo['dia_campania'])} días")
    st.write(f"Objetivo: {objetivo_dias} días")
    st.progress(min(avance_tiempo_pct / 100, 1.0))
    st.caption(f"{avance_tiempo_pct:.1f}% consumido")

estado_global = (avance_md_pct + avance_coste_pct + avance_tiempo_pct) / 3

st.header("📊 Indicadores Ejecutivos (Gauges)")
g1, g2, g3, g4 = st.columns(4)

with g1:
    fig_avance = go.Figure(go.Indicator(
        mode="gauge+number", value=avance_md_pct,
        number={"suffix": "%", "font": {"size": 24}},
        title={"text": "🌋 Avance Físico"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#0F4C81"}, "bgcolor": "white"}
    ))
    fig_avance.update_layout(height=180, margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_avance, use_container_width=True)
    st.caption(f"{ultimo['md']} m de {objetivo_md} m")

with g2:
    fig_coste = go.Figure(go.Indicator(
        mode="gauge+number", value=avance_coste_pct,
        number={"suffix": "%"},
        title={"text": "💰 Presupuesto"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#2E8B57"}, "bgcolor": "white"}
    ))
    fig_coste.update_layout(height=180, margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_coste, use_container_width=True)
    st.caption(f"{ultimo['coste_acumulado']/1000000:.1f} M$ de {objetivo_coste/1000000:.1f} M$")

with g3:
    fig_plazo = go.Figure(go.Indicator(
        mode="gauge+number", value=avance_tiempo_pct,
        number={"suffix": "%", "font": {"size": 24}},
        title={"text": "📅 Plazo"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#F5A623"}, "bgcolor": "white"}
    ))
    fig_plazo.update_layout(height=180, margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_plazo, use_container_width=True)
    st.caption(f"{int(ultimo['dia_campania'])} días de {objetivo_dias} días")

with g4:
    fig_global = go.Figure(go.Indicator(
        mode="gauge+number", value=estado_global,
        number={"suffix": "%", "font": {"size": 24}},
        title={"text": "📊 Estado Global"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#6A5ACD"}, "bgcolor": "white"}
    ))
    fig_global.update_layout(height=180, margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_global, use_container_width=True)
    st.caption("Promedio Profundidad + Coste + Plazo")

# --- GRÁFICOS DE LÍNEA ---
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.header("📈 Profundidad vs Día de Campaña")
    if not depth_df.empty:
        fig = px.line(depth_df, x="dia", y="md", markers=True, title=f"Evolución de profundidad {sondeo_actual}")
        fig.update_traces(line=dict(width=4), marker=dict(size=8), fill="tozeroy")
        fig.update_layout(height=500, title_x=0.5, plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Sin datos de profundidad históricos disponibles.")

with col_graf2:
    st.header("💰 Coste Acumulado vs Día de Campaña")
    if not cost_df.empty:
        fig_cost = px.line(cost_df, x="dia", y="coste", markers=True, title=f"Evolución económica {sondeo_actual}")
        fig_cost.update_traces(line=dict(width=4), marker=dict(size=8), fill="tozeroy")
        fig_cost.update_layout(height=500, title_x=0.5, plot_bgcolor="white", paper_bgcolor="white")
        fig_cost.update_yaxes(tickprefix="$", separatethousands=True)
        st.plotly_chart(fig_cost, use_container_width=True)
    else:
        st.info("Sin datos de costes históricos disponibles.")
