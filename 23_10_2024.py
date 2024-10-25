class avto:
    """Avto nomli klass yaratamiz"""

    def __init__(self, model, rang, karobka, narx):
        """Talabaning xususiyatlari"""
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.kilometr = 0
    def get_info(self):
        return f"modeli-{self.model}. rangi-{self.rang}. karobka-{self.karobka}. narxi-{self.narx}. probeg-{self.kilometr} "
    def set_kilometr(self,kilometr):
        """Talabaning kursini yangilovchi metod"""
        self.kilometr = kilometr
avto1 = avto("malibu","qora","avto",35000)
print(avto1.get_info())
