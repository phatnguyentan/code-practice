export class SelectConversation {
  chain: any;

  constructor(chain: any) {
    this.chain = chain;
  }

  init() {
    setTimeout(() => {
      console.log("SelectConversation");
      this.chain.next();
    }, 2000);
  }
}
