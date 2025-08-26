class myClass:

    __privateVar = 27;

    def privMeth(self):
        print("I'm inside my class")

    def hello(self):
        print("Private Variable value: ",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.privMeth() 