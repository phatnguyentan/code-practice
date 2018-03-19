// Given 3 numbers {1, 3, 5}, we need to tell
// the total number of ways we can form a number 'N'
// using the sum of the given three numbers.
// 1) Adding 1 to all possible combinations of state (n = 6)
// Eg : [ (1+1+1+1+1+1) + 1]
// [ (1+1+1+3) + 1]
// [ (1+1+3+1) + 1]
// [ (1+3+1+1) + 1]
// [ (3+1+1+1) + 1]
// [ (3+3) + 1]
// [ (1+5) + 1]
// [ (5+1) + 1]
// 2) Adding 3 to all possible combinations of state (n = 4);
// Eg : [(1+1+1+1) + 3]
// [(1+3) + 3]
// [(3+1) + 3]
// 3) Adding 5 to all possible combinations of state(n = 2)
// Eg : [ (1+1) + 5]



// Dynamic Programing Memoizatation
// let numbers = [1, 3, 5];
// let result = [];
// function state(n) {
//     if (n < 0) return 0;
//     if (n == 1) return 1;
//     if (result[n]) return result[n];
//     result[n] = numbers.reduce((acc, curr, i) => acc + state(n - numbers[i]), 0);
//     return result[n];
// }

let numbers = [1,3, 5];
let result = [];
function state(n) {
  if (n < 0) return 0;
  if (n == 1) return 1;
  if (result[n]) return result[n];
  result[n] = numbers.reduce((acc, curr, i) => acc + state(n - curr), 0)
  return result[n];
}
console.log(state(7));
