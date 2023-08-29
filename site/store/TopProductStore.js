export const state = () => ({
  topProducts: null
})

export const actions = {
  getTopProduct({commit}) {
    this.$axios.get('http://87.249.50.115:8000/api/v1/products/topList')
      .then(res => commit('SET_TOP_PRODUCT', res.data))
  }
}

export const mutations = {
  SET_TOP_PRODUCT(state, payload) {
    state.topProducts = payload
  }
}

export const getters = {
}
