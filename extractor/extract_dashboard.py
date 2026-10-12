import re

from pdf_reader import read_pdf


pdf_file = (
    "test_data/"
    "20260514 TSA-01 Daily Report with cost DDR 01.pdf"
)

texto = read_pdf(pdf_file)

print("===== TEXTO EXTRAÍDO =====")

print(texto[:3000])

print("\n")

print("===== BUSCANDO DATOS =====")

match = re.search(
    r"DDR\s*(\d+)",
    texto,
    re.IGNORECASE
)

if match:

    print(
        f"Reporte encontrado: {match.group(1)}"
    )

else:

    print(
        "No se encontró número de reporte"
    )
