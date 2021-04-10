// RxJS v6+
import { take, concatAll, map } from 'rxjs/operators';
import { interval, of } from 'rxjs';

const obs1 = interval(1000).pipe(take(5), map(val => 'obs1'));
const obs2 = interval(500).pipe(take(2), map(val => 'obs2'));
const obs3 = interval(2000).pipe(take(1), map(val => 'obs3'));
//emit three observables
const source = of(obs1, obs2, obs3);
//subscribe to each inner observable in order when previous completes
const example = source.pipe(concatAll());

const subscribe = example.subscribe(val => console.log(val));
