const { pairwise, take } = require('rxjs/operators')
const { of } = require('rxjs/observable/of')
const { merge } = require('rxjs/observable/merge')
const { interval } = require('rxjs/observable/interval')

//Returns: [0,1], [1,2], [2,3], [3,4], [4,5]
interval(1000)
  .pipe(pairwise(), take(5))
  .subscribe(console.log);
