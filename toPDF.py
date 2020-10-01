from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak
import textwrap

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    rlist = []
    for i in range(0, len(l), n):
        rlist.append(l[i:i + n])
    return rlist

def genPDF(ciphertexts):
    doc = SimpleDocTemplate("CipherTest.pdf", pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    for ciphertext in ciphertexts:
        data = [['ciphertext'] + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                ['plaintext'] + list(' ' * 26)]
        t = Table(data)
        t.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER')
                               ]))
        elements.append(t)

        for line in chunks(list(ciphertext.upper()), 26):
            data = []
            elements.append(Spacer(1, 0.1 * inch))
            data.append(line)
            data.append(list(' ' * (len(line))))
            t2 = Table(data, colWidths=0.25 * inch)
            t2.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER')
                                    ]))
            elements.append(t2)
        elements.append(PageBreak())

    # write the document to disk
    doc.build(elements)