"""
EGT GeoControl

CSV Generator V1

Genera los ficheros:
- dashboard.csv
- depth_history.csv
- cost_history.csv

a partir de información extraída
de los DDR.
"""

import pandas as pd

from test_ddr import test_ddr


def generate_dashboard_csv():

    ddr = test_ddr()

    dashboard_df = pd.DataFrame([
        {
            "reporte": ddr.reporte,
            "fecha": ddr.fecha,
            "dia_campania": ddr.dia_campania,
            "md": ddr.md,
            "afe_pct": ddr.afe_pct,
            "coste_acumulado": ddr.coste_acumulado,
            "rop": ddr.rop,
            "npt": ddr.npt
        }
    ])

    dashboard_df.to_csv(
        "dashboard.csv",
        index=False
    )

    return dashboard_df


def generate_depth_csv():

    ddr = test_ddr()

    depth_df = pd.DataFrame([
        {
            "dia": ddr.dia_campania,
            "md": ddr.md
        }
    ])

    depth_df.to_csv(
        "depth_history.csv",
        index=False
    )

    return depth_df


def generate_cost_csv():

    ddr = test_ddr()

    cost_df = pd.DataFrame([
        {
            "dia": ddr.dia_campania,
            "coste": ddr.coste_acumulado
        }
    ])

    cost_df.to_csv(
        "cost_history.csv",
        index=False
    )

    return cost_df


if __name__ == "__main__":

    generate_dashboard_csv()

    generate_depth_csv()

    generate_cost_csv()

    print(
        "CSV generados correctamente"
    )
