import { interval, of } from "rxjs";
import { combineAll, map, take } from "rxjs/operators";

interval(500).pipe(take(2), map(e => of("Time: " + e))).pipe(combineAll()).subscribe(console.log);