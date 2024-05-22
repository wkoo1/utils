from pypdf import PdfWriter

merger = PdfWriter()

# for pdf in ["D:/oukai/Dropbox/application/Overleaf/wangkai-修論/00titlepage.pdf", "D:/oukai/Dropbox/application/Overleaf/wangkai-修論-概要/abstract.pdf", "D:/oukai/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai.pdf"]:
#     merger.append(pdf)

# merger.write("D:/oukai/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai_Complete.pdf")
# merger.close()

for pdf in ["D:/oukai/D1/IMA投稿/Response_Letter_IMA_wang_2024.4.17.pdf", "D:/oukai/D1/IMA投稿/IMA_draftpaper_revision1_wang_2024.4.17.pdf"]:
    merger.append(pdf)

merger.write("D:/oukai/D1/IMA投稿/IMA_draftpaper_revision1_2024.4.17.pdf")
merger.close()