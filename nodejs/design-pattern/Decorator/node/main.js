// import Espresso from './Espresso';
// import Mocha from './Mocha';
// import Whip from './Whip';
const Espresso = require('./Espresso');
const Mocha = require('./Mocha');
const Whip = require('./Whip');

let oEspressoWithMochaAndWhip = new Espresso();
oEspressoWithMochaAndWhip = new Mocha(oEspressoWithMochaAndWhip);
oEspressoWithMochaAndWhip = new Whip(oEspressoWithMochaAndWhip);

console.log(oEspressoWithMochaAndWhip.cost());
