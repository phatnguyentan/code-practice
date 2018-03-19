// import { take, map, combineAll } from 'rxjs/operators';
// import { interval } from 'rxjs/observable/interval';

const { take, map, combineAll } = require('rxjs/operators')
const { interval } = require('rxjs/observable/interval')

const source = interval(1000).pipe(take(2))

const example = source.pipe(
  map(val => interval(1000).pipe(map(i => `Result (${val}): ${i}`, take(5))))
)

const combined = example.pipe(combineAll());

// combined.subscribe(val => console.log(val))
source.subscribe(val => console.log(val))
example.subscribe(val => console.log(val))
