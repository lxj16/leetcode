// Plus One

// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

// The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

// You may assume the integer does not contain any leading zero, except the number 0 itself.

// Example 1:

// Input: [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Example 2:

// Input: [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.

//Dumb trial
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let lastDigit = digits.pop();
    if (digits === []) return digits;
    if (lastDigit === 9 ){
        const digitsExceptLast = plusOne(digits);
        return digitsExceptLast.push(0)
    }else{
        digits.push(lastDigit+1);
    }
    return digits;
};

//==Solution==
var plusOne2 = function(digits) {
    for(var i = digits.length - 1; i >= 0; i--){
      if(++digits[i] > 9) digits[i] = 0; //already plus one
      else return digits;
    }
    digits.unshift(1);
    return digits;
  };