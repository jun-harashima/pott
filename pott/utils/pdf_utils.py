from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def extract_text_from(pdf_file):
    manager = PDFResourceManager()
    stringio = StringIO()
    laparams = LAParams()
    device = TextConverter(manager, stringio, codec='utf-8', laparams=laparams)
    interpreter = PDFPageInterpreter(manager, device)
    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)
    return stringio.getvalue()
