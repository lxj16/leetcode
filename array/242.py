# Share
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

#Tracker
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         tracker = collections.defaultdict(int)
#         for x in s: tracker[x] += 1
#         for x in t: tracker[x] -= 1
#         return all(x == 0 for x in tracker.values())

#sort
# def isAnagram1(self, s, t):
#     dic1, dic2 = {}, {}
#     for item in s:
#         dic1[item] = dic1.get(item, 0) + 1
#     for item in t:
#         dic2[item] = dic2.get(item, 0) + 1
#     return dic1 == dic2
    
# def isAnagram2(self, s, t):
#     dic1, dic2 = [0]*26, [0]*26
#     for item in s:
#         dic1[ord(item)-ord('a')] += 1
#     for item in t:
#         dic2[ord(item)-ord('a')] += 1
#     return dic1 == dic2
    
# def isAnagram3(self, s, t):
#     return sorted(s) == sorted(t)

def isAnagram(self, s, t):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True