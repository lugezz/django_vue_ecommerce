<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Jackets!</strong>
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="toggleMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" :class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-ligth">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <i class="fas fa-shopping-cart"></i>
                </span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section>
      <router-view/>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';

</style>

<script>

export default {
  components: {},
  data () {
    return {
      showMobileMenu: false
    }
  },
  methods: {
    toggleMobileMenu () {
      this.showMobileMenu = !this.showMobileMenu
    }
  }
}
</script>
