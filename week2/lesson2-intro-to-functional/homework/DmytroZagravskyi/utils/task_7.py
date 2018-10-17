def makeRoman(i_int: int) -> str:
    if (i_int > 3999):
        return 'Can not convert the number greater than 3999'

    roman_dict = [
        {'int': 1000, 'roman': 'M'},
        {'int': 900, 'roman': 'CM'},
        {'int': 500, 'roman': 'D'},
        {'int': 400, 'roman': 'CD'},
        {'int': 100, 'roman': 'C'},
        {'int': 90, 'roman': 'XC'},
        {'int': 50, 'roman': 'L'},
        {'int': 40, 'roman': 'XL'},
        {'int': 10, 'roman': 'X'},
        {'int': 9, 'roman': 'IX'},
        {'int': 5, 'roman': 'V'},
        {'int': 4, 'roman': 'IV'},
        {'int': 1, 'roman': 'I'},
    ]

    r = ''
    while i_int > 0:
        ro = max(roman_dict, key=lambda i: i['int'] <= i_int)
        i_int = i_int - ro['int']
        r = r + ro['roman']
    return r
