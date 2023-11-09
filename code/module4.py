class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car is starting.")
        self.engine.start()

    def stop(self):
        print("Car is stopping.")
        self.engine.stop()


my_car = Car()
my_car.start()
my_car.stop()