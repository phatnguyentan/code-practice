{
  // const chunk = (arr, num) => {
  //   let tmp = [];
  //   let newArr;
  //   while(arr.length > 0) {
  //     newArr = arr.slice(0, num);
  //     arr = arr.slice(num, arr.length)
  //     tmp.push(newArr);
  //   }
  //   return tmp;
  // }
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
