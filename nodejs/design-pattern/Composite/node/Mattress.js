class Mattress {
  constructor(aMenus) {
    this.menus = aMenus;
  }

  printMenu() {
    this.menus.print();
  }
}

module.exports = Mattress;
