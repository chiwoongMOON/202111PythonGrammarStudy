﻿# circle_simple2.py

from circle import ar_circle as ac
from circle import ci_circle as cc


def ar_circle(rad):     # 원의 넓이를 출력
    print("넓이: ", rad * rad * 3.14) 


def ci_circle(rad):     # 원의 둘레를 출력
    print("둘레: ", rad * 2 * 3.14)

def main():
    r = float(input("반지름 입력: "))
    ar_circle(r)
    ci_circle(r)

    sum = ac(r) + cc(r)
    print("넓이와 둘레의 합: ", sum)

main()
