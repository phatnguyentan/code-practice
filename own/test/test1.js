var add = (...arr) => {
  if (arr.length > 1) {
    return arr.reduce((acc, curr) => {
      acc += curr;
      return acc;
    })
  } else {
    return (number) => {
      return number + arr[0];
    }
  }
}

console.log((add(2, 5)));
console.log((add(2)(5)));