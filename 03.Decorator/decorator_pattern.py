import abc


class Beverage(abc.ABC):
    """Abstract class to represent a base for beverages"""
    @abc.abstractmethod
    def cost(self):
        """Calculates and returns the cost of the beverage"""
        pass

    def get_description(self):
        """Returns the description of the beverage"""
        return self.__description

    def set_description(self, d):
        """Set the description of the beverage"""
        self.__description = d


class CondimentDecorator(Beverage):
    """Represents a decorator for a beverage"""
    @abc.abstractmethod
    def get_description(self):
        pass


class Espresso(Beverage):
    """Represents an espresso coffee"""
    def __init__(self):
        self.__description = "Espresso"

    def cost(self):
        return 1.99

    def get_description(self):
        return self.__description


class Mocha(CondimentDecorator):
    """Represents a mocha addon for a beverage"""
    def __init__(self, beverage):
        self.__description = "Mocha"
        self.__beverage = beverage

    def cost(self):
        return self.__beverage.cost() + 0.20

    def get_description(self):
        return self.__beverage.get_description() + ", Mocha"


if __name__ == "__main__":
    print("* Creating an Espresso..")
    beverage = Espresso()
    print(f"Espresso price is: ${beverage.cost()}")
    print(f"Espresso description is: {beverage.get_description()}")

    print("\n* Wrapping the espresso with a Mocha object..")
    beverage = Mocha(beverage)
    print(f"Espresso with Mocha price is: ${beverage.cost()}")
    print(f"Espresso with Mocha description is: {beverage.get_description()}")

    print("\n* Wrapping the espresso with another Mocha object..")
    beverage = Mocha(beverage)
    print(f"Espresso with two Mochas price is: ${beverage.cost()}")
    print(f"Espresso with two Mochas description is: "
          f"{beverage.get_description()}")
