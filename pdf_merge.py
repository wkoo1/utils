from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["F:/Dropbox/application/Overleaf/wangkai-修論/00titlepage.pdf", "F:/Dropbox/application/Overleaf/wangkai-修論-概要/abstract.pdf", "F:/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai.pdf"]:
    merger.append(pdf)

merger.write("F:/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai_Complete.pdf")
merger.close()