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
              <p class="title">Title</p>
                <span v-for="(entry, idx) in entries" :key="`entry${idx}`">
                  <v-textarea class="mb-2" outlined hide-details v-model="entries[idx]"></v-textarea>
                </span>
              <v-btn color="primary" @click="addNewCard()">+ Add another card</v-btn>
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
    methods: {
      addNewCard() {
        this.entries.push('')
      }
    }
  }
</script>
