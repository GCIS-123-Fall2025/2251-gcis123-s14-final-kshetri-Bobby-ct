"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ['__item_code', '__item_name', '__item_price'] 
    def __init__(self, code, name, price):
        self.__item_code = code
        self.__item_name = name
        self.__item_price = int(price)  # Really should be float, but the example states simply "24", not "24.0" or "24.00", so using int to match that

    # Accessors
    def get_code(self):
        return self.__item_code
    def get_name(self):
        return self.__item_name
    def get_price(self):
        return self.__item_price
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__item_code == other.__item_code
        else:
            raise TypeError("Types not same")
      
    def to_hash(self):
        to_return = ""
        for char in str(self):
            to_return += str(ord(char))
        return int(to_return)

    def __hash__(self):  # We didn't cover how to do this in lecture, __hash__ was always given to us.  Theroetically the method I implemented should always be unique and therefore work as a usable hash
        return self.to_hash()

    def __repr__(self):
        return f"{self.__item_code}"  # instructions don't mention what to include in the sorted representation so I'm assuming just item code

    def __str__(self):
        return f"({self.__item_code}, {self.__item_name}, {self.__item_price})"  # note if grader isn't Storm: f-strings were covered in our section by Prof. Kshetri
    
    def sort_by_id_key(self):  # im aware it doesn't necessarily need to be in the class but I'm putting it there for organizatoinal purposes
        return self.get_code()


# manual test from main() method
def main():
  item_1 = Item("WOND-0001", "Wonder Bread", "2")
  item_2 = Item("WOND-0002", "Wonder Bagels", 4)
  item_3 = Item("WOND-0002", "Wonder Bagels New and Improved", 5)
  items_sold = set()  # testing hash-ability
  items_sold.add(item_1)
  items_sold.add(item_2)
  items_sold.add(item_3)
  for item in items_sold:  # testing __str__
      print(item)
  print(item_2 == item_3)  # Testing equality by item code
  print(sorted(items_sold, key=Item.sort_by_id_key))  # Testing sort

if __name__ == "__main__":
  main()