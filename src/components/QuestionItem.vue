<template>
  <li>
    <div v-if="!question.editing">
      {{ question.text }}
      <button @click="editQuestion">Editer</button>
    </div>
    <div v-else>
      <input v-model="question.text" required>
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
      this.$emit('edit', this.question);
    },
    saveQuestion() {
      this.$emit('save', this.question);
    }
  }
}
</script>
