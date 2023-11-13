from flask import Flask, render_template
from app.forms import cliente_form
from app import app

@app.route("/cadrastra_cliente")
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    return render_template("clientes/form.html", form=form)