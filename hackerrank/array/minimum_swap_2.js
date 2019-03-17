Array.prototype.swap = function(x, y) {
  var b = this[x];
  this[x] = this[y];
  this[y] = b;
  return this;
};
function minimumSwaps(arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    while (arr[i] != i + 1) {
      count++;
      const tmp = arr[i];
      [arr[i], arr[tmp - 1]] = [arr[tmp - 1], arr[i]];
    }
  }
  return count;
}
console.log(minimumSwaps([4, 3, 1, 2]));
