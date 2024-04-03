<template>
    <li>
      <div v-if="!questionnaire.editing">
        {{ questionnaire.name }}
        <button @click="editQuestionnaire">Editer</button>
      </div>
      <div v-else>
        <input v-model="questionnaire.name" required>
        <button @click="saveQuestionnaire">Enregistrer</button>
      </div>
      <button @click="removeQuestionnaire">Supprimer</button>
      <h3>Questions</h3>
      <ul>
        <question-item
          v-for="question in questionnaire.questions"
          :key="question.id"
          :question="question"
          @remove="removeQuestion"
          @edit="editQuestion"
          @save="saveQuestion"
        />
      </ul>
      <form @submit.prevent="addNewQuestion">
        <input v-model="newQuestionText" required placeholder="Nouvelle question">
        <button type="submit">Ajouter une question</button>
      </form>
    </li>
  </template>
  
  <script>
  import QuestionItem from './QuestionItem.vue';
  
  export default {
    components: {
      QuestionItem
    },
    
    props: ['questionnaire'],
    data() {
      return {
        newQuestionText: ''
      }
    },
    methods: {
      async addQuestionnaire() {
      try {
        const response = await fetch('http://127.0.0.1:5000/questionnaires', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: this.newQuestionnaire,
            questions: []
          })
        });
        const data = await response.json();
        this.questionnaires.push(data);
        this.newQuestionnaire = '';
      } catch (error) {
        console.error('Erreur lors de l\'ajout du questionnaire:', error);
      }
    },

    async removeQuestionnaire(questionnaire) {
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${questionnaire.id}`, {
          method: 'DELETE'
        });
        this.questionnaires = this.questionnaires.filter(q => q !== questionnaire);
      } catch (error) {
        console.error('Erreur lors de la suppression du questionnaire:', error);
      }
    },

    async saveQuestionnaire(questionnaire) {
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${questionnaire.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: questionnaire.name
          })
        });
      } catch (error) {
        console.error('Erreur lors de la sauvegarde du questionnaire:', error);
      }
    },

    async addQuestion(questionnaire) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/questionnaires/${questionnaire.id}/questions`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            text: this.newQuestion
          })
        });
        const data = await response.json();
        questionnaire.questions.push(data);
        this.newQuestion = '';
      } catch (error) {
        console.error('Erreur lors de l\'ajout de la question:', error);
      }
    },

    async removeQuestion(questionnaire, question) {
      try {
        await fetch(`http://127.0.0.1:5000/questions/${question.id}`, {
          method: 'DELETE'
        });
        questionnaire.questions = questionnaire.questions.filter(q => q !== question);
      } catch (error) {
        console.error('Erreur lors de la suppression de la question:', error);
      }
    },

    async saveQuestion(question) {
      try {
        await fetch(`http://127.0.0.1:5000/questions/${question.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            text: question.text
          })
        });
      } catch (error) {
        console.error('Erreur lors de la sauvegarde de la question:', error);
      }
    }
  }
}
</script>