class Calculator:

    def add(self, a, b):
        addition = a + b
        print("Result of addition:", addition)

    def sub(self, a, b):
        subtraction = a - b
        print("Result of subtraction:", subtraction)

    def mul(self, a, b):
        multiplication = a * b
        print("Result of multiplication:", multiplication)

    def div(self, a, b):
        if b != 0:
            division = a / b
            print("Result of division:", division)
        else:
            print("Error: Division by zero")

    def choices(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        choice = input("Enter your choice (+ for addition, - for subtraction, * for multiplication, / for division): ")
        if choice == "+":
            self.add(a, b)
        elif choice == "-":
            self.sub(a, b)
        elif choice == "*":
            self.mul(a, b)
        elif choice == "/":
            self.div(a, b)
        else:
            print("Invalid choice")


c = Calculator()
c.choices()
