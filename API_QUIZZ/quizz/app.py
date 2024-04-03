from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse


app = Flask( __name__ )


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizz.db'
app.config['SECRET_KEY'] = 'iMQWPgaEP2WQQUxPvKiYiZoP5jaP5RdzGoE4msqtGFTJgSVKTwVH3SEUGsjRRTkFZMKqXKmCsAaEWbdjWJEb8ip2rNi4hCKezTxe5VVXfiAgDfYzdLRAEqf3dou8gGwr'

db: SQLAlchemy = SQLAlchemy(app)
api = Api(app)

class Question_api(Resource):
    def get(self, question_id):
        from quizz.models import Question
        question = db.session.query(Question).get_or_404(question_id)
        return question.to_json()

    def delete(self, question_id):
        from quizz.models import Question
        db.session.delete(db.session.query(Question).get_or_404(question_id))
        db.session.commit()
        return '', 204


    def put(self, question_id):
        from quizz.models import Question
        question = db.session.query(Question).get_or_404(question_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='Title of the question')
        parser.add_argument('questionType', type=str, help='Type of the question')
        parser.add_argument('questionnaire_id', type=int, help='Id of the questionnaire')
        args = parser.parse_args()
        if args['title'] is not None:
            question.title = args['title']
        if args['questionType'] is not None:
            question.questionType = args['questionType']
        if args['questionnaire_id'] is not None:
            question.questionnaire_id = args['questionnaire_id']
        db.session.commit()
        return '', 200

class QuestionByQuestionnaire_api(Resource):
    def get(self, questionnaire_id):
        from quizz.models import Question
        questions = db.session.query(Question).filter(Question.questionnaire_id == questionnaire_id).all()
        return jsonify([question.to_json() for question in questions])
    


class Questions_api(Resource):
    def get(self):
        from quizz.models import Question
        questions = db.session.query(Question).all()
        return jsonify([question.to_json() for question in questions])

    def post(self):
        from quizz.models import Question
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='Title of the question')
        parser.add_argument('questionType', type=str, help='Type of the question')
        parser.add_argument('questionnaire_id', type=int, help='Id of the questionnaire')
        args = parser.parse_args()
        db.session.add(Question(args['title'], args['questionType'], args['questionnaire_id']))
        db.session.commit()
        return '', 201


class Questionnaire_api(Resource):
    def get(self, questionnaire_id):
        from quizz.models import Questionnaire
        questionnaire = db.session.query(Questionnaire).get_or_404(questionnaire_id)
        return jsonify(questionnaire.to_json())
        

    def delete(self, questionnaire_id):
        from quizz.models import Questionnaire
        db.session.delete(db.session.query(Questionnaire).get_or_404(questionnaire_id))
        db.session.commit()
        return '', 204

    def put(self, questionnaire_id):
        from quizz.models import Questionnaire
        questionaire =db.session.query(Questionnaire).get_or_404(questionnaire_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Name to give to the questionnaire')
        args = parser.parse_args()
        questionaire.name = args['name']
        db.session.commit()
        return '', 200
    

class Questionnaires_api(Resource):
    def get(self):
        from quizz.models import Questionnaire
        questionnaires = db.session.query(Questionnaire).all()
        return jsonify([questionnaire.to_json() for questionnaire in questionnaires])
        

    def post(self):
        from quizz.models import Questionnaire
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Name to give to the questionnaire')
        args = parser.parse_args()
        db.session.add(Questionnaire(args['name']))
        db.session.commit()
        return '', 201

api.add_resource(Questions_api, '/questions')
api.add_resource(Question_api, '/questions/<int:question_id>')

api.add_resource(QuestionByQuestionnaire_api, '/questions/questionnaire/<int:questionnaire_id>')

api.add_resource(Questionnaires_api, '/questionnaires')
api.add_resource(Questionnaire_api, '/questionnaires/<int:questionnaire_id>')


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.create_all()
    db.session.commit()
    print('Initialized the database.')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

