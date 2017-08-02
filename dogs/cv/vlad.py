import dogs.cv.bow.Bow as Bow


class VLAD():
    def __init__(self, dict_path="./dict", dict_size=64):
        self.dict_path = dict_path

        self.bow = Bow()

        
