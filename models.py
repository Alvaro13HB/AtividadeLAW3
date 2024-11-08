from database import db

class Professor(db.Model):
    __tablename__ = 'tb_professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    dpto = db.Column(db.String(50))


    def __init__(self, nome, dpto):
        self.nome = nome
        self.dpto = dpto


    def __repr__(self):
        return f"<Professor {self.nome}>"
    

class Turma(db.Model):
    __tablename__ = 'tb_turma'
    id = db.Column(db.Integer, primary_key=True)
    nome_disc = db.Column(db.String(100))
    semestre = db.Column(db.String(10))
    id_professor = db.Column(db.Integer, db.ForeignKey('tb_professor.id'))

    professor = db.relationship('Professor', foreign_keys=id_professor)


    def __init__(self, nome_disc, semestre, id_professor):
        self.nome_disc = nome_disc
        self.semestre = semestre
        self.id_professor = id_professor

    
    def __repr__(self):
        return f"<Turma {self.nome_disc} - {self.professor.nome}>"