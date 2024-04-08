# National park -> Trips <- Visitors
# Trips belong to a park and a visitor

class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str:
            if len(value) >= 3:
                if not hasattr(self, 'name'):
                    self._name = value
                else:
                    print("Name has already been defined")
            else:
                raise ValueError("Name must be greater than 3 characters")
        else:
            raise ValueError("Name must be of type string")

    name = property(get_name, set_name)

    def trips(self):
        returnList = list()
        for trip in Trip.all:
            if trip.national_park is self:
                returnList.append(trip)
        return returnList

    def visitors(self):
        returnList = set()
        for trip in Trip.all:
            if trip.national_park is self:
                returnList.add(trip.visitor)
        return list(returnList)

    def total_visits(self):
        returnList = 0
        for trip in Trip.all:
            if trip.national_park is self:
                returnList += 1
        return returnList

    def best_visitor(self):
        maxAmt = 0
        maxVisitor = None
        for visitor in Visitor.all:
            temp = 0
            for trip in Trip.all:
                if trip.visitor is visitor and trip.national_park is self:
                    temp += 1
            if temp > maxAmt:
                maxAmt = temp
                maxVisitor = visitor

        print(maxVisitor)
        return maxVisitor


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, value):
        if type(value) is Visitor:
            self._visitor = value
        else:
            raise ValueError("Visitor must be of type visitor")

    visitor = property(get_visitor, set_visitor)

    def get_park(self):
        return self._national_park

    def set_park(self, value):
        if type(value) is NationalPark:
            self._national_park = value
        else:
            raise ValueError("National park must be of type NationalPark")

    national_park = property(get_park, set_park)

    def get_start(self):
        return self._start_date

    def set_start(self, value):
        if type(value) is str:
            if len(value) >= 7:
                self._start_date = value
            else:
                print("Start date much be greater than 7 characters")
        else:
            print("Start date must be of type string")

    start_date = property(get_start, set_start)

    def get_end(self):
        return self._end_date

    def set_end(self, value):
        if type(value) is str:
            if len(value) >= 7:
                self._end_date = value
            else:
                print("End date much be greater than 7 characters")
        else:
            print("End date must be of type string")

    end_date = property(get_end, set_end)


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str:
            if 15 >= len(value) >= 1:
                self._name = value
            else:
                print("Name must be greater than 1 characters, but less than 15")
        else:
            print("Name must be of type string")

    name = property(get_name, set_name)

    def trips(self):
        returnList = list()
        for trip in Trip.all:
            if trip.visitor is self:
                returnList.append(trip)
        return returnList

    def national_parks(self):
        returnList = set()
        for trip in Trip.all:
            if trip.visitor is self:
                returnList.add(trip.national_park)
        return list(returnList)

    def total_visits_at_park(self, park):
        returnList = 0
        for trip in Trip.all:
            if trip.national_park is park and trip.visitor is self:
                print("+1")
                returnList += 1
        print(returnList)
        return returnList


acadia = NationalPark("Acadia National Park")
rocky = NationalPark("Rocky mountain")
jackson = Visitor("jackson")
sam = Visitor("sam")
trip1 = Trip(jackson, acadia, "October 7th", "march 14th")
trip2 = Trip(jackson, acadia, "October 7th", "march 14th")
trip3 = Trip(jackson, acadia, "October 7th", "march 14th")
trip4 = Trip(sam, acadia, "October 7th", "march 14th")
trip5 = Trip(sam, acadia, "October 7th", "march 14th")
trip6 = Trip(sam, acadia, "October 7th", "march 14th")
trip7 = Trip(sam, acadia, "October 7th", "march 14th")
trip8 = Trip(sam, acadia, "October 7th", "march 14th")
trip9 = Trip(sam, rocky, "October 7th", "march 14th")
trip10 = Trip(sam, rocky, "October 7th", "march 14th")

sam.total_visits_at_park(acadia)
