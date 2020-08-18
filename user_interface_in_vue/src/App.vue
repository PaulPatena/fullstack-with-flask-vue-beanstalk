<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Trello Lite</v-toolbar-title>
      <v-spacer></v-spacer>
      <span class="mr-2">Aug 2020</span>
    </v-app-bar>

    <v-main class="contentBgColor">
      <transition name="fade-transition" mode="out-in">
        <keep-alive>
          <router-view/>
        </keep-alive>
      </transition>
    </v-main>
  </v-app>
</template>

<script>


export default {
  name: 'App',
  data: () => ({
    //
  }),
};
</script>

<style>
.contentBgColor {
  background-color: rgb(211, 230, 255);
}
</style>