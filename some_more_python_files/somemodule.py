import main

class SomeClass:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass

    def print_something(self):
        print("Some random txt")

    def iterator(self):
        for i in range(0, 10):
            print(i)

    def call_main(self):
        main.Output().print("normal", "Successfully loaded the data", f"It took {99} sec.")

