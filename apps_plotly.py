"""
G63 — apps_plotly.py
Plotly interactive charts
Follows professor's pattern from lesson 13 apps_plotly.py
Responsável: Membro 4
"""
from flask import render_template, session
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    ulogin = session.get("user")
    if ulogin is not None:
        engine = create_engine('sqlite:///' + filename + 'g63_database.db')

        # Monthly transaction volume — line chart
        df = pd.read_sql("""
            SELECT strftime('%Y-%m', delivery_date) as month,
                   ROUND(SUM(amount), 2) as total
            FROM Transation
            GROUP BY month ORDER BY month
        """, con=engine)

        fig = px.line(df, x='month', y='total',
                      labels={'month': 'Month', 'total': 'Total (€)'},
                      title='Monthly Transaction Volume (€)')

        plot_div = fig.to_html(full_html=False, div_id='my-plot')

        return render_template("plotly.html", plot_div=plot_div,
                               ulogin=ulogin)
    else:
        return render_template("index.html", ulogin=ulogin)
