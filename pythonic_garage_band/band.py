class Band:
    band_list = []

    def __int__(self, name, members, play_solos):
        self.band_name = name
        self.members = members
        self.play_solos = play_solos

    @classmethod
    def to_list(cls):
        pass


class Musician:

    def play_solo(self):
        return ""

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Guitarist(Musician):
    def __str__(self):
        print(f'My name is {Musician.name} Jett and I play guitar')


class Bassist(Musician):
    def __str__(self):
        pass

    def __repr__(self):
        pass


class Drummer(Musician):
    def __str__(self):
        pass

    def __repr__(self):
        pass
