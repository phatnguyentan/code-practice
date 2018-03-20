function sum(arr) {
  let max = 0;
  let maxHere = 0;
  arr.forEach(item => {
    maxHere += item;
    if (max < maxHere) max = maxHere;
    if (maxHere < 0) maxHere = 0;
  })
  return max;
}

console.log(sum([-2, -3, -4, 1, -2, -1, -5, -3]));
