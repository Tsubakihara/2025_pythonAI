# ---------------------------------------------
# 問題5: プロパティを使ってgetterを定義せよ
# 実行方法: python q_oop_05_property_decorator.py
# ---------------------------------------------

# ヒント: @property を使うとメソッドを属性のように使える

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * XXXXXXXXXXXX

r = Rectangle(4, 5)
print(r.XXXXXXXXXXXX)  # areaを属性のように呼び出し
