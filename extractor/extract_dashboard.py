"""
EGT GeoControl

Dashboard Extractor V1

Extrae los campos principales
de un Daily Drilling Report.
"""

import re

from pdf_reader import read_pdf


def extract_dashboard_data(pdf_path):

    texto = read_pdf(pdf_path)

    resultado = {
        "reporte": None,
        "fecha": None,
        "md": None,
        "rop": None,
        "coste_acumulado": None,
        "afe_pct": None
    }

    # --------------------------------------------------
    # REPORT NUMBER
    # --------------------------------------------------

    match = re.search(
        r"DDR\s*(\d+)",
        texto,
        re.IGNORECASE
    )

    if match:
        resultado["reporte"] = match.group(1)

    # --------------------------------------------------
    # MEASURED DEPTH
    # --------------------------------------------------

    md_match = re.search(
        r"Measured Depth.*?(\d+\.\d+)",
        texto,
        re.IGNORECASE
    )

    if md_match:
        resultado["md"] = md_match.group(1)

    # --------------------------------------------------
    # ROP
    # --------------------------------------------------

    rop_match = re.search(
        r"Average ROP.*?(\d+\.\d+)",
        texto,
        re.IGNORECASE
    )

    if rop_match:
        resultado["rop"] = rop_match.group(1)

    # --------------------------------------------------
    # AFE %
    # --------------------------------------------------

    afe_match = re.search(
        r"AFE.*?(\d+\.\d+)\s*%",
        texto,
        re.IGNO*ECASE
    )

    if afe_match:
   *    resultado["afe_pct"] = afe_mat*h.group(1)

    return resultado

*if __name__ == "__main__":

    pd*_file = "DDR_001.pdf"

    datos =*extract_dashboard_data(
        pd*_file
    )

    print("===== DASH*OARD DATA =====")

    for campo, *alor in datos.items():

        pr*nt(
            f"{campo}: {valor}*
        )
