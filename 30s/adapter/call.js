// ctx = [1, 2, 3]
const call = (keyFunc, ...args) => ctx => ctx[keyFunc](...args);

Promise.resolve([1, 2, 3])
  .then(call('map', x => 2 * x))
  .then(console.log); //[ 2, 4, 6 ]
