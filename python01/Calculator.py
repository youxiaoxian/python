from decimal import Decimal

class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b == 0:
            return 0
            print("div zero")
        else:
            return Decimal(a / b).quantize(Decimal("0.00"))
            # return round(a / b, 2)
