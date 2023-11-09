from Some_Folder.module1 import TestClass1
from Some_Folder.module2 import TestClass2

class TestClass3:
    def __init__(self):
        self.test_class_1 = None
        self.test_class_2 = None
        pass

    def interact_with_module_1(self):
        self.test_class_1 = TestClass1()

    def interact_with_module_2(self):
        self.test_class_2 = TestClass2()