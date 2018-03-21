// const ary = (fn, n) => (...args) => fn(...args.slice(0, n));

const ary = (func, n) => {
  return (...arr) => func(...arr.slice(0, n));
}

const firstTwoMax = ary(Math.max, 2);
let res = [[2, 6, 'a'], [8, 4, 6], [10]].map(x => firstTwoMax(...x)); // [6, 8, 10]
console.log(res);
