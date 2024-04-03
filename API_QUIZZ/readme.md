# API Quizz

Cette API permet de gérer des questions et des questionnaires pour un quizz.

## Installation

1. Cloner ce dépôt
2. Installer les dépendances : `pip install -r requirements.txt` (Il est recommandé de créer un environnement virtuel)
3. Initialiser la base de données : `flask initdb`
4. Lancer l'API : `flask run`
5. Lancer le client : `http://127.0.0.1:5000/static/index.html`


## Fonctionnalités

Client web pour consulter, créer, modifier et supprimer des questionnaires et questions

### Questionnaires

#### Récupérer tous les questionnaires

```bash
curl http://127.0.0.1:5000/questionnaires
```

### Récupérer un questionnaire spécifique

```bash
curl http://127.0.0.1:5000/questionnaires/<questionnaire_id>
```

### Créer un nouveau questionnaire

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"Nom_du_questionnaire"}' http://127.0.0.1:5000/questionnaires
```

### Mettre à jour un questionnaire existant

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Nouveau_nom_du_questionnaire"}' http://127.0.0.1:5000/questionnaires/<questionnaire_id>
```

### Supprimer un questionnaire

```bash
curl -X DELETE http://127.0.0.1:5000/questionnaires/<questionnaire_id>
```
### Questions

#### Récupérer toutes les questions

```bash
curl http://127.0.0.1:5000/questions
```

#### Récupérer une question spécifique

```bash
curl http://127.0.0.1:5000/questions/<question_id>
```

#### Créer une nouvelle question

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"Titre_de_la_question", "questionType":"Type_de_question", "questionnaire_id":"ID_du_questionnaire"}' http://127.0.0.1:5000/questions

```

#### Mettre à jour une question existante

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Nouveau_titre"}' http://127.0.0.1:5000/questions/<question_id>

```

#### Supprimer une question

```bash
curl -X DELETE http://127.0.0.1:5000/questions/<question_id>
```

#### Récupérer toutes les questions pour un questionnaire donné

```bash
curl http://127.0.0.1:5000/questions/questionnaire/<questionnaire_id>
```

## Auteur

Créé par Marin TREMINE 22B.