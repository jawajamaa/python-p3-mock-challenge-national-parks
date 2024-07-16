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
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >= 3:
            self._name = name
        else:
            raise ValueError ("Name must be a string three or more characters in length")  
        
    def trips(self):
        if isinstance(self, NationalPark):
            return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        if isinstance(self, NationalPark):
            return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        pass
    # from chatGPT
    # from collections import Counter
    # visitors = [trip.visitor for trip in self.trips()]
    # if visitors:
        # return Counter(visitors).most_common(1)[0][0]
    # return None

class Trip:
    all = list()

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise ValueError("Start date must be a string with 7 or more characters")

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise ValueError("End date must be a string with 7 or more characters")

    def __repr__(self):
        return f"Traveler {self.visitor} visited {self.national_park} from {self.start_date} to {self.end_date}"

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <=len(name) <=15:
            self._name = name
        else:
            raise ValueError ("Name must be a string between one and 15 characters in length")

    def __repr__(self):
        return f"Explorer {self.name}"
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])
