// RxJS v6+
import { mapTo, merge, take } from 'rxjs/operators';
import { interval } from 'rxjs';

//emit every 2.5 seconds
const first = interval(2500).pipe(mapTo("Frist"), take(2));
//emit every 1 second
const second = interval(1000).pipe(mapTo("Second"), take(4));
//used as instance method
const example = first.pipe(merge(second));
//output: 0,1,0,2....
const subscribe = example.subscribe(val => console.log(val));