from flask import Flask, render_template
from app.forms import cliente_form
from app.models import cliente_models
from app import app, db

@app.route("/cadrastra_cliente", methods=['GET', 'POST'])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_models.Cliente(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao, sexo=sexo)

        try:
            db.sesion.add(cliente)
            db.sesion.commit()
        except:
            print("Cliente não cadastrado")


    return render_template("clientes/form.html", form=form)