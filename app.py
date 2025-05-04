
from flask import Flask, request, send_file
from fpdf import FPDF
import tempfile

app = Flask(__name__)

@app.route('/genera-pdf', methods=['POST'])
def genera_pdf():
    dati = request.json
    cliente = dati.get("cliente", "Cliente")
    totale = dati.get("totale", "0.00")
    note = dati.get("note", "Nessuna nota")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Preventivo per: {cliente}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Note:\n{note}")
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt=f"Totale stimato: {totale} € (IVA esclusa)", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 8, "Il prezzo include la posa con piastrella base a 20 €/mq.\nEsclusi trasporti, carichi e materiali non forniti al piano di posa.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        pdf.output(temp.name)
        return send_file(temp.name, as_attachment=True, download_name="preventivo.pdf")

if __name__ == '__main__':
    app.run()
