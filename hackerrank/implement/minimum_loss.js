// Lauren has a chart of distinct projected prices for a house over the next  years, where the price of the house in the  year is . She wants to purchase and resell the house at a minimal loss according to the following rules:
//
// The house cannot be sold at a price greater than or equal to the price it was purchased at (i.e., it must be resold at a loss).
// The house cannot be resold within the same year it was purchased.
// Find and print the minimum amount of money Lauren must lose if she buys the house and resells it within the next years.
//
// Note: It's guaranteed that a valid answer exists.

function solve(price){
    // Complete this function
    let best = price[0] || 999;
    price.forEach((p1, i1) => price.slice(i1+1).forEach((p2, i2) => {
      if (p1 > p2) {
        const x = p1 - p2;
        if (x < best) best = x;
        if (best == 1) return;
      }
    }));
    return best;
}
console.log(solve([1]))
// console.log([1,2,3,4].slice(1));
