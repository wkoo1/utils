from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["D:/oukai/Dropbox/application/Overleaf/wangkai-修論/00titlepage.pdf", "D:/oukai/Dropbox/application/Overleaf/wangkai-修論/0abstract.pdf", "D:/oukai/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai.pdf"]:
    merger.append(pdf)

merger.write("D:/oukai/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai_Complete.pdf")
merger.close()