from reptile import Reptile

class Snake(Reptile) :
    def __int__(self):
        super().__init__()
        self.forked_tongue = True

    def use_forked_tongue_smell(self):
        return "Yes"

smart_snake = Snake
print(smart_snake.hunt()) # inherited from parent class
print(smart_snake.eat()) # inherited from grandparents class
print(smart_snake.use_forked_tongue_smell()) # Inherited from current class
