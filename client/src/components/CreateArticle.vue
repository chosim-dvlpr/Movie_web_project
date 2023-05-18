<template>
    <div>
        <input type="text" v-model.trim="createArticle">
        <button @click="submitArticle">제출</button>
    </div>
</template>

<script>
export default {
    name: 'CreateArticle',
    data() {
        return {
            createArticle: null,
        }
    },
    methods: {
        submitArticle() {
            this.$emit('submit-article', this.createArticle)
        }
    }
}
</script>

<style>

</style>