"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""


class Name():
    def __init__(self, name):
        self.name = name

    def pr_name(self):
        print(self.name, 'гений')


class Misery(Name):
    def but(self):
        super().pr_name()
        print('Но его не  отчислят, так как он выучил ООП')


nme = Misery('Егор')
nme.but()
