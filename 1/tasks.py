from typing import List


def make_ten(s: str) -> List[str]:
    flowers = [s for i in range(10)]
    return flowers


print(make_ten('роза'))
