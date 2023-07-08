import os
from io import BytesIO

from PyPDF2 import PdfFileReader
from docx import Document


class FileUtils:

    def get_file_extension_from_file_name(self, filename: str) -> str:
        """

        :param filename:
        :return:
        """
        return os.path.splitext(filename)[1].lower()

    def get_content_from_stream(self, file_data_stream: bytes, extension: str) -> str:
        """

        :param file_data_stream:
        :param extension:
        :return:
        """
        content = ''
        match extension:
            case ".pdf":
                pdf = PdfFileReader(file_data_stream)
                number_of_pages = pdf.numPages

                for page_number in range(number_of_pages):
                    page = pdf.getPage(page_number)
                    content += page.extractText()

            case ".txt":
                content = file_data_stream.decode("utf-8")
            case ".docx":
                document = Document(BytesIO(file_data_stream))

                for paragraph in document.paragraphs:
                    content += paragraph.text + "\n"
            case _:
                content = ''

        return self.__sanitise_data(content)

    def __sanitise_data(self, content_entry: str) -> str:
        """

        :param content_entry:
        :return:
        """
        # Create a custom list of stop words
        custom_stop_words = ['\n', '\r', '\s', '\p', "\\u"]

        # Tokenize the input string
        word_list = content_entry.split()
        # Remove stop words
        filtered_tokens = [word for word in word_list if word.lower() not in custom_stop_words]

        # Join the filtered tokens back into a string
        filtered_string = ' '.join(filtered_tokens)
        filtered_string = filtered_string.replace('\\u', '')

        return filtered_string
