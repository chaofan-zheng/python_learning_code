"""
统计文件中每个文件中单词的数量
"""
from mrjob.job import MRJob


class WordCount(MRJob):
    # 重写mapper和reducer方法
    # def mapper(self, key, value):
    def mapper(self, _, line):
        # 参数key：每行行首的偏移量
        # 参数value：一行的内容
        # mapper的执行次数由文本的行数决定。
        # 文件有几行，mapper被调用几次。每次执行的时候，把行首的偏移量、行首的的文本内容传给key(_)，value(line)
        # 一行的内容通常写作line
        for word in line.split():
            yield word, 1
    # shuffle and sort 这个过程我们看不见，由MapReduce自己实现
    # little 1
    # twink  1 1
    # you    1

    def reducer(self, word, occurence):
        # key是shuffle sort之后的哪些key（上面的单词），values shuffle之后的序列（上面的1 / 11 ）
        yield word,sum(occurence)


if __name__ == '__main__':
    WordCount.run()
