<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/paul_logo.png')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-card width="100%" color="blue lighten-4">
            <v-card-text>
              <p class="title">Task List</p>
                <span v-for="(entry, idx) in entries" :key="`entry${idx}`">
                  <v-textarea auto-grow rows="1" clearable autofocus
                              class="mb-2" outlined hide-details v-model="entries[idx]"
                              @change="textChangedHandler()"
                  ></v-textarea>
                </span>
              <v-btn :disabled="taskLimitReached" color="primary" @click="addNewCard()">+ Add another card</v-btn>
            </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Home',

    data: () => ({
      entries: []
    }),
    computed: {
      taskLimitReached() {
        return this.entries.length >= 10
      }
    },
    methods: {
      addNewCard() {
        this.entries.push('')
      },
      textChangedHandler() {
        const config = { headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}}
        this.$axios.post('/api/tasks/', this.entries, config)
          .then(
              resp => {
                console.log(`${resp}`)
              }
          )
      }
    },
    created() {
      this.$axios.get('/api/tasks')
        .then(
          resp => {
            this.entries = resp.data
          }
        )
        .catch(
          error => {
            console.log(`Something went wrong in /api/tasks ${error}`)
          }
        )
    }
  }
</script>
