# ---------------------------------------------
# 問題6: サブクラスでメソッドをオーバーライドせよ
# 実行方法: python q_oop_06_method_override.py
# ---------------------------------------------

class Shape:
    def draw(self):
        return "Drawing shape"

class Circle(Shape):
    def draw(self):
        return XXXXXXXXXXXX

s = Shape()
c = Circle()

print(s.draw())   # Drawing shape
print(c.XXXXXXXXXXXX())  # Circle固有の出力
