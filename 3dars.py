# 1-savol
# def Hello():
#     print("Salom, dunyo!")
# Hello()
    


# 2-savol
# def Ism():
#     a = input()
#     print(f"Salom,[{a}]!")
# Ism()



# 3-savol
# def Yigindi():
#     a, b = map(int, input().split())
#     s = a + b
#     print(s)
# Yigindi()



# 4-savol
# def Kvadrat():
#     a = int(input("son: "))
#     s = a ** 2
#     print(s)
# Kvadrat()



# 5-savol
# def Orta(a, b, c):
#     s = a + b + c
#     l = s / 3
#     return l

# a, b, c = map(int, input().split())
# print(Orta(a, b, c))



# 6-savol
# def Juft(a:int):
#     if a % 2 == 0:
#         s = "Juft"
#     else:
#         s = "Toq"
#     return s

# a = int(input("son: "))
# print(Juft(a))



# 7-savol
# def Katta(a, b, c):
#     maxx = max(a, b, c)
#     return maxx
# a, b, c = map(int, input().split())
# print(Katta(a, b, c))



# 8-savol
# def Palindrom(soz:str):
#     if soz == soz[::-1]:
#         a = "Palindrom"
#     else:
#         a = "Palindrom emas"
#     return a
# soz = input("soz: ")
# print(Palindrom(soz))



# 9-savol
# def Son(son:int):
#     if son == 0:
#         a = "nol"
#     elif son > 0:
#         a = "musbat"
#     else:
#         a = "manfiy"
#     return a
# son = int(input("son: "))
# print(Son(son))



# 10-savol
# def Kabisa(a:int):
#     if a % 4 == 0 or a % 400 == 0:
#         s = "kabisa yili"
#     else:
#         s = "kabisa yili emas"
#     return s
# a = int(input("son: "))
# print(Kabisa(a))



# 11-savol
s = 0
def Unli(soz:str):
    for i in soz:
        if "a" "o" "i" "e" in i:
            s += 1
        return s
soz = input("soz: ")
print(Unli(soz))