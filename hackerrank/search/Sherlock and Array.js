function solve(a){
    // Complete this function
    let flag = "NO";
    const sum = a.reduce((a, b) => a + b, 0);
    let left = 0;
     a.forEach((num, i) => {
       const right = sum - left - num;
       if (right < left) return;
       if (right == left) {flag = "YES"; return;}
       left += num;
    });
    return flag;
}
console.log(solve([1]))
