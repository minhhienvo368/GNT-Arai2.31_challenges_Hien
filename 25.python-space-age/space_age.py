#in space_age file create SpaceAge function

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        pass

    def seconds_to_years(self):
        return self.seconds / (60 * 60 * 24 * 365.25)  # Calculate seconds to years

    def calc_years(self, earth_years):
        return self.seconds_to_years() / earth_years  # Base

    def on_earth(self):
        years = self.seconds_to_years()
        return round(years, 2)

    def on_mercury(self):
        years = self.calc_years(0.2408467)
        return round(years, 2)

    def on_venus(self):
        years = self.calc_years(0.61519726)
        return round(years, 2)

    def on_mars(self):
        years = self.calc_years(1.8808158)
        return round(years, 2)

    def on_jupiter(self):
        years = self.calc_years(11.862615)
        return round(years, 2)

    def on_saturn(self):
        years = self.calc_years(29.447498)
        return round(years, 2)

    def on_uranus(self):
        years = self.calc_years(84.016846)
        return round(years, 2)

    def on_neptune(self):
        years = self.calc_years(164.79132)
        return round(years, 2)

age = SpaceAge(8210123456)
age_on_Earth = age.on_earth()
age_on_Neptune = age.on_neptune()
print(age_on_Earth)
print(age_on_Neptune)
