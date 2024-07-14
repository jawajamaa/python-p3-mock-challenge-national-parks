class NationalPark:

    all_park = []

    def __init__(self, name):
        self.name = name
        type(self).all_park.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, name):
            self._name = name
        else:
            raise Exception as exc:
