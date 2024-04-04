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
      <h5>Questions</h5>
      <ul>
        <question-item
          v-for="question in questions"
          :key="question.id"
          :question="question"
          @remove="removeQuestion"
          @save="saveQuestion"
        />
      </ul>
      <form @submit.prevent="addNewQuestion">
        <input v-model="newQuestionTitle" required placeholder="Nouvelle question">
        <input v-model="newQuestionType" required placeholder="Type de question">
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
        questions: [],
        newQuestionText: ''
      }
    },
    async mounted() {
      await this.getQuestions();
    },
    methods: {

      removeQuestionnaire() {
        this.$emit('remove', this.questionnaire);
      },
      editQuestionnaire() {
        this.questionnaire.editing = true;
      },
      saveQuestionnaire() {
        this.$emit('save', this.questionnaire);
        this.questionnaire.editing = false;
      },

      async getQuestions() {
        try {
          const response = await fetch(`http://127.0.0.1:5000/questions/questionnaire/${this.questionnaire.id}`);
          const data = await response.json();
          this.questions = data;
          console.log(this.questions);
        } catch (error) {
          console.error('Erreur lors de la récupération des questions:', error);
        }
      },

      async addNewQuestion() {
        try {
          const response = await fetch('http://127.0.0.1:5000/questions', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              title: this.newQuestionTitle,
              questionType: this.newQuestionType,
              questionnaire_id: this.questionnaire.id
            })
          });
          const data = await response.json();
          console.log(data);
          this.newQuestionTitle = '';
          this.newQuestionType = '';
          await this.getQuestions();

        } catch (error) {
          console.error('Erreur lors de l\'ajout de la question:', error);
        }
      },

      async removeQuestion(question) {
        console.log(question);
        try {
          await fetch(`http://127.0.0.1:5000/questions/${question.id}`, {
            method: 'DELETE'
          });
          await this.getQuestions();
        } catch (error) {
          console.error('Erreur lors de la suppression de la question:', error);
        }
      },

      async saveQuestion(question) {
        console.log(question);
        try {
          await fetch(`http://127.0.0.1:5000/questions/${question.id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              title: question.title,
              questionType: question.questionType
            })
          });
          await this.getQuestions();
        } catch (error) {
          console.error('Erreur lors de la sauvegarde de la question:', error);
        }
      }

      
  }
}
</script>