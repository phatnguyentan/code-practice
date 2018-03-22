const { map, concatAll } = require('rxjs/operators')
const { of } = require('rxjs/observable/of')
const { interval } = require('rxjs/observable/interval')

//emit a value every 2 seconds
const source = interval(1000);
const example = source.pipe(
  //for demonstration, add 10 to and return as observable
  map(val => of(val + 10)),
  //merge values from inner observable
  concatAll()
);
//output: 'Example with Basic Observable 10', 'Example with Basic Observable 11'...
const subscribe = source.subscribe(val =>
  console.log('Example with Basic Observable:', val)
);
