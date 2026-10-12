from pypdf import PdfReader


def read_pdf(pdf_path):

    texto_completo = ""

    reader = PdfReader(pdf_path)

    for pagina in reader.pages:

        texto = pagina.extract_text()

        if texto:
            texto_completo += texto
            texto_completo += "\n\n"

    return texto_completo
