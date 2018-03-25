class Chainable {
  constructor() {
    this.number = 0;
  }

  add(n) {
    this.number += n;
    return this;
  }

  output() {
    return this.number;
  }
}
module.exports = Chainable;
