class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def sound_name(self):
        return(self.name)
    def double_hp(self):
        return(self.health_points * 2)
    def full_hero(self):
        return f"Имя героя: {self.name}, Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points} Фраза: {self.catchphrase}"

hero = SuperHero("Cristiano Ronaldo", "CR7", "Goal Machine", 100, "I'm the best")
print(hero.sound_name())
print(hero.double_hp())
print(hero.full_hero())
