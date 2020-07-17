'''
* Create a file called `item.py` and add an `Item` class in there.

  * The item should have `name` and `description` attributes.

     * Hint: the name should be one word for ease in parsing later.

  * This will be the _base class_ for specialized item types to be declared
    later.
'''

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f' {self.name} : {self.description}'

    def on_take(self, item):
        print(f'\n You have picked up {self.name}!')

    def on_drop(self, item):
        print(f'\n You have dropped {self.name}.')
