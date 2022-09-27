# def caoitalize(s):
#     res = s
    
#     # делаем заглавный первый не пробельный символ
#     pos = 0

#     while pos < len(s) and res[pos] == ' ':
#         pos = pos + 1

def kalk(a, b, c):
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    else:
        print(a // b)

kalk(2,2,"+")