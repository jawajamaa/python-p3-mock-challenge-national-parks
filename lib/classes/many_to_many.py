class NationalPark:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"National Park: {self.name}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(self, str) and not hasattr(self, "name") and 1 <=len(name) <=15:
            self._name = name
        else:
            raise ValueError ("Name must be a string between one and 15 characters in length")  
        
    def trips(self):
        if isinstance(self, NationalPark):
            return [trip for trip in Trip.all if Trip.name == self]
    
    def visitors(self):
        if isinstance(self, NationalPark):
            return [trip for trip in Trip.all if trip.national_park == self.name]
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass

class Trip:
    all = list()
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    def __repr__(self):
        return f"Traveler {self.visitor} visited {self.national_park} from {self.start_date} to {self.end_date}"

class Visitor:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Explorer {self.name}"
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass
