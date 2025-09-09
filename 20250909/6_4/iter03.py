# ファイル名: iter03.py
# ヒント: 数値リストから偶数だけを返すイテレータを作ろう（フィルタリング処理）

class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def XXXXXXXXXXX(self):  # __iter__
        return self

    def XXXXXXXXXXX(self):  # __next__
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration

nums = [1, 2, 3, 4, 5, 6]
it = EvenIterator(nums)

for n in it:
    print(n)
# 期待値: 2, 4, 6
