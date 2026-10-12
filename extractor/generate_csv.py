"""
EGT GeoControl

CSV Generator

Genera dashboard.csv
a partir de un DDR real.
"""

import pandas as pd

from parser import parse_ddr


def generate_dashboard_csv(pdf_path):

    ddr = parse_ddr(pdf_path)

    dashboard_df = pd.DataFrame([
        {
            "reporte": ddr.reporte,
            "fecha": ddr.fecha,
            "dia_campania": ddr.dia_campania,
            "md": ddr.md,
            "tvd": ddr.tvd,
            "hole_made": ddr.hole_made,
            "rop": ddr.rop,
            "coste_acumulado": ddr.coste_acumulado,
            "afe_pct": ddr.afe_pct,
            "npt": ddr.npt
        }
    ])

    dashboard_df.to_csv(
        "dashboard.csv",
        index=False
    )

    return dashboard_df


if __name__ == "__main__":

    pdf_file = (
        "test_data/"
        "20260514 TSA-01 Daily Report with cost DDR 01.pdf"
    )

    dashboard = generate_dashboard_csv(
        pdf_file
    )

    print(dashboard)
