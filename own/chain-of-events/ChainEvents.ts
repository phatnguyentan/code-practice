export class ChainEvents {
  events: any = [];
  pointer: any = 0;
  total: any = 0;
  addEvents(...events: any[]) {
    this.events = [...this.events, ...events];
    this.total = this.events.length;
  }

  start() {
    this.events[this.pointer].init();
  }

  next() {
    this.pointer = this.pointer + 1;
    if (this.events[this.pointer]) {
      this.events[this.pointer].init();
    }
  }

  back() {
    this.pointer = this.pointer - 1;
    if (this.events[this.pointer]) {
      this.events[this.pointer].init();
    }
  }
}
