const { take, map, combineAll, concat, debounce } = require('rxjs/operators')
const { interval } = require('rxjs/observable/interval')
const { timer } = require('rxjs/observable/timer')
const { Observable } = require('rxjs/Observable')

const loginEvent = interval(1000).pipe(take(1));

const callApi = Observable.create(function(observer) {
  observer.next('Call Api');
});

const store = Observable.create(function(observer) {
  observer.next('Store Api');
});

const hello = Observable.create(function(observer) {
  observer.next('Hello');
  observer.next('World');
  observer.next('World2');
}).pipe(debounce(() => timer(1000)));

//output: 'Hello'...'World'
const subscribe = hello.subscribe(val => console.log(val));
//
// const example = concat(callApi, store);
// example.subscribe(val => console.log(val));

// loginEvent.subscribe(val => example.subscribe(message => console.log(message)));
