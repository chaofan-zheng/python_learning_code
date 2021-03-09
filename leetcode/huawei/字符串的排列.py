"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
示例1
输入
"ab"
返回值
["ab","ba"]
"""


class Solution:
    res = []

    def Permutation(self, string):
        self.recure(string)
        set1 = set(self.res)
        return list(set1)

    def recure(self, string):
        if len(string) == 1:
            return string
        for i in range(len(string) - 1):
            str_list = list(string)
            del str_list[i]
            str_next = ''.join(str_list)
            print(str_next)
            str = string[i] + self.recure(str_next)
            self.res.append(str)
str='abc'
s = Solution()
res = s.Permutation(str)
print(res)

"""
class Solution {
public:
    void perm(int pos, string s, set<string> &ret) {
        if (pos+1 == s.length()) {
            ret.insert(s);
            return;
        }
        // for循环和swap的含义：对于“ABC”，
        // 第一次'A' 与 'A'交换，字符串为"ABC", pos为0， 相当于固定'A'
        // 第二次'A' 与 'B'交换，字符串为"BAC", pos为0， 相当于固定'B'
        // 第三次'A' 与 'C'交换，字符串为"CBA", pos为0， 相当于固定'C'
        for (int i = pos; i < s.length(); ++i) {
            swap(s[pos], s[i]);
            perm(pos+1, s, ret);
            swap(s[pos], s[i]);
            // 回溯的原因：比如第二次交换后是"BAC"，需要回溯到"ABC"
            // 然后进行第三次交换，才能得到"CBA"
        }
    }
    vector<string> Permutation(string s) {
        if (s.empty()) return {};
        set<string> ret;
        perm(0, s, ret);
        return vector<string>({ret.begin(), ret.end()});
    }
};"""