import fitz  # PyMuPDF
import pyperclip as pc  # Copying to the clipboard
import sys  # Get the pdf path

# Specify the path to your pdf file
try:
    pdf_path = sys.argv[1]
except:
    raise Exception("There's no path provided to extract the highlights from")

# Create a document object using the fitz.open function
doc = fitz.open(pdf_path)

parts = []
# Loop through each page in the document
for page in doc:
    annot = page.first_annot

    # As long as there are annotations
    while annot:
        if annot.type[0] in (8, 9, 10, 11):
            rect = annot.rect
            parts.append(page.get_text(clip=rect).strip())
        annot = annot.next

# Importing all the highlights to the clipboard
pc.copy("\n".join(parts))

# Terminating the script
doc.close()
print("Highlights successfully copied to the clipboard")
