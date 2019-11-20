"""
反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = [i for i in s]
        i,j=0,len(s)-1
        check_list = "aeiou"
        while(i<j):
            if result[i].lower() not in check_list:
                i+=1
                continue
            if result[j].lower() not in check_list:
                j-=1
                continue
            result[i],result[j]=result[j],result[i]
            i+=1
            j-=1
        return "".join(result)