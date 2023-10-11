import fire

def sayHello(name):
    print('Hello ' + name)
    
def sayGoodbye(name):
    print('Goodbye ' + name)
    
class Car:
    def __init__(self, color):
        self.color = color
    
    def create(self):
        print('create car with ' + self.color)
        
class Number:
    def __init__(self, value = 0):
        self.value = value
        print('init: ', self.value)
        
    def add(self, value):
        self.value += value
        print('add result: ', self.value)
        return self
    
    def substract(self, value):
        self.value -= value
        print('substract result: ', self.value)
        return self
        
if __name__ == "__main__":
    fire.Fire(Number)