# pdf_splitter.py
import os
import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


# Split a single pdf into multiple documents
def pdf_splitter(inpath, outpath):
    fname = os.path.splitext(os.path.basename(inpath))[0]
    pdf = PdfReader(inpath)

    for page in range(len(pdf.pages)):

        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page])

        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)

        with open(os.path.join(outpath, output_filename), 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))


parser = argparse.ArgumentParser(
    description='A basic PDF file splitter and combiner.  Provide a path and a mode.')     
parser.add_argument(
    '-i', '--inpath', help='The name of the file to be split or the files to be combined')
parser.add_argument(
    '-o', '--outpath', help='The name of the output file or files')
args = parser.parse_args()


if __name__ == '__main__':
    if not os.path.exists(args.outpath):
        os.mkdir(args.outpath)
    pdf_splitter(inpath=args.inpath, outpath=args.outpath)
