import PyPDF2
import os

pdf_folder = 'pdfs_to_merge'
output_pdf = 'merged_output.pdf'

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
pdf_files.sort()

merger = PyPDF2.PdfMerger()

for pdf in pdf_files:
    path = os.path.join(pdf_folder, pdf)
    merger.append(path)

merger.write(output_pdf)
merger.close()

print("✅ PDFs merged into:", output_pdf)
