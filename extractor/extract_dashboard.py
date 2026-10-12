from pdf_reader import read_pdf

pdf_file = (
    "test_data/"
    "20260514 TSA-01 Daily Report with cost DDR 01.pdf"
)

texto = read_pdf(pdf_file)

print(texto[:5000])
