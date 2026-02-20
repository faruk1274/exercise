# Classes and objects

class ShoppingList:
    def __init__(self):
        self.items = []

    def number_of_items(self):
        return len(self.items)

    def item(self, index: int):
        return self.items[index - 1][0]

    def amount(self, index: int):
        return self.items[index - 1][1]

    # METHOD YOU ADD
    def add(self, item: str, amount: int):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i] = (item, self.items[i][1] + amount)
                return
        self.items.append((item, amount))


shopping_list = ShoppingList()
shopping_list.add("banana", 3)
shopping_list.add("apple", 2)
shopping_list.add("banana", 2)

print(shopping_list.number_of_items())  # 2
print(shopping_list.item(1))            # banana
print(shopping_list.amount(1))          # 5
print(shopping_list.item(2))            # apple
print(shopping_list.amount(2))          # 2