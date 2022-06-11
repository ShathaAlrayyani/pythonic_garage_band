class Musician:
    def __init__(self, name):
        self.name = name
        self.member = []

    @staticmethod
    def play_solo():
        return f''

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Guitarist(Musician):
    def __int__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


class Bassist(Musician):
    def __int__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):
    def __int__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


class Band(Guitarist, Drummer, Bassist):
    band_list = []
    instances = []

    def __init__(self, name, band):
        super().__init__(name)
        self.name = name
        self.members = band
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for i in self.members:
            solos.append(i.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


if __name__ == "__main__":
    pass
