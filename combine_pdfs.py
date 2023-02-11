# pdf_splitter.py
import os
import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


# Combine multiple pdfs into one document 
def pdf_combiner(inpath, outpath):

    paths = Path(inpath).glob("*.pdf") 
    print("Paths before:", paths)
    paths = sorted(list(map(lambda x: str(x), paths)))
    print("Paths after:", paths)

    merger = PdfWriter()
    for path in paths:
        merger.append(path)

    with open(outpath, 'wb') as out:
        merger.write(out)
        merger.close()


parser = argparse.ArgumentParser(
    description='A basic PDF file splitter and combiner.  Provide a path and a mode.')     
parser.add_argument(
    '-i', '--inpath', help='The name of the file to be split or the files to be combined')
parser.add_argument(
    '-o', '--outpath', help='The name of the output file or files')
args = parser.parse_args()


if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(args.outpath)):
        os.mkdir(os.path.dirname(args.outpath))
    pdf_combiner(inpath=args.inpath, outpath=args.outpath)
    
