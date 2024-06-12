class Band:
    def __init__(self, name, hometown):
        # The __init__ method initializes a new Band object with the given name and hometown.
        # It checks if the name and hometown are valid non-empty strings, and raises a ValueError if not.
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise ValueError("Hometown must be a non-empty string")

        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        # The name property returns the name of the band.
        return self._name

    @name.setter
    def name(self, value):
        # The name setter method allows you to change the name of the band.
        # It checks if the new name is a valid non-empty string, and raises a ValueError if not.
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        # The hometown property returns the hometown of the band.
        return self._hometown

    def concerts(self):
        # The concerts method returns a list of all the concerts the band has played.
        return self._concerts

    def play_in_venue(self, venue, date):
        # The play_in_venue method creates a new Concert object with the given venue and date,
        # and adds it to the band's list of concerts and the venue's list of concerts.
        concert = Concert(date=date, band=self, venue=venue)
        return concert

    def venues(self):
        # The venues method returns a list of all the venues the band has played at.
        return list(set(concert.venue for concert in self._concerts))

    def all_introductions(self):
        # The all_introductions method returns a list of all the introductions the band has
        # given at their concerts.
        return [concert.introduction() for concert in self._concerts]

class Concert:
    all = []

    def __init__(self, date, band, venue):
        # The __init__ method initializes a new Concert object with the given date, band, and venue.
        # It checks if the date is a valid non-empty string, and if the band and venue are of the
        # correct types, and raises a ValueError if not.
        if not isinstance(date, str) or len(date) == 0:
            raise ValueError("Date must be a non-empty string")
        if not isinstance(band, Band):
            raise ValueError("Band must be of type Band")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")

        self._date = date
        self._band = band
        self._venue = venue

        band._concerts.append(self)
        venue._concerts.append(self)
        Concert.all.append(self)

    @property
    def date(self):
        # The date property returns the date of the concert.
        return self._date

    @date.setter
    def date(self, value):
        # The date setter method allows you to change the date of the concert.
        # It checks if the new date is a valid non-empty string, and raises a ValueError if not.
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Date must be a non-empty string")
        self._date = value

    @property
    def band(self):
        # The band property returns the band that played the concert.
        return self._band

    @band.setter
    def band(self, value):
        # The band setter method allows you to change the band that played the concert.
        # It checks if the new band is of type Band, and raises a ValueError if not.
        if not isinstance(value, Band):
            raise ValueError("Band must be of type Band")
        self._band = value

    @property
    def venue(self):
        # The venue property returns the venue where the concert was held.
        return self._venue

    @venue.setter
    def venue(self, value):
        # The venue setter method allows you to change the venue where the concert was held.
        # It checks if the new venue is of type Venue, and raises a ValueError if not.
        if not isinstance(value, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = value

    def hometown_show(self):
        # The hometown_show method returns True if the concert was held in the band's hometown,
        # and False otherwise.
        return self._band.hometown == self._venue.city

    def introduction(self):
        # The introduction method returns the introduction the band gave at the concert.
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"

class Venue:
    def __init__(self, name, city):
        # The __init__ method initializes a new Venue object with the given name and city.
        # It checks if the name and city are valid non-empty strings, and raises a ValueError if not.
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(city, str) or len(city) == 0:
            raise ValueError("City must be a non-empty string")

        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        # The name property returns the name of the venue.
        return self._name

    @name.setter
    def name(self, value):
        # The name setter method allows you to change the name of the venue.
        # It checks if the new name is a valid non-empty string, and raises a ValueError if not.
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        # The city property returns the city where the venue is located.
        return self._city

    @city.setter
    def city(self, value):
        # The city setter method allows you to change the city where the venue is located.
        # It checks if the new city is a valid non-empty string, and raises a ValueError if not.
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("City must be a non-empty string")
        self._city = value

    def concerts(self):
        # The concerts method returns a list of all the concerts that have been held at the venue.
        return self._concerts

    def bands(self):
        # The bands method returns a list of all the bands that have played at the venue.
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        # The concert_on method returns the concert that was held at the venue on the given date,
        # or None if no concert was held on that date.
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
