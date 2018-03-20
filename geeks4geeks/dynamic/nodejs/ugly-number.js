// function findUgly(index) {
//   let count = 1;
//   if (index == 1) return 1;
//   let number = 1;
//   while (count < index) {
//     number += 1;
//     let no = number;
//     no = divide(no, 2);
//     no = divide(no, 3);
//     no = divide(no, 5);
//     if (no == 1) {
//       count += 1;
//     }
//   }
//   return number;
// }
// function divide(a, b) {
//   while (a % b == 0) a = a / b;
//   return a;
// }
function findUgly(index) {
  let count = 1;
  if (index == 1) return 1;
  let number = 1;
  while (count < index) {
    number += 1;
    let no = number;
    no = divide(no, 2);
    no = divide(no, 3);
    no = divide(no, 5);
    if (no == 1) {
      count += 1;
    }
  }
  return number;
}
function divide(a, b) {
  while (a % b == 0) a = a / b;
  return a;
}
console.log(findUgly(7));
console.log(findUgly(150));
