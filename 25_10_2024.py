class Shaxs:
    """Shaxslar Haqida Ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs xaqida ma'lumot"""
        info = f"{self.ism} {self.familiya}, "
        info += f"Passport seriyasi: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info

    def get_age(self, yil):
        return yil - self.tyil


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, email):
        super().__init__(ism, familiya, passport, tyil)
        self.email = email

    def get_info(self):
        info = super().get_info()
        info += f", Email: {self.email}"
        return info

class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, mahsulotlar):
        super().__init__(ism, familiya, passport, tyil)
        self.mahsulotlar = mahsulotlar

    def get_info(self):
        info = super().get_info()
        info += f", Mahsulotlar: {', '.join(self.mahsulotlar)}"
        return info

class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, xaridlar):
        super().__init__(ism, familiya, passport, tyil)
        self.xaridlar = xaridlar

    def get_info(self):
        info = super().get_info()
        info += f", Xaridlar: {', '.join(self.xaridlar)}"
        return info

    def ban_user(self):
        print("Foydalanuvchi bloklandi.")

mijoz = Mijoz("otkir", "sadullaev", "FA0548798", 1994, ["poyavzal"])
sotuvchi = Sotuvchi("xamit", "nuraddinov", "FA0212146", 2005, ["kiym-kechak"])
foydalanuvchi = Foydalanuvchi("ergash", "bekchanov", "FK6452165", 1989, "ergash@gmail.com")

print(foydalanuvchi.get_info())
print(sotuvchi.get_info())
print(mijoz.get_info())
