// import Beverage from './Beverage';
const Beverage = require('./Beverage');

class Espresso extends Beverage {
  cost() {
    return 1.99;
  }
}

module.exports = Espresso;
