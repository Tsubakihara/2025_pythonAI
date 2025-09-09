# ファイル名: abc03.py
# ヒント: ダック・タイピングで外部サービスを扱う(抽象基底クラスは使わず、共通メソッドさえあればOK)

class SlackNotifier:
    def send(self, message):
        print(f"[Slack] {message}")

class EmailNotifier:
    def send(self, message):
        print(f"[Email] {message}")

# ダックタイピング: send メソッドがあればOK
def notify_all(notifiers, message):
    for n in notifiers:
        n.XXXXXXXXXXX(message)

services = [SlackNotifier(), EmailNotifier()]
notify_all(services, "System is running normally.")
