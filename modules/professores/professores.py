from flask import Blueprint, render_template, request, redirect, flash
from models import Professor
from database import db

bp_professores = Blueprint('professores', __name__, template_folder="templates")

@bp_professores.route("/")
def index():
    p = Professor.query_all()
    return render_template("professores.html", dados=p)


@bp_professores.route("/add")
def add():
    return render_template("professores_add.html")


@bp_professores.route("/save")
def save():
    nome = request.form.get("nome")
    dpto = request.form.get("dpto")
    if nome and dpto:
        db_professor = Professor(nome, dpto)
        db.session.add(db_professor)
        db.session.commit()
        flash("Professor cadastrado!")
        return redirect("/professores")
    else:
        flash("Preencha todos os campos!")
        return redirect("/professores/add")
    

@bp_professores.route("/remove/<int:id>")
def remove():
    p = Professor.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Professor removido!")
    except:
        flash("Professor Inválido!")
    return redirect("/professores")


@bp_professores.route("/edit/<int:id>")
def edit():
    p = Professor.query.get(id)
    return render_template("professores_edit.html", dados=p)


@bp_professores.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    dpto = request.form.get("dpto")
    id = request.form.get("id")
    if nome and dpto and id:
        p = Professor.query.get(id)
        p.nome = nome
        p.dpto = dpto
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/professores")