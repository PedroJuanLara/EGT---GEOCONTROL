"""
EGT GeoControl
DDR Parser V1

Objetivo:
Leer Daily Drilling Reports (DDR)
y extraer información estructurada.

Versión inicial:
Todavía no procesa PDFs.
Solo define los campos objetivo.
"""

from dataclasses import dataclass


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

    """
    Función principal del extractor.

    Entrada:
        PDF DDR

    Salida:
        DDRData
    """

    ddr = DDRData()

    return ddr


if __name__ == "__main__":

    ejemplo = parse_ddr(
        "DDR_001.pdf"
    )

    print(ejemplo)
