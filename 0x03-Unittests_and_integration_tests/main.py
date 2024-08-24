from  utils import memoize

class MyClass:
    @memoize
    def a_method(self):
        print("a_method")
        return 42
mymethod = MyClass()
mymethod.a_method
print(mymethod.a_method)