import main

class SomeClass:
    """
    This is just some class...
    """
    def __init__(self):
        """
        The constructor. Not very special...
        """
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass

    def print_something(self):
        """
        This class just prints some random text!
        :return:
        """
        print("Some random txt")

    def iterator(self):
        for i in range(0, 10):
            print(i)

    def call_main(self):
        main.Output().print("normal", "Successfully loaded the data", f"It took {99} sec.")

