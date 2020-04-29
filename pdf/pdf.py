import PyPDF2
import sys

files = sys.argv[1:]


def pdf_comb(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("doc-output.pdf")


pdf_comb(files)
