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
        @edit="editQuestionnaire"
        @save="saveQuestionnaire"
      />
    </ul>
  </div>
</template>

<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';

// donne à chaque questionnaire un id unique
let questionnaireId = 0;

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
  methods: {
    addQuestionnaire() {
      this.questionnaires.push({
        id: questionnaireId++,
        name: this.newQuestionnaire,
        questions: []
      });
      this.newQuestionnaire = '';
    },
    removeQuestionnaire(questionnaire) {
      this.questionnaires = this.questionnaires.filter(q => q !== questionnaire);
    },
    editQuestionnaire(questionnaire) {
      questionnaire.editing = true;
    },
    saveQuestionnaire(questionnaire) {
      questionnaire.editing = false;
    }
  }
}
</script>
