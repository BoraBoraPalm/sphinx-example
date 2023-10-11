import sys
import time
import somemodule
from typeguard import typechecked
#import typeguard import typechecked
#from typeguard import install_import_hook
#install_import_hook('main')


class TestClass:
    """
    This class was just created for testing various things ;)
    """

    def __int__(self):
        """
        Constructor comment ;)
        :param self: object variable.
        :return: nothing
        """
        raise NotImplementedError  # implement instead of "pass"

    def __call__(self):
        """
        With __call__ instances behave like functions and can be called like a function.
        :return: A nice message.
        """
        print(f"Using the fancy __call__ method ;) of {self.__class__}\n")

    @typechecked
    def test_method(self, a: str, b: int, c: float) -> int:
        """
        This method is just for testing purposes. Otherwise, it would be complete nonsense ;)

        :param a: insert a desired string.
        :param b: insert a desired integer.
        :param c: insert a desired floating number.
        :return: just 1!!
        """
        print(f"This function returns just {1}", file=sys.stdout)
        return 1


class TestClass2:
    """
    This class implemented the call method with positional and keyword arguments. The purpose is just as a dummy class.
    """
    def __call__(self, *args, **kwargs):
        """
        :param args: just positional arguments...
        :param params: just keyword arguments...
        :return: nothing
        """
        a, b, c = kwargs.get("a", "default_a"), kwargs.get("b", "default_b"), kwargs.get("c", "default_c")
        print(f"Printing the keyword arguments: {a},{b},{c}")
        print(f"Printing the positional arguments: {args}")


class Output:
    """
    For creating standardised console output.
    """
    i = 0

    @staticmethod
    @typechecked
    def print(type_of_message: str = "normal", *args):
        """
        For printing the desired message formatted to the console.

        :param type_of_message: it can be either "normal" or "error" so far. The default is "normal".
        :type type_of_message: str
        :param args: Messages which the use would like to print to the console.
        :return: nothing
        """
        Output.i += 1

        match type_of_message:
            case "normal":
                target = sys.stdout
            case "error":
                target = sys.stderr
            case _:
                target = sys.stdout

        current_time = time.strftime("%H:%M", time.localtime())

        print(f"[ {Output.i: ^5} ] [ {current_time: ^5} ] [ {type_of_message: ^15} ] >>> Message: {args}", file=target)


if __name__ == "__main__":
    testClass = TestClass()
    testClass.test_method("some string", 1, 1.0)
    testClass()  # __call__

    testClass2 = TestClass2()
    testClass2(2, 5, 1, 4, a="one", b="two", c="three")

    # output = Output()
    # output.print(23)
    Output().print("normal", "Successfully loaded the data", f"It took {10} sec.")
    Output().print("normal", "Successfully loaded the data", f"It took {2} sec.")
    Output().print("normal", "Successfully loaded the data", f"It took {8} sec.")
    Output().print("normal", "Successfully loaded the data", f"It took {300} sec.")
    Output().print("error", "Could not load file", "The file might not be available.")
    """
    The code above creates the console output:
    [   1   ] [ 11:24 ] [     normal      ] >>> Message: ('Successfully loaded the data', 'It took 10 sec.')
    [   2   ] [ 11:24 ] [     normal      ] >>> Message: ('Successfully loaded the data', 'It took 2 sec.')
    [   3   ] [ 11:24 ] [     normal      ] >>> Message: ('Successfully loaded the data', 'It took 8 sec.')
    [   4   ] [ 11:24 ] [     normal      ] >>> Message: ('Successfully loaded the data', 'It took 300 sec.')
    and...
    [   5   ] [ 11:24 ] [      error      ] >>> Message: ('Could not load file', 'The file might not be available.')
    ...being not in order, because it is an error message.
    """

    # From the other module
    sm = somemodule.SomeClass()
    sm.print_something()
    sm.call_main()
    sm.iterator()
