"""
EGT GeoControl
DDR Mapping

Relación entre los campos encontrados
en los Daily Drilling Reports y los
datasets utilizados por GeoControl.
"""

# -----------------------------
# DASHBOARD
# -----------------------------

DASHBOARD_FIELDS = {

    "report_number": "reporte",

    "report_date": "fecha",

    "day_number": "dia_campania",

    "measured_depth": "md",

    "tvd": "tvd",

    "rop": "rop",

    "cumulative_cost": "coste_acumulado",

    "afe_percent": "afe_pct",

    "npt_hours": "npt"

}

# -----------------------------
# DEPTH HISTORY
# -----------------------------

DEPTH_FIELDS = {

    "day_number": "dia",

    "measured_depth": "md"

}

# -----------------------------
# COST HISTORY
# -----------------------------

COST_FIELDS = {

    "day_number": "dia",

    "cumulative_cost": "coste"

}

# -----------------------------
# EVENTS
# -----------------------------

EVENT_FIELDS = {

    "depth": "profundidad",

    "event_type": "tipo",

    "event_category": "categoria",

    "criticality": "criticidad",

    "description": "descripcion"

}

# -----------------------------
# CLASIFICACIÓN DE EVENTOS
# -----------------------------

EVENT_CATEGORIES = {

    "LOSS": "Hidraulico",

    "GAIN": "Hidraulico",

    "DRILL_OUT_FAILURE": "Operacional",

    "STRING_STALL": "Operacional",

    "MUD_PUMP_FAILURE": "Mecanico",

    "ADA_LEAK": "Mecanico",

    "BOP_TEST": "Control_Pozo",

    "CEMENTING": "Cementacion",

    "NPT": "Operacional"
}
