// Two Sum

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:

// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

//first try-- failed [3,2,4]  target 6
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i=0; i<nums.length; i++){
        let targetNum = target - nums[i];
        if (nums.indexOf(targetNum) !== -1){
            return [i, nums.indexOf(targetNum)]
        }
    }
};
//2nd -good but slow
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum2= function(nums, target) {
    for (let i=0; i<nums.length; i++){
        let targetNum = target - nums[i];
        if (nums.indexOf(targetNum) !== -1 && nums.indexOf(targetNum) !== i){
            return [i, nums.indexOf(targetNum)]
        }
    }
    return null;
};

//Better solution using map
const twoSum3 = (nums, target) => {
    const map = {};
  
    for (let i = 0; i < nums.length; i++) {
      const another = target - nums[i];
  
      if (another in map) {
        return [map[another], i];
      }
  
      map[nums[i]] = i;
    }
  
    return null;
  };