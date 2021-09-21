#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number -= 2*number
        return number
    else:
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    mots = []
    for letter in prefixes:
        mots.append(letter + suffixe)
    return mots


def prime_integer_summation() -> int:
    count = 0
    valid = 0
    for num in range(2, 101):
        for i in range (1,101):
            if num % i == 0:
                valid += 1
        if valid == 2:
            count += num
        valid = 0
    return count
            

def factorial(number: int) -> int:
    mul = 1
    for num in range (1, number):
        mul = mul + num * mul
    return mul


def use_continue() -> None:
    for i in range(1, 11):
        if i != 5:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    valid = True
    acceptance = []
    for group in groups:
        twofive = False
        fifty = False
        older_70 = False
        valid = True
        for person in group:
            if person < 18:
                valid = False
            if person > 70:
                older_70 = True
            if person == 25:
                twofive = True
            if person == 50:
                fifty = True
        if len(group) > 10 or len(group) <= 3:
            valid = False
        elif older_70 and fifty:
            valid = False
        if twofive:
            valid = True
        if valid:
            acceptance.append(True)
        else:
            acceptance.append(False)
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
