import time

class FizzBuzz:
    
    def __init__(self, _range, fizzCondition, buzzCondition):
        self.range = _range
        self.fizzPartialCondition = fizzCondition
        self.buzzPartialCondition = buzzCondition
    
    def fizzCondition(self, number):
        return self.fizzPartialCondition(number) and \
                not self.buzzPartialCondition(number)
    
    def buzzCondition(self, number):
        return self.buzzPartialCondition(number) and \
                not self.fizzPartialCondition(number)
    
    def fizzbuzzCondition(self, number):
        return self.fizzPartialCondition(number) and \
                self.buzzPartialCondition(number)

    def play(self):
        for number in self.range:
            if self.fizzCondition(number):
                print('Fizz')
            elif self.buzzCondition(number):
                print('Buzz')
            elif self.fizzbuzzCondition(number):
                print('FizzBuzz')
            else:
                print(number)

def isDivisibleByThree(number):
    return number % 3 == 0

def isDivisibleByFive(number):
    return number % 5 == 0

tik = time.perf_counter()
aTest = FizzBuzz(range(0,101), isDivisibleByThree, isDivisibleByFive)
aTest.play()
tok = time.perf_counter()
print(tok-tik)



