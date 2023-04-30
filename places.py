class places:
    def __init__(self):
        self.places_name = []

    def add_place(self, name):
        self.places_name.append(name)

    def get_places(self):
        return self.places_name