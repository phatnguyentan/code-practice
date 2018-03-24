const { take, map, delay, mergeAll } = require('rxjs/operators')
const { of } = require('rxjs/observable/of')
const { merge } = require('rxjs/observable/merge')
const { interval } = require('rxjs/observable/interval')

const myPromise = val =>
  new Promise(resolve => setTimeout(() => resolve(`Result: ${val}`), 2000));
//emit 1,2,3
const source = of(1, 2, 3);

const example = source.pipe(
  //map each value to promise
  map(val => myPromise(val)),
  //emit result from source
  mergeAll()
);

const subscribe = example.subscribe(val => console.log(val));
