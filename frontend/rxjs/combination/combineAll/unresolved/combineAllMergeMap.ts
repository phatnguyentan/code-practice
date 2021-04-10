import { interval, of } from "rxjs";
import { combineAll, map, mergeMap, take } from "rxjs/operators";

const source = of("a", "b", "c");
// source.pipe(
//     mergeMap(val => interval(1000).pipe(map(i => "source " + val + " i " + i),take(4)))
// ).pipe(combineAll()).subscribe(console.log);
source.pipe(
    mergeMap(val => interval(1000).pipe(map(i => "source " + val + " i " + i),take(4)))
).subscribe(console.log);