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
    def __str__(self):
        return(f'name: {self.name}\n'
               f'nickname: {self.nickname}\n'
               f'superpower: {self.superpower}\n'
               f'health_points: {self.health_points}\n'
               f'catchphrase: {self.catchphrase}')
hero = SuperHero("Cristiano Ronaldo", "CR7", "Goal Machine", 100, "I'm the best")
print(hero.sound_name())
print(hero.double_hp())
print(hero.full_hero())
