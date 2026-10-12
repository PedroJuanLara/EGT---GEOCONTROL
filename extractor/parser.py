from dataclasses import dataclass
import re

from pdf_reader import read_pdf


@dataclass
class DDRData:

    reporte: int = 0

    fecha: str = ""

    dia_campania: int = 0

    md: float = 0.0

    tvd: float = 0.0

    hole_made: float = 0.0

    rop: float = 0.0

    coste_acumulado: float = 0.0

    afe_pct: float = 0.0

    npt: float = 0.0


def parse_ddr(pdf_path):

    texto = read_pdf(pdf_path)

    ddr = DDRData()

    # --------------------------------
    # DDR NUMBER
    # --------------------------------

    match = re.search(
        r"DDR\s*(\d+)",
        texto,
        re.IGNORECASE
    )

    if match:
        ddr.reporte = int(match.group(1))
# --------------------------------
# FECHA
# --------------------------------

fecha_match = re.search(
    r"(\d{2}/\d{2}/\d{4})",
    texto
)

if fecha_match:
    ddr.fecha = fecha_match.group(1)
# --------------------------------
# MEASURED DEPTH
# --------------------------------

md_match = re.search(
    r"Measured\s+Depth.*?(\d+\.\d+)",
    texto,
    re.IGNORECASE
)

if md_match:
    ddr.md = float(
        md_match.group(1)
    )
    # -------*------------------------
# TVD
# -*------------------------------*
tvd_match = re.search(
    r"T*D**?(\d+\.\d+)",
    texto,
    re.I*NORECASE
)

if tvd_match:
    ddr.*vd = float(
        tvd_match.grou*(1)
    )
    # --------------------------------
# HOLE MADE
# --------------------------------

hole_match = re.search(
    r"Hole\s+Made.*?(\d+\.\d+)",
    texto,
    re.IGNORECASE
)

if hole_match:
    ddr.hole_made = float(
        hole_match.group(1)
    )
    # --------------------------------
# ROP
# --------------------------------

rop_match = re.search(
    r"Average\s+ROP.*?(\d+\.\d+)",
    texto,
    re.IGNORECASE
)

if rop_match:
    ddr.rop = float(
        rop_match.group(1)
    )
    return ddr


if __name__ == "__main__":

    resultado = parse_ddr(
        "test_data/20260514 TSA-01 Daily Report with cost DDR 01.pdf"
    )

    print("===== DDR EXTRAIDO =====")

print(
    f"Reporte: {resultado.reporte}"
)

print(
    f"Fecha: {resultado.fecha}"
)
print(
    f"MD: {resultado.md}"
)
print(
   f"TVD: {resultado.tvd}"
)
print(
    f"Hole Made: {resultado.hole_made}"
)
print(
    f"ROP: {resultado.rop}"
)
