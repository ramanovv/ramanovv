kitoblar = []
print("kitoblaringizni ro`yxatini tuzamiz")
n=1
while True:
    savol = f"{n}-yaxshi ko`rgan kitobingizni  kiriting: "
    kitob = input(savol)
    kitoblar.append(kitob)
    javob = input("yana kitob qo`shasizmi? (ha/yo`q)")
    if javob == 'ha':
        n+=1
        continue
    else:
        break
print("kitoblaringizni ro`yxati: ")
for kitob in kitoblar:
    print(kitob.title())