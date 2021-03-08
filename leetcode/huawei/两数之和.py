"""
给出一个整数数组，请在数组中找出两个加起来等于目标值的数，
你给出的函数twoSum 需要返回这两个数字的下标（index1，index2），需要满足 index1 小于index2.。注意：下标是从1开始的
假设给出的数组中只存在唯一解
例如：
给出的数组为 {20, 70, 110, 150},目标值为90
输出 index1=1, index2=2
"""
class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]

class Solution2:
    def twoSum(self , numbers , target ):
        # write code here
        res = [0,0]#保存结果
        mp = {}#定义一个哈希表存储numbers[i]和对应的下标
        for i in range(len(numbers)):#进行标记
            mp[numbers[i]] = i
        for i in range(len(numbers)):
             #每遍历一个numbers[i]就去对应的mp里找有没有target - numbers[i]
             #如果有就返回结果
             #如果没有就找下一个
            if target - numbers[i] in mp:
                if mp[target - numbers[i]] != i:
                    res[0] = i + 1
                    res[1] = mp[target - numbers[i]]
                    return res
        return res