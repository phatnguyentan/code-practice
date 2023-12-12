// Complete the unboundedKnapsack function below.
function unboundedKnapsack(k, arr) {
  let max = knapsack(k, arr, 0, 0);
  return max;
}

function knapsack(k, arr, max, tempMax) {
  for (let i = 0; i < arr.length; i++) {
    if (tempMax + arr[i] <= k) {
      tempMax = tempMax + arr[i];
      console.log(max, tempMax, arr[i]);
      
      if (max < tempMax) {
        max = tempMax;
      }
      if (tempMax == k) {
        return k;
      }
      max = knapsack(k, arr, max, tempMax);
      tempMax = tempMax - arr[i];
    }
  }
  return max;
}


// const k = 12;
// const arr = [1, 6,9];

const k = 11;
const arr = [3,4,8];

unboundedKnapsack(k, arr);
