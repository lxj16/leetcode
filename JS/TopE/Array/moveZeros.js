// Move Zeroes

// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Example:

// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Note:

// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.

// ====== My dumb solution ======
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    for (let i=0; i<nums.length; i++){
        if (nums[i] === 0){
            nums.splice(i,1);
            nums.push(0);
        }
    }
};

//solution
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes2 = function(nums) {
    let index = 0;
    for (let i=0; i<nums.length; i++){
        if (nums[i] !== 0){
            nums[index] = nums[i];
            index++;
        }
    }
    for (let i=index; i<nums.length; i++){
        nums[i] = 0;
    }
};