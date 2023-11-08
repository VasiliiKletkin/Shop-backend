
export const products = {
  namespaced: true,
  state: {
    forSale: [],
    inCart: [],
  },
  
  getters: {
    forSale: state => state.forSale,
    inCart: state => state.inCart,
  },

  actions: {

  },

  mutations: {
    
  },
};
