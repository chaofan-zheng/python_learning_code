a = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 0, 1], [
         1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
     [1, 1, 0, 1, 0, 1, 0, 1, 0, 1], [
         1, 0, '%', 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Solution:
    def __init__(self, a):
        self.a = a
        self.res = set()

    def find_exit(self, i, j):
        if i - 1 < 0 or j - 1 < 0 or i + 1 > len(self.a)-1 or j + 1 > len(self.a[0])-1:
            self.fres = self.res
            return self.fres
        self.judge(i - 1, j)
        self.judge(i + 1, j)
        self.judge(i, j - 1)
        self.judge(i, j + 1)

    def judge(self, i, j):
        if self.a[i][j] == 0:
            if (i, j) in self.res:
                pass
            else:
                self.res.add((i, j))
                self.find_exit(i, j)
                return
        # self.res = set()

    def find_start(self):
        for i in range(len(self.a) - 1):
            for j in range(len(self.a[i]) - 1):
                if a[i][j] == '%':
                    return i, j


s = Solution(a)
i, j = s.find_start()
print(i, j)
fres = s.find_exit(i, j)
print(fres)
fres =s.fres
print(fres)
