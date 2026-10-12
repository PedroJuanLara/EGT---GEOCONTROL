from dataclasses import dataclass
import re

from extractor.pdf_reader import read_pdf


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

    # Reporte
    if "Report No" in texto:
        ddr.reporte = 1

    # Fecha
    fecha_match = re.search(
        r"(\d{2}-[A-Za-z]{3}-\d{2})",
        texto
    )

    if fecha_match:
        ddr.fecha = fecha_match.group(1)

    # MD
    md_match = re.search(
        r"Measured Depth \(m\):\s*(\d+\.\d+)",
        texto
    )

    if md_match:
        ddr.md = float(md_match.group(1))
        ddr.tvd = ddr.md

    # Hole Made
    hole_match = re.search(
        r"Hole Made \(m\) / Hrs:\s*(\d+\.\d+)",
        texto
    )

    if hole_match:
        ddr.hole_made = float(hole_match.group(1))

    # ROP
    rop_match = re.search(
        r"Average ROP \(m/hr\):\s*(\d+\.\d+)",
        texto
    )

    if rop_match:
        ddr.rop = float(rop_match.group(1))

    # Coste acumulado (primera versión)
    costes = re.findall(
        r"(\d{1,3}(?:,\d{3})+)",
        texto
    )

    if len(costes) > 0:

        try:
            ddr.coste_acumulado = float(
                costes[0].replace(",", "")
            )

        except:
            pass

    return ddr
