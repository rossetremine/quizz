from quizz.app import db

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Questionnaire (%d) %s>" % (self.id, self.name)



    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
            'questions': [question.to_json() for question in get_questions_by_questionnaire_id(self.id)]
        }
        return json


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    questionType = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref=db.backref("questions", lazy="dynamic", cascade="all, delete-orphan"))

    def __init__(self, title, questionType, questionnaire_id):
        self.title = title
        self.questionType = questionType
        self.questionnaire_id = questionnaire_id

    def to_json(self):
        json = {
            'id': self.id,
            'title': self.title,
            'questionType': self.questionType,
            'questionnaire_id': self.questionnaire_id
        }
        return json

def get_questions_by_questionnaire_id(questionnaire_id):
    return db.session.query(Question).filter_by(questionnaire_id=questionnaire_id).all()