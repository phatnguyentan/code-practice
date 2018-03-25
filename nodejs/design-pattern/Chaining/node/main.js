
const Chainable = require('./Chainable')

const chain = new Chainable(0);
console.log(chain.add(2).add(3).output());
// console.log(chainable.add(3).add(4).multiply(3));
