from flask import Blueprint, render_template, request, redirect, flash
from models import Turma, Professor
from database import db

bp_turmas = Blueprint('turmas', __name__, template_folder="templates")

@bp_turmas.route("/")
def index():
    t = Turma.query.all()
    return render_template("turmas.html", dados=t)


@bp_turmas.route("/add")
def add():
    t = Turma.query.all()
    p = Professor.query.all()
    return render_template("turmas_add.html", dados=t, professores=p)


@bp_turmas.route("/save", methods=['POST'])
def save():
    nome_disc = request.form.get("nome_disc")
    semestre = request.form.get("semestre")
    id_professor = request.form.get("id_professor")

    professor = Professor.query.all()

    if nome_disc and semestre and id_professor:
        db_turma = Turma(nome_disc, semestre, id_professor)
        db.session.add(db_turma)
        db.session.commit()
        flash("Turma cadastrada!")
        return redirect("/turmas")
    else:
        flash("Preencha todos os campos!")
        return redirect("/turmas/add")
    

@bp_turmas.route("/remove/<int:id>")
def remove(id):
    t = Turma.query.get(id)
    try:
        db.session.delete(t)
        db.session.commit()
        flash("Turma removida!")
    except:
        flash("Turma Inválida!")
    return redirect("/turmas")


@bp_turmas.route("/edit/<int:id>")
def edit(id):
    t = Turma.query.get(id)
    p = Professor.query.all()
    return render_template("turmas_edit.html", dados=t, professores=p)


@bp_turmas.route("/edit-save", methods=['POST'])
def edit_save():
    nome_disc = request.form.get("nome_disc")
    semestre = request.form.get("semestre")
    id_professor = request.form.get("id_professor")
    id = request.form.get("id")
    if nome_disc and semestre and id_professor and id:
        t = Turma.query.get(id)
        t.nome_disc = nome_disc
        t.semestre = semestre
        t.id_professor = id_professor
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/turmas")