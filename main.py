#1-misol
age = int(input("Yoshingizni kiriting: "))

if age >= 18:
    print("Kattasiz")
else:
    print("Kattasiz emas")

# 2-misol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if a > b:
    print("Birinchi son katta")
elif b > a:
    print("Ikkinchi son katta")
else:
    print("Sonlar teng")

# 3-misol
n = float(input("Son kiriting: "))

if n > 0:
    print("Musbat son")
elif n < 0:
    print("Manfiy son")
else:
    print("0 ga teng")

# 4-misol
if n < 10:
    print("10 dan kichik")
elif n == 10:
    print("10 ga teng")
else:
    print("10 dan katta")

# 5-misol
a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))

if a == b:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")

# 6-misol
s = input("So'z kiriting: ").lower()

if s == "hello":
    print("Salom!")
elif s == "bye":
    print("Xayr!")
else:
    print("Noma'lum so'z")
