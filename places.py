class places:
    def __init__(self, data):
        self.places_name = []
        self.data = data

    def init_place(self):
        place_name = self.data['장소 이름'].values
        for name in place_name:
            self.add_place(name)

    def add_place(self, name):
        self.places_name.append(name)

    def get_places(self):
        return self.places_name