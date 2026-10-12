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

    return ddr


if __name__ == "__main__":

    resultado = parse_ddr(
        "test_data/20260514 TSA-01 Daily Report with cost DDR 01.pdf"
    )

    print(resultado)
