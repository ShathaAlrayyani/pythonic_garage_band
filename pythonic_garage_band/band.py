
class Musician:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def play_solo():
        return f''

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Band:
    band_list = []

    def __int__(self, name, members):
        # super().__init__(name)
        self.name = name
        self.members = members

        # self.band_name = band

    def play_solos(self):
        pass

    @classmethod
    def to_list(cls):
        pass


class Guitarist(Musician):
    def __int__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "guitar"

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

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


if __name__ == "__main__":
    pass
