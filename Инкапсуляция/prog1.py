"""
настройка классического банковского аккаунта по аналогии с показом. Сделать имя атрибута защищенным, а
баланс и паспорт приватными.
Добавьте геттер-методы на паспорт и баланс. Сделайте смену номера на паспорт поролю. Изменение баланса
на отклонение суммы(сумма не может пасть меньше 0, так что выполните проверку).
настроить метод удаления данных паспорта аккаунта (также по поролю).
"""
class Account():
    def __init__(self, balanse, pasport, name, pasworld):
        self._name = name
        self.__balanse = balanse
        self.__pasport = pasport
        self.__pasworld = pasworld
    def getbalance(self):
        print(self.__balanse)
    def getpasport(self):
        a = input('Введите пароль для смены паспорта')
        if a == self.__pasworld:
            print(self.__pasport)
    def setpasport(self):
        a = input('Введите пароль: ')
        if a == self.__pasworld:
            a = input('Введите новые паспротные данные: ')
            self.__pasport = a
        else:
            print('Неправильынй пароль')
    def setbalance(self, newbalance):
        if newbalance < 0:
            print('Нельзя установить отрицательный баланс')
        else:
            print('Деньги успешно начислены')
            self.__balanse += newbalance
    def delpasport(self):
        a = input('Введите пароль: ')
        if a == self.__pasworld:
            del self.__pasport
        else:
            print('Неверный пароль ')
