from fpdf import FPDF

def clean_text(text):
    # Replace common unicode characters with ASCII equivalents
    replacements = {
        '\u2013': '-',  # en dash
        '\u2014': '-',  # em dash
        '\u2018': "'",  # left single quote
        '\u2019': "'",  # right single quote
        '\u201c': '"',  # left double quote
        '\u201d': '"',  # right double quote
        '\u2022': '*',  # bullet
        '\u00a0': ' ',  # non-breaking space
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text.encode('ascii', errors='ignore').decode('ascii')

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Resume-Job Match Report", ln=True, align="C")

    def add_content(self, content):
        self.set_font("Arial", "", 11)
        cleaned = clean_text(content)
        for line in cleaned.split('\n'):
            self.multi_cell(0, 10, line)

def generate_pdf(report_text):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_content(report_text)
    return pdf.output(dest='S').encode('latin1')
