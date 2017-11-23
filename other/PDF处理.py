#!/usr/bin/env python

import pdfkit
from PyPDF2 import PdfFileReader, PdfFileWriter


def generate_from_string():
    options = {
        'page-size': 'A4',
        'orientation': 'Landscape',
        'encoding': 'utf-8',
    }
    pdfkit.from_string('<h1><a href="https://chenjiabing666.gituhb.io">陈加兵的博客</a></h1>', '../data/demo.pdf', options=options)


def generate_from_url():
    options = {
        'page-size': 'A4',
        'orientation': 'Landscape',
        'encoding': 'utf-8',
    }
    pdfkit.from_url('https://wkhtmltopdf.org/downloads.html', '../data/demo.pdf', options=options)


def merge_pdf():
    pdf1 = PdfFileReader(open('../data/test1.pdf', "rb"))
    pdf2 = PdfFileReader(open('../data/test2.pdf', "rb"))
    output = PdfFileWriter()
    for i in range(pdf1.getNumPages()):
        output.addPage(pdf1.getPage(i))
    for i in range(pdf2.getNumPages()):
        output.addPage(pdf2.getPage(i))
    out_stream = open('../data/merge.pdf', "wb")
    output.write(out_stream)
    out_stream.close()


def pick_up_pdf(start, end):
    pdf = PdfFileReader(open('../data/test3.pdf', "rb"))
    output = PdfFileWriter()
    for i in range(pdf.getNumPages()):
        if start <= i <= end:
            output.addPage(pdf.getPage(i))
    out_stream = open('../data/result.pdf', "wb")
    output.write(out_stream)
    out_stream.close()


generate_from_url()
