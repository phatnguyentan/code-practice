
const { timer } = require('rxjs/observable/timer')
const { combineLatest } = require('rxjs/observable/combineLatest')
//timerOne emits first value at 1s, then once every 4s
const timerOne = timer(1000, 1000);
//timerTwo emits first value at 2s, then once every 4s
const timerTwo = timer(2000, 2500);

const combined = combineLatest(timerOne, timerTwo);

const subscribe = combined.subscribe(
  ([timerValOne, timerValTwo]) => {
    console.log(
      `Timer 1 Latest: ${timerValOne},
       Timer 2 Latest: ${timerValTwo}`
    );
  }
);
