<template>
    <div>
        <input type="text" v-model.trim="createReview" @keyup.enter="submitReview">
        <button @click="submitReview">제출</button>
    </div>
</template>

<script>
export default {
    name: 'CreateReview',
    data() {
        return {
            createReview: null,
        }
    },
    methods: {
        submitReview() {
            this.$emit('submit-review', this.createReview)
            this.createReview = ''
        }
    }
}
</script>

<style>

</style>