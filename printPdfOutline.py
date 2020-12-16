import sys
import PyPDF2

def visit(node, level):
  if isinstance(node, PyPDF2.pdf.Destination):
    prefix = level * '+'
    print('{0}"{1}"|{2}'.format(prefix, node.title, node.page+1))
  else:
    for child in node:
      visit(child, level+1)

if __name__ == "__main__":
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    reader = PyPDF2.PdfFileReader(filename)
    root = reader.getOutlines()
    visit(root, 0)
  else:
    print('Usage:')
    print('  $ python3 printPdfOutline.py <FILE.pdf> [> toc.txt]')
