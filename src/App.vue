<template>
  <div>
    <h2>Questionnaires</h2>
    <form @submit.prevent="addQuestionnaire">
      <input v-model="newQuestionnaire" required placeholder="Nom du questionnaire">
      <button>Ajouter un questionnaire</button>
    </form>
    <ul>
      <questionnaire-item
        v-for="questionnaire in questionnaires"
        :key="questionnaire.id"
        :questionnaire="questionnaire"
        @remove="removeQuestionnaire"
        @save="saveQuestionnaire"
      />
    </ul>
  </div>
</template>

<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';


export default {
  components: {
    QuestionnaireItem
  },
  data() {
    return {
      newQuestionnaire: '',
      questionnaires: []
    }
  },
  async mounted() {
    await this.getQuestionnaires();
  },
  methods: {
    async getQuestionnaires() {
      try {
        const response = await fetch('http://127.0.0.1:5000/questionnaires');
        const data = await response.json();
        console.log(data);
        this.questionnaires = data;
      } catch (error) {
        console.error('Erreur lors de la récupération des questionnaires:', error);
      }
    },

    async addQuestionnaire() {
      try {
        const response = await fetch('http://127.0.0.1:5000/questionnaires', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: this.newQuestionnaire
          })
        });
        const data = await response.json();
        console.log(data);
        await this.getQuestionnaires();
        this.newQuestionnaire = '';
      } catch (error) {
        console.error('Erreur lors de l\'ajout du questionnaire:', error);
      };
    },
    async removeQuestionnaire(questionnaire) {
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${questionnaire.id}`, {
          method: 'DELETE'
        });
        await this.getQuestionnaires();
      } catch (error) {
        console.error('Erreur lors de la suppression du questionnaire:', error);
      }

    },
    async saveQuestionnaire(questionnaire) {
      console.log(questionnaire);
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
        await this.getQuestionnaires();
      } catch (error) {
        console.error('Erreur lors de la sauvegarde du questionnaire:', error);
      }
    }
  }
}
</script>
