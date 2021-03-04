import re


class Solution:
    res_dict = {}

    def solution(self, input_str):
        # 把输入处理成行
        lines = input_str.split('\n')
        for line in lines:
            if self.is_full(Solution.res_dict):
                break
            # 得到文件名和行数
            path = line.split(' ')[0]
            row = line.split(' ')[1]
            filename = re.findall('.*\\\(.*?)$', path)[0]
            # 结果字典
            key = filename + ' ' + row
            count = Solution.res_dict.get(key)
            if count:
                Solution.res_dict[key] += 1
            else:
                Solution.res_dict[key] = 1
            # 输出结果
        for key, value in Solution.res_dict.items():
            yield key + ' ' + str(value)

    def is_full(self, res_dict):
        """判断结果字典是否已经为8"""
        count = 0
        for key in res_dict:
            count += 1
        if count < 8:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    input_str = r"""e:\1\aa3.txt 3
e:\3\aa1.txt 2"""
    res = s.solution(input_str)
    for item in res:
        print(item)
