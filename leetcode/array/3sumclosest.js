// For example, given array S = {-1 2 1 -4}, and target = 1.
// The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
let best = 9999;
let bestChoices = [];
let choices = [];
let index = [];
let current = 0;
const threeSumClosest = function(nums, target) {
  tryWith(0, nums, target);
};
const tryWith = function(i, nums, target) {
  for(let j in nums) {
    if(index[j] !== true) {
      current += nums[j];
      choices[i] = nums[j];
      index[j] = true;
      if (i == 2) {
        if (Math.abs(current - target) < best) {
          best = Math.abs(current - target);
          bestChoices = [...choices];
        }
        current -= nums[j];
        tryWith(i-1, nums, target);
      } else {
        tryWith(i+1, nums, target);
      }
    }
  }
}
// threeSumClosest([-1,2,1,-4], 1)
threeSumClosest([0,0,0], 1)
console.log(bestChoices);
