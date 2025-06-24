"""
【問題６】
以下のコードでは、素数を求める問題で、関数の処理時間を計測するためのデコレータ `timer` が定義されています。
このデコレータを用いて、指定された個数の素数を生成する `generate_primes` 関数の実行時間を測定しています。

次の問いに答えなさい。

【設問1】  
`@timer` という記法が `generate_primes` 関数に対してどのような効果を持つか？  
次のうち最も適切なものを1つ選びなさい。

1. `generate_primes` 関数が実行される前後に処理時間の計測を行い、実行時間を表示するようになる。  
2. `generate_primes` 関数のコードを自動で最適化し、処理を高速化する。  
3. `generate_primes` 関数の戻り値を必ず `None` にする。  
4. `generate_primes` 関数の引数を自動でキャッシュし、同じ引数の呼び出しを省略する。

【設問2】  
`generate_primes(100_000)` を実行した際に表示されるものとして最も適切なものはどれか？

1. 素数のリストと、処理時間が表示される。  
2. 処理時間だけが表示され、戻り値は表示されない。  
3. 何も表示されない。  
4. エラーが発生し処理が停止する。

【設問3】  
もし `timer` デコレータ内の `return wrapper` を `return func` に変更した場合、どうなるか？

1. 実行時間の計測・表示が行われなくなる。  
2. 元の関数が2回実行される。  
3. 関数が呼ばれた際に必ずエラーになる。  
4. 処理時間の計測は行われるが、結果は返されない。

"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"処理時間: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

generate_primes(100_000)
