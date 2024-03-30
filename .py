import random

a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

b = int(input("şifrenin uzunluğu ?"))

sifre = ""
for i in range(b):
    sifre += random.choice(a)

print(sifre)

