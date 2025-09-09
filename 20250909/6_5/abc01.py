# ファイル名: abc01.py
# ヒント: 抽象基底クラスを使って共通のインターフェースを強制する(DBリポジトリ)

from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def XXXXXXXXXXX(self, data):  # save メソッドを抽象化
        pass

    @abstractmethod
    def XXXXXXXXXXX(self, id):  # find メソッドを抽象化
        pass

class UserRepository(Repository):
    def save(self, data):
        print(f"Saving user: {data}")

    def find(self, id):
        return {"id": id, "name": "Alice"}

repo = UserRepository()
repo.save({"id": 1, "name": "Alice"})
print(repo.find(1))
