import random


class Die:
    def __init__(self, face: int = None,  sides=6):
        self.sides = sides
        # Face is added for testing as extra parameter, if face is not None then __face = face
        if face is not None:
            self.__face = face
        else:
            # Here roll is a method because we assume that a die will always have a value.
            self.roll()

        def roll(self):
            self.__face = random.randint(1, self.sides)
            return self.__face

        def set_face(self, value):
            self.__face = value

        def get_face(self):
            return self.__face

        def __str__(self):
            return str(self.__face)
