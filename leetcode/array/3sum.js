/**
 * @param {number[]} nums
 * @return {number[][]}
 */
let indexs = []
let tmp = []
let res = []
var tryWith = function(i, nums) {
    for (let index in nums) {
      if (indexs[index] !== true) {
          if (i == 2) {
            if(tmp[0] + tmp[1] + nums[index] == 0) {
              res.push([...tmp, nums[index]]);
              indexs[index] = true;
              tryWith(i - 1, nums);
            } else {
              indexs[index] = false;
              tryWith(i - 1, nums);
            }
          }
          else {
              tmp[i] = nums[index];
              indexs[index] = true;
              tryWith(i + 1, nums);
          }
      }
    }
};

var threeSum = function(nums) {
   tryWith(0, nums);
   return res;
};
