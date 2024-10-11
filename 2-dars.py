mehmonlar = ['rasul', 'temur', 'bexruz', 'ergash']
for mehmon in mehmonlar:
    print(f'hurmatli {mehmon}, sizni 31-dekabr kuni yangi yil kechasiga taklif qilamiz')
print('xurmat bilan, ramanovlar oilasi')

sonlar = list(range(11,100,2))
print(sonlar)
for son in sonlar:
    print(f'{son} ning qubi {son**3} ga teng')

dostlar = []
print('5 ta eng sevimli kinolaringiz qaysi ?')
for n in range(5):
    dostlar.append(input(f'{n+1}-kinolarning nomini  kiriting: '))
print(dostlar)