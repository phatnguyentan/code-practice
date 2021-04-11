// RxJS v6+
import { interval } from 'rxjs';
import { take } from 'rxjs/operators';

//emit value in sequence every 1 second
const source = interval(1000).pipe(take(2));
//output: 0,1,2,3,4,5....
const subscribe = source.subscribe(val => console.log(val));
