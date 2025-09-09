# ファイル名: abc02.py
# ヒント: レポート生成機能。抽象基底クラスで各フォーマットを共通化。

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def XXXXXXXXXXX(self, data):  # generate メソッドを抽象化
        pass

class PDFReport(ReportGenerator):
    def generate(self, data):
        return f"PDF Report: {data}"

class CSVReport(ReportGenerator):
    def generate(self, data):
        return f"CSV Report: {','.join(data)}"

# ダックタイピングで利用
def export_report(generator, data):
    return generator.XXXXXXXXXXX(data)

print(export_report(PDFReport(), "Project Status OK"))
print(export_report(CSVReport(), ["Task1", "Task2"]))
