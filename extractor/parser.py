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

    # 1. Número de Reporte real (ej. "Report No: 5")
    reporte_match = re.search(r"Report\s*No[:\s]*(\d+)", texto, re.IGNORECASE)
    if reporte_match:
        ddr.reporte = int(reporte_match.group(1))

    # 2. Fecha (ej. "12-Oct-26")
    fecha_match = re.search(r"(\d{2}-[A-Za-z]{3}-\d{2})", texto)
    if fecha_match:
        ddr.fecha = fecha_match.group(1)

    # 3. Measured Depth (MD)
    md_match = re.search(r"Measured Depth \(m\):\s*(\d+\.\d+)", texto)
    if md_match:
        ddr.md = float(md_match.group(1))
        ddr.tvd = ddr.md  # O busca el TVD específico si lo prefieres

    # 4. Hole Made (m) / Hrs
    hole_match = re.search(r"Hole Made \(m\)\s*/\s*Hrs:\s*(\d+\.\d+)", texto)
    if hole_match:
        ddr.hole_made = float(hole_match.group(1))

    # 5. Average ROP (m/hr)
    rop_match = re.search(r"Average ROP \(m/hr\):\s*(\d+\.\d+)", texto)
    if rop_match:
        ddr.rop = float(rop_match.group(1))

    # 6. Coste Acumulado (buscando la etiqueta "Actual ($)" o similar)
    coste_match = re.search(
        r"Actual\s*\(\$\)\s*([\d,]+)", texto, re.IGNORECASE
    )
    if coste_match:
        try:
            ddr.coste_acumulado = float(coste_match.group(1).replace(",", ""))
        except ValueError:
            pass

    return ddr
