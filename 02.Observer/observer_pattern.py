import abc


class Observable(abc.ABC):
    """An observable (subject) interface"""
    @classmethod
    def __subclasshook__(cls, subclass):
        """Check whether a class implements this interface"""
        interface_methods = ["add_observer", "remove_observer",
                             "notify_observers"]
        for method in interface_methods:
            if not (hasattr(subclass, method) and
                    callable(eval("subclass." + method))):
                return False

        return True

    @abc.abstractmethod
    def add_observer(self, observer):
        """Add/Subscribe an observer to the current observable"""
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        """Remove/Unsubscribe an observer from the current observable"""
        pass

    @abc.abstractmethod
    def notify_observers(self):
        """Notify the observers with the new state"""
        pass


class Observer(abc.ABC):
    """An observer interface"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "update") and
                callable(subclass.update))

    @abc.abstractmethod
    def update(self):
        """Update the observer with the new state"""
        pass


class DisplayElement(abc.ABC):
    """Interface to ensure an observer can display state"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "display") and
                callable(subclass.display))

    @abc.abstractmethod
    def display(self):
        """Display the current weather state"""
        pass


class WeatherData(Observable):
    """The weather station"""

    def __init__(self):
        self.__observers = set()
        self.__changed = False
        # temperature, humidity and pressure are just initialized with 0.
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0

    def get_temperature(self):
        """Returns the current temperature"""
        return self.__temperature

    def get_humidity(self):
        """Returns the current humidity"""
        return self.__humidity

    def get_pressure(self):
        """Returns the current pressure"""
        return self.__pressure

    def add_observer(self, observer):
        self.__observers.add(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        if self.__changed:
            for observer in self.__observers:
                observer.update()

            self.__changed = False

    def __set_changed(self):
        self.__changed = True

    def __measurements_changed(self):
        self.__set_changed()
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        """Set the weather data"""
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.__measurements_changed()


class GeneralDisplay(Observer, DisplayElement):
    """Represents a general display"""
    def __init__(self, observable):
        self.__observable = observable
        self.__observable.add_observer(self)
        # temperature, humidity and pressure are just initialized with 0 and
        # then they will get set by the update() call.
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0

        self.update()  # To set the current state

    def update(self):
        self.__temperature = self.__observable.get_temperature()
        self.__humidity = self.__observable.get_humidity()
        self.__pressure = self.__observable.get_pressure()

        self.display()

    def display(self):
        """Display the current state on the display."""
        print(f"Current conditions: {self.__temperature}F degrees, "
              f"{self.__humidity}% humidity, and {self.__pressure} pressure.")


if __name__ == "__main__":
    station = WeatherData()

    print("* Creating mobile display (observer)..")
    mobile_display = GeneralDisplay(station)

    print("\n* Changing measurements (in observable)..")
    station.set_measurements(temperature=14, humidity=8, pressure=80)

    print("\n* Creating digital display (observer)..")
    digital_display = GeneralDisplay(station)
