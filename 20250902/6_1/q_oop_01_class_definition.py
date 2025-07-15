# ---------------------------------------------
# 問題1: クラスを定義し、属性とメソッドを設定せよ
# 実行方法: python q_oop_01_class_definition.py
# ---------------------------------------------

# ヒント: __init__ はコンストラクタで、selfを通じて属性を操作します

class Car:
    def __init__(self, brand, model):
        self.brand = XXXXXXXXXXXX
        self.model = XXXXXXXXXXXX

    def info(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.XXXXXXXXXXXX())  # infoメソッドを呼び出す
