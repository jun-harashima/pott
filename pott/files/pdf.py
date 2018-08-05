import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pott.files.file import File
from pott.utils.log import logger


class Pdf(File):

    DIR_NAME = os.environ['HOME'] + '/.pott/pdf'

    def __init__(self, file_name):
        self.set_file_name_and_path(file_name)

    def dir_name(self):
        return self.DIR_NAME

    def save(self, content):
        with open(self.DIR_NAME + '/' + self.file_name, 'wb') as file:
            file.write(content)

    def extract_text(self):
        with open(self.DIR_NAME + '/' + self.file_name, 'rb') as file:
            manager = PDFResourceManager()
            stringio = StringIO()
            laparams = LAParams()
            device = TextConverter(manager, stringio, codec='utf-8',
                                   laparams=laparams)
            interpreter = PDFPageInterpreter(manager, device)
            for page in PDFPage.get_pages(file):
                try:
                    interpreter.process_page(page)
                except ValueError as e:
                    logger.warn(str(e))
            pdfminer_result = stringio.getvalue()
            formed_result = self._form(pdfminer_result)
            return formed_result

    def _form(self, pdfminer_result):
        paragraphs = []
        paragraph = ''
        for line in pdfminer_result.split('\n'):
            if len(line) == 0:
                paragraphs.append(paragraph[:-1])
                paragraph = ''
                continue
            if line[-1:] == '-':
                paragraph += line[:-1]
            else:
                paragraph += line + ' '
        return '\n'.join(paragraphs)
