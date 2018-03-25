const MenuComponent = require('./MenuComponent')

class MenuItem extends MenuComponent {
  print() {
    console.log(this.getName() + ": " + this.getDescription() + ", " + this.getPrice() + "euros");
  }
}

module.exports = MenuItem;
