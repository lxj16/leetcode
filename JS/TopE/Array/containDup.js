// Contains Duplicate

// Solution
// Given an array of integers, find if the array contains any duplicates.

// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:

// Input: [1,2,3,1]
// Output: true
// Example 2:

// Input: [1,2,3,4]
// Output: false
// Example 3:

// Input: [1,1,1,3,3,4,3,2,4,2]
// Output: true

//========My dumb solution=========
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let checked = [];
    if (nums.length === 1) return false;
    for (let i=0; i < nums.length; i++){
        if (checked.indexOf(nums[i]) !== -1){
            return true;
        }else{
            checked.push(nums[i])
        }
    }
    return false;
};

//===obj===
var containsDuplicate2 = function(nums) {
    var obj = {};
    
    for(let i = 0; i < nums.length; i++){
        obj[nums[i]] = obj[nums[i]] + 1 || 1;
        
        if(obj[nums[i]] > 1) return true;
    }
    
    return false;
};
