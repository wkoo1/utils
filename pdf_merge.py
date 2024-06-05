from pypdf import PdfWriter

merger = PdfWriter()

# for pdf in ["D:/oukai/Dropbox/application/Overleaf/wangkai-修論/00titlepage.pdf", "D:/oukai/Dropbox/application/Overleaf/wangkai-修論-概要/abstract.pdf", "D:/oukai/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai.pdf"]:
#     merger.append(pdf)

# merger.write("D:/oukai/Dropbox/application/Overleaf/wangkai-修論/MasterThesis_WangKai_Complete.pdf")
# merger.close()

for pdf in ["D:/oukai/D2/IMA.R1投稿/Response_Letter_IMA_wang_2.pdf", "D:/oukai/D2/IMA.R1投稿/Preparation_of_Papers_for_IMA_Revision2_track.pdf"]:
    merger.append(pdf)

merger.write("D:/oukai/D2/IMA.R1投稿/Preparation_of_Papers_for_IMA_Revision2_track_2024.6.3.pdf")
merger.close()