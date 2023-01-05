import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoice\*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    filename = Path(filepath).stem
    invoice_nr = filename.split(sep='-')[0]
    pdf.cell(w=0, h=12, txt=f"Invoice_nr.{invoice_nr}", align="L", ln=1, border=0)
    pdf.output(f"PDFs\{filename}.pdf")
