# 扑克牌的顺子

'''
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''


class Solution:

    def IsContinuous(self, numbers):

        # 转化扑克牌为数字
        if numbers == None or len(numbers) <= 0:
            return False
        tran = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in tran.keys():
                numbers[i] = tran[numbers[i]]

        # 统计0个数
        numberof0 = 0
        for i in range(len(numbers)):
            if numbers[i] == 0:
                numberof0 += 1
            else:
                continue
        if numberof0 >= len(numbers)-1:
            return True

        # 统计间隔个数
        numberofempty = 0
        numbers.sort()
        for i in range(numberof0, len(numbers)-1):
            nextid = i + 1
            if numbers[nextid] == numbers[i]:
                return False
            else:
                numberofempty += (numbers[nextid]-numbers[i]-1)

        # 判断是否顺子
        if numberofempty == numberof0:
            return True
        else:
            return False


test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
test3 = [3, 0, 0, 0, 0]
s = Solution()
print(s.IsContinuous(test3))