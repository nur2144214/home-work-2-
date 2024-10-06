class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def say_hero_name(self):
        print(f"hero name : {self.name}")

    def double_health(self):
        self.health_points = int(self.health_points) * 2
        return
    def __str__(self):
        return f'nickname : {self.nickname}, superpower : {self.superpower}, health : {self.health_points}'


piter = SuperHero('Peter', 'spider man', 'strength', '300', "I'm your friendly neighbor")

piter.say_hero_name()
piter.double_health()
print(piter)