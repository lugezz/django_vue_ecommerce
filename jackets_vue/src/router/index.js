import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/HomeView.vue'

import ProductView from '../views/ProductView.vue'
import CategoryView from '../views/CategoryView.vue'
import Search from '../views/SearchView.vue'
import Cart from '../views/CartView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/about',
    name: 'AboutView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/search',
    name: 'SearchView',
    component: Search
  },
  {
    path: '/cart',
    name: 'CartView',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'SuccessView',
    component: Success
  },
  {
    path: '/cart/checkout',
    name: 'CheckoutView',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/:product_slug',
    name: 'ProductView',
    component: ProductView
  },
  {
    path: '/category/:category_slug',
    name: 'CategoryView',
    component: CategoryView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } })
  } else {
    next()
  }
})

export default router
