# Component Interface
class Pizza:
    def cost(self):
        pass

# Concrete Component
class MargheritaPizza(Pizza):
    def cost(self):
        return 8.0

# Decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def cost(self):
        return self._pizza.cost()

# Concrete Decorator
class CheeseTopping(ToppingDecorator):
    def cost(self):
        return self._pizza.cost() + 2.0

# Concrete Decorator
class PepperoniTopping(ToppingDecorator):
    def cost(self):
        return self._pizza.cost() + 3.0

if __name__ == "__main__":
    pizza = MargheritaPizza()
    print(f"Cost of Margherita Pizza: ${pizza.cost()}")  # Print the cost of a plain Margherita pizza

    pizza_with_cheese = CheeseTopping(pizza)
    print(f"Cost of Margherita Pizza with Cheese: ${pizza_with_cheese.cost()}")  # Print the cost of a Margherita pizza with cheese

    pizza_with_pepperoni = PepperoniTopping(pizza)
    print(f"Cost of Margherita Pizza with Pepperoni: ${pizza_with_pepperoni.cost()}")  # Print the cost of a Margherita pizza with pepperoni
