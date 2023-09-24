export const state = () => ({
  products: null,
  initialProducts: null,
  isTopProductsLoaded: false,
  isProductsLoaded: false
})

export const actions = {
  getProduct({commit, state}) {
    if (!state.isProductsLoaded) {
      this.$axios.get('https://dev.aromatic.kz/api/v1/products/baseList')
        .then(res => {
          commit('SET_PRODUCTS', res.data.items);
        });
    }
  },
  updatedProduct({commit}, {index, isCheckedCart}) {
    commit('UPDATED_PRODUCT', {index, isCheckedCart})
  },
  searchProducts({ commit, state }, searchTerm) {
    const searchTerms = searchTerm.toLowerCase().split(' ');

    const filteredProducts = state.initialProducts.filter(product => {
      return searchTerms.every(term => {
        return (
          product.title.toLowerCase().includes(term)
        );
      });
    });

    commit('SEARCH_PRODUCTS', filteredProducts);
  },
}

export const mutations = {
  UPDATED_PRODUCT(state, {index, isCheckedCart}) {
    state.products[index].inCart = isCheckedCart
  },
  SET_PRODUCTS(state, payload) {
    const newPayload = payload.map(item => ({...item, inCart: false}))
    state.initialProducts = newPayload
    state.products = newPayload
    state.isProductsLoaded = true
    state.isTopProductsLoaded = true
  },
  UPDATE_PRODUCT_IN_CART(state, { id, inCart }) {
    const product = state.products.find(product => product.id === id);
    if (product) {
      product.inCart = inCart;
    }
  },
  SEARCH_PRODUCTS(state, payload) {
    state.products = payload;
  },
  ASCENDING_AND_DESCENDING_PRODUCTS(state, {data, payload}) {
    const sortedProducts = [...state.products];

    if(data === 'возрастание') {
      sortedProducts.sort((a, b) => a.price - b.price);
    } else {
      sortedProducts.sort((a, b) => b.price - a.price);
    }

    state.products = sortedProducts;
  },
  POPULAR_PRODUCTS(state) {
    const popular = state.products.filter(product => product.is_top);

    const newProductsArray = [...popular, ...state.products.filter(product => !product.is_top)];

    state.products = newProductsArray;
  },
  RESET_PRODUCTS(state) {
    state.products = state.initialProducts
  },

}

export const getters = {
  topProducts: state => {
    if (state.isTopProductsLoaded) {
      return state.products.filter(product => product.is_top === true);
    } else {
      return [];
    }
  },
  Products: state => state.products,
}

