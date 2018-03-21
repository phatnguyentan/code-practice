{
  const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
  // chunk([1, 2, 3, 4, 5], 2); // [[1,2],[3,4],[5]]
}

{
  // const compact = (arr) => arr.filter((i) => i != false && i)
  const compact = arr => arr.filter(Boolean);
  // compact([0, 1, false, 2, '', 3, 'a', 'e' * 23, NaN, 's', 34]); // [ 1, 2, 3, 'a', 's', 34 ]
}

{
  const countBy = (arr, f) => arr.map((i) => typeof f == 'function'? f(i): i[f]).reduce((acc, c) => {acc[c] = acc[c]? acc[c] + 1 : 1; return acc} , {})
  // console.log(countBy([6.1, 4.2, 6.3], Math.floor)); // {4: 1, 6: 2}
  // console.log(countBy(['test', 'test2', 'abcd'], 'length')); // {4: 1, 6: 2}
}

{
  const countOccurrences = (arr, v) => arr.reduce((acc, value) => value == v ? acc + 1 : acc, 0)
  // console.log(countOccurrences([1, 1, 2, 1, 2, 3], 1)); // 3
}

{
  const deepFlatten = (arr) => [].concat(...arr.map(a => Array.isArray(a)? deepFlatten(a) : a));
  // console.log(deepFlatten([1, [2], [[3], 4], 5])); // [1,2,3,4,5]
}

{
  const difference = (a,b) => {s = new Set(b); return a.filter(i => !s.has(i))};
  // console.log(difference([1, 2, 3], [1, 2, 4])); // [3]
}

{
  const differenceBy = (a, b, func) => {s = new Set(b.map(v => func(v))); return a.filter(i => !s.has(func(i)))}
  // console.log(differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], v => v.x)); // [ { x: 2 } ]
}
