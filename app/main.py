import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

def generate_report():
    df = pd.read_csv("data/sample.csv")
    df.plot(kind="bar", x="Categoria", y="Valor")
    plt.savefig("reports/plot.png")

    c = canvas.Canvas("reports/relatorio.pdf")
    c.drawString(100, 800, "Relatório de Dados")
    c.drawImage("reports/plot.png", 100, 400, width=400, height=300)
    c.save()

if __name__ == "__main__":
    generate_report()
