"""
Project: Custom List-based Bag ADT (Abstract Data Type)

Description:
    An implementation of the Bag ADT (Multiset) using Python's built-in list data structure. 
    A Bag is a collection that allows duplicate elements, focusing on custom data structure 
    design and collection management.

Author:
    - Katherine Borges Sato

Key Skills & Concepts Demonstrated:
    - Object-Oriented Programming (OOP): Implementation of custom classes and dunder/magic 
      methods (__init__, __len__, __add__, __eq__) for operator overloading and built-in function integration.
    - Data Structures & Algorithms: Designing an Abstract Data Type (ADT), managing underlying lists, 
      and implementing order-independent collection comparison (handling duplicates/multisets).
    - Error & Exception Handling: Robust type checking and input validation using custom exceptions 
      (ValueError, TypeError).
    - Python Best Practices: Use of type hinting, clean code architecture, and standard library modules (random).
"""

import random


class BagCollection:

    def __init__(self, iterable=[]) -> None:
        """Initialize this BagCollection.

        If no iterable is provided, the new BagCollection is empty.
        Otherwise, initialize the BagCollection by adding the values
        provided by the iterable.

        >>> bag = BagCollection()
        >>> bag
        BagCollection([])
        >>> bag = BagCollection([1, 4, 3, 6, 3])
        >>> bag
        BagCollection([1, 4, 3, 6, 3])
        """
        self._elems = []
        for item in iterable:
            self._elems.append(item)
            # or, self.add(item)

    def __len__(self) -> int:
        """Return the number of items in this BagCollection."""
        return len(self._elems)

    def count(self, item: any) -> int:
        """Return the total number of occurrences of item in this bag.

        >>> bag = BagCollection([3, 1, 2, 3, 4])
        >>> bag.count(3)
        2
        >>> bag.count(7)
        0
        """
        return self._elems.count(item)

    def remove(self, item: any) -> any:
        """Remove and return one instance of item from this BagCollection.

        Raises ValueError if the bag is empty.
        Raises ValueError if item is not in the bag.

        >>> bag = BagCollection([3, 1, 2, 3, 4])

        # The bag has 5 elements, including two 3's.
        >>>len(bag)
        5
        >>> bag.count(3)
        2

        # Now remove one 3.
        >>> bag.remove(3)
        3
        >>> bag.count(3)
        1
        >>> len(bag)
        4
        """
        if self._elems == []:
            raise ValueError("bag.remove(", item, "): remove from empty bag")
        if item in self._elems:
            index = self._elems.index(item)
            return self._elems.pop(index)
        raise ValueError("bag.remove(", item, "): x not in bag")

    def grab(self) -> any:
        """Remove and return a randomly selected item from this bag.

        Raises ValueError if the bag is empty.

        >>> bag = BagCollection([3, 1, 2, 3, 4])
        >>> len(bag)
        5

        >>> BagCollection.grab()
        # grab will randomly select one of items stored in the bag,
        # and remove and return that value. The value displayed in the shell
        # will be one of 1, 2, 3 or 4, depending on which item was removed.

        >>> len(bag)
        4
        """
        if self._elems == []:
            raise ValueError("bag.grab(): grab from empty bag")
        grab_item = random.choice(self._elems)
        return self.remove(grab_item)

    def __add__(self, other: 'BagCollection') -> 'BagCollection':
        """Return a new BagCollection containing the concatenation of self and other.

        Raises TypeError if other is not a BagCollection.

        >>> bag1 = BagCollection([1, 3, 5])
        >>> bag2 = BagCollection([2, 4, 6])
        >>> bag3 = bag1 + bag2
        >>> repr(bag3)
        'BagCollection([1, 3, 5, 2, 4, 6])'

        Note: Depending on how __add__ and __repr__ are implemented, the
        order of the elements in the string returned by repr may be different.
        """
        if not isinstance(other, BagCollection):
            raise TypeError(
                "can only concatenate BagCollection to BagCollection")

        return BagCollection(self._elems + other._elems)

    def __eq__(self, other: 'BagCollection') -> bool:
        """Return True if self is equal to the BagCollection referred to by other;
        otherwise return False.

        >>> bag1 = BagCollection([1, 2, 3])
        >>> bag2 = BagCollection([3, 2, 1])
        >>> bag1 == bag2
        True

        >>> bag1 = BagCollection([1, 2, 3])
        >>> bag2 = BagCollection([4, 5, 6])
        >>> bag1 == bag2
        False
        """
        if not isinstance(other, BagCollection):
            return False

        # Solution considering that dict can also be an elem of BagCollection:
        if len(self._elems) != len(other._elems):
            return False

        other_elems_copy = list(other._elems)

        for item in self._elems:
            if item in other_elems_copy:
                other_elems_copy.remove(item)
            else:
                return False

        return True

        # Another solution considering that there are no dict in the BagCollection:
        #
        # list1 = list(self._elems)
        # list2 = list(other._elems)
        # list1.sort()
        # list2.sort()
        # if list1 == list2:
        #   return True

        # return False

