"""
EGT GeoControl

PDF Reader V1

Objetivo:
Leer el contenido de un DDR PDF
y mostrar el texto extraído.

Dependencia:
pypdf
"""

from pypdf import PdfReader


def read_pdf(pdf_path):
    """
    Lee un PDF y devuelve todo el texto.
    """

    texto_completo = ""

    reader = PdfReader(pdf_path)

    for pagina in reader.pages:

        texto = pagina.extract_text()

        if texto:
            texto_completo += texto
            texto_completo += "\n\n"

    return texto_completo


if __name__ == "__main__":

    pdf_file = "DDR_001.pdf"

    contenido = read_pdf(pdf_file)

    print("===== TEXTO EXTRAÍDO =====")
    print(contenido[:5000])
``
