// RxJS v6+
import { map, concatAll, take } from 'rxjs/operators';
import { of, interval } from 'rxjs';

//emit a value every 2 seconds
const source = interval(1000).pipe(take(10));
const example = source.pipe(
  //for demonstration, add 10 to and return as observable
  map(val => of(val, 2, 3)),
  //merge values from inner observable
  concatAll()
);
//output: 
const subscribe = example.subscribe(val =>
  console.log('Ex:', val)
);