class Profil():
    def __init__(self, name, surname, age, pasport):
        self.name = name
        self.surname = surname
        self.age = age
        self.pasport = pasport

    def print_info(self):
        print(self.name, self.surname, self.age, self.pasport)


class Adress():
    def __init__(self, city, street, M_index):
        self.city = city
        self.street = street
        self.M_index = M_index


class Rol():
    def __init__(self, rol, workH):
        self.rol = rol
        self.workH = workH


class Bankaccount():
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance


class Order():
    def __init__(self, price, items, delivery, date):
        self.date = date
        self.price = price
        self.item = items
        self.delivery = delivery


class Add_user():
    def __init__(self, name, surname, age, pasport):
        self.name = name
        self.surname = surname
        self.age = age
        self.pasport = pasport
        self.order = []
        self.bankAccount = []
        self.role = []
        self.addres = []

    def add_Acount(self, name, surname, age, pasport):
        self.profile = Profil(name, surname, age, pasport)

    def add_role(self, rol, workH):
        self.role.append(Rol(rol, workH))

    def add_bankAccount(self, card_number, balance):
        self.bankAccount.append(Bankaccount(card_number, balance))

    def add_Adress(self, city, street, M_index):
        self.addres.append(Adress(city, street, M_index))

    def add_order(self, price, items, delivery, date):
        self.order.append(Order(price, items, delivery, date))
