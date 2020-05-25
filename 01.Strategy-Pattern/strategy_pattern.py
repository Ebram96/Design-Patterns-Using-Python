import abc


class FlyBehavior(abc.ABC):
    """Represents flying behavior of a Duck object"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "fly") and
                callable(subclass.fly) or
                NotImplemented)

    @abc.abstractmethod
    def fly(self):
        """Defines how a Duck object should fly"""
        pass


class FlyWithWings(FlyBehavior):
    """Defines the mechanism for a Duck that can fly with wings"""
    def fly(self):
        """The actual flying behavior"""
        print("Flying with my wings..!")
        return True


class FlyNoFly(FlyBehavior):
    """Defines the mechanism for a Duck that can not fly"""
    def fly(self):
        """The actual flying behavior"""
        print("I can not fly..!")
        return True


class Duck(abc.ABC):
    """Represents a base class for Ducks"""
    def __init__(self, fb):
        """Initialize a Duck object"""
        self.fly_behavior = fb

    @abc.abstractmethod
    def display(self):
        """Display the type of a Duck"""
        pass

    def set_fly_behavior(self, fb):
        """Change the Duck object fly behavior"""
        self.fly_behavior = fb

    def perform_fly(self):
        """Perform the flying mechanism"""
        self.fly_behavior.fly()


class MallardDuck(Duck):
    """Represents a Mallard Duck"""
    def display(self):
        """Display the type of the duck as Mallard duck"""
        print("I'm a Mallard Duck!")


if __name__ == "__main__":
    print("* Creating a new mallard duck with wings..")
    duck = MallardDuck(fb=FlyWithWings())
    duck.display()

    print("* Performing the fly..")
    duck.perform_fly()
    print("----------------------------------------")

    print("* Changing the fly behavior..")
    duck.set_fly_behavior(fb=FlyNoFly())
    print("* Performing the fly after changing fly behavior..")
    duck.perform_fly()

    print("----------------------------------------")
    print("* Cool and simple design pattern!")
