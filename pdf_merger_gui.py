import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def select_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        pdf_list.extend(file_paths)
        status_label.config(text=f"{len(pdf_list)} PDFs selected.")

def merge_pdfs():
    if not pdf_list:
        messagebox.showwarning("No Files", "Please select PDF files first.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF Files", "*.pdf")],
                                             title="Save Merged PDF As")
    if save_path:
        merger = PdfMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(save_path)
        merger.close()
        messagebox.showinfo("Success", f"PDFs merged and saved to:\n{save_path}")
        pdf_list.clear()
        status_label.config(text="Ready")

# GUI Setup
pdf_list = []
root = tk.Tk()
root.title("PDF Merger Tool")

tk.Label(root, text="PDF Merger Tool", font=("Helvetica", 16)).pack(pady=10)
tk.Button(root, text="Select PDF Files", command=select_pdfs).pack(pady=5)
tk.Button(root, text="Merge PDFs", command=merge_pdfs).pack(pady=5)
status_label = tk.Label(root, text="Ready", fg="blue")
status_label.pack(pady=10)

root.geometry("300x200")
root.mainloop()
