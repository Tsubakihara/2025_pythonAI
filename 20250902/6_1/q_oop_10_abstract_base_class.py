# ---------------------------------------------
# 問題10: 抽象基底クラスを使って派生クラスに実装を強制せよ
# 実行方法: python q_oop_10_abstract_base_class.py
# ---------------------------------------------

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        XXXXXXXXXXXX

class Dog(Animal):
    def speak(self):
        return "Bark!"

d = Dog()
print(d.XXXXXXXXXXXX())  # speak