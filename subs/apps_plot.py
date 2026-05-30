"""
G63 — apps_plot.py
"""
from flask import render_template, session
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    ulogin = session.get("user")
    if ulogin is not None:
        engine = create_engine('sqlite:///' + filename + 'g63_database.db')

        # 1. Total amount per supermarket chain (bar chart)
        df = pd.read_sql("""
            SELECT s.name, ROUND(SUM(t.amount), 2) as total
            FROM Transation t
            JOIN Supermarket s ON t.supermarket_id = s.supermarket_id
            GROUP BY s.name ORDER BY total DESC
        """, con=engine)

        fig, ax = plt.subplots(figsize=(8, 4))
        plt.bar(df['name'], df['total'], width=0.5, color='steelblue')
        plt.xlabel('Supermarket Chain')
        plt.ylabel('Total Amount (€)')
        plt.xticks(rotation=20, ha='right')
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        image1 = base64.b64encode(buf.getvalue()).decode('utf-8')

        # 2. Number of transations per supplier type (bar chart)
        df2 = pd.read_sql("""
            SELECT sup.supplier_type, COUNT(*) as count
            FROM Transation t
            JOIN Supplier sup ON t.supplier_id = sup.supplier_id
            GROUP BY sup.supplier_type ORDER BY count DESC
        """, con=engine)

        fig2, ax2 = plt.subplots(figsize=(8, 4))
        plt.bar(df2['supplier_type'], df2['count'], width=0.5, color='seagreen')
        plt.xlabel('Supplier Type')
        plt.ylabel('Number of Transations')
        plt.xticks(rotation=20, ha='right')
        plt.tight_layout()

        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png')
        plt.close(fig2)
        buf2.seek(0)
        image2 = base64.b64encode(buf2.getvalue()).decode('utf-8')

        return render_template("plot.html", image1=image1, image2=image2,
                               ulogin=ulogin)
    else:
        return render_template("index.html", ulogin=ulogin)
