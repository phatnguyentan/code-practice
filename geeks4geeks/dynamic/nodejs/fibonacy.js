// Dynamic Programing Tabulation
// function fib(n) {
//   if(n < 2) return 1;
//   let f = [1, 1];
//   for(let i = 2; i <= n; i++) {
//     f[i] = f[i - 1] + f[i -2]
//   }
//   return f[n];
// }

function fib(n) {
  if (n < 2) return 1;
  return fib(n - 1) + fib(n - 2);
}

console.log(fib(0));
console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(4));
console.log(fib(5));
console.log(fib(6));
