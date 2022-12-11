"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
class Hero():
    def __init__(self, name, armor, health, power):
        self.name = name
        self.armor = armor
        self.power = power
        self.health = health
    def print_info(self):
        print('Уровень здоровья', self.health)
        print('Класс брони', self.armor, '\n')


class Magician(Hero):
    def Hello(self):
        print('Новый персонаж ->', self.name)
    def strike(self, enemy):
        print(self.name, 'Атакует ->', enemy.name)
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health -= enemy.armor
            enemy.armor = 0
        print('Вражеская броня ->', enemy.armor)
        print('Вражеское хп ->', enemy.health)

