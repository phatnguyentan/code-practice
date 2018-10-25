export class GetMessageEvent {
  chain: any;

  constructor(chain: any) {
    this.chain = chain;
  }

  init() {
    setTimeout(() => {
      console.log("GetMessageEvent");
      this.chain.next();
    }, 2000);
  }
}
