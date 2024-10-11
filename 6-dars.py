royxat = []

print("Buyurtma qabul qiluvchi dastur.")
n=1
while True:
    savol = f"{n}-maxsulotni nomini kiriting:"
    ism = input(savol)
    royxat.append(ism)
    javob = input("Yana maxsulot qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
print(royxat)

royxat = []

print("Buyurtma qabul qiluvchi dastur.")
n=1
while True:
    savol = f"{n}-maxsulotni nomini kiriting:"
    ism = input(savol)
    royxat.append(ism)
    javob = input("Yana maxsulot qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
print(royxat)

print("maxsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur.")
e_bozor = {}
ishora = True
while ishora:
    bozor = input("Maxsulotni nomini kiriting:")
    yosh = input(f"{bozor.title()}ning narxini kiriting:")
    e_bozor[bozor] = int(yosh)  # ism kalit, yosh qiymat

    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "no":
        ishora = False

for bozor, yosh in e_bozor.items():
    print(f"{bozor.title()}ning {yosh} narxi ")