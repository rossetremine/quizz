<template>
  <li>
    <div v-if="!question.editing">
      {{ question.title }} - {{ question.questionType }}
      <button @click="editQuestion">Editer</button>
    </div>
    <div v-else>
      <input v-model="question.title" required>
      <input v-model="question.questionType" required>
      <button @click="saveQuestion">Enregistrer</button>
    </div>
    <button @click="removeQuestion">Supprimer</button>
  </li>
</template>

<script>
export default {
  props: ['question'],
  methods: {
    removeQuestion() {
      this.$emit('remove', this.question);
    },
    editQuestion() {
      this.question.editing = true;
    },
    saveQuestion() {
      this.$emit('save', this.question);
    }
  }
}
</script>
