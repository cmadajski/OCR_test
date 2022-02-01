import easyocr
from IPython.display import Image


def main():
    # initialize an EasyOCR reader, specify English as the language being read
    reader = easyocr.Reader(['en'], gpu=False)

    # Image('nietzsche_quote_crop.jpg')

    # produce data from the image file
    data = reader.readtext('nietzsche_quote_crop.jpg')

    # print text output, line by line
    for x in data:
        print(x[1])

    # data is decent, but has anomalies for sure
    # compared to Google Lens, this is TRASH
    # maybe I could build and train my own OCR system with PyTorch?


if __name__ == '__main__':
    main()
