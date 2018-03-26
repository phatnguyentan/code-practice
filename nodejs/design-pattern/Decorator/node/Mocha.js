const CondimentDecorator = require('./CondimentDecorator');

class Mocha extends CondimentDecorator {
  constructor(beverage) {
    super();
    this.beverage = beverage;
  }

  getDescription() {
    return this.beverage.getDescription() + ", Mocha";
  }

  cost() {
    return 0.20 + this.beverage.cost();
  }
}

module.exports = Mocha;
