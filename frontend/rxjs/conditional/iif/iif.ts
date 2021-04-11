// RxJS v6+
import { iif, of, interval } from 'rxjs';
import { mergeMap, take } from 'rxjs/operators';

const r$ = of('R');
const x$ = of('X');

interval(1000)
  .pipe(take(6), mergeMap(v => iif(() => v % 4 === 0, r$, x$)))
  .subscribe(console.log);

// output: R, X, X, X, R, X, X, X, etc...
