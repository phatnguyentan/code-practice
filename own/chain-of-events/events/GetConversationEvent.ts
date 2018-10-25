export class GetConversationEvent {
  chain: any;

  constructor(chain: any) {
    this.chain = chain;
  }

  init() {
    setTimeout(() => {
      console.log("GetConversationEvent");
      this.chain.next();
    }, 2000);
  }
}
