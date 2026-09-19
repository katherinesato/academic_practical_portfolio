import unittest

from bag_collection import BagCollection


class CountTestCase(unittest.TestCase):

    def test_count1(self):
        """Test count with an empty bag """
        bag = BagCollection()
        self.assertEqual(bag.count(3), 0)
        self.assertEqual(bag.count(True), 0)
        self.assertEqual(bag.count("Hi"), 0)
        self.assertEqual(bag.count([]), 0)
        self.assertEqual(bag.count([1, 2]), 0)

    def test_count2(self):
        """Test count with a bag containing int elements"""
        bag = BagCollection([2, 2, 2, 8, 9, 12, -15, -15, 27, 0, 0])
        self.assertEqual(bag.count(2), 3)
        self.assertEqual(bag.count(-15), 2)
        self.assertEqual(bag.count(0), 2)
        self.assertEqual(bag.count(8), 1)
        self.assertEqual(bag.count(84), 0)

    def test_count3(self):
        """Test count with a bag containing float, 'double' elements"""
        bag = BagCollection([5.2, 5.2, -4.0, 4.0, 5.78493])
        self.assertEqual(bag.count(5.2), 2)
        self.assertEqual(bag.count(-4.0), 1)
        self.assertEqual(bag.count(5.78493), 1)
        self.assertEqual(bag.count(84.7), 0)

    def test_count4(self):
        """Test count with a bag containing char and string elements"""
        bag = BagCollection(
            ['a', 'a', "This", "A", "A", "Katherine", '3.2451'])
        self.assertEqual(bag.count("This"), 1)
        self.assertEqual(bag.count('a'), 2)
        self.assertEqual(bag.count("Katherine"), 1)
        self.assertEqual(bag.count('3.2451'), 1)
        self.assertEqual(bag.count("Hi"), 0)

    def test_count5(self):
        """Test count with a bag containing boolean elements"""
        bag = BagCollection([True, True, True])
        self.assertEqual(bag.count(True), 3)
        self.assertEqual(bag.count(False), 0)

    def test_count6(self):
        """Test count with a bag that contain lists, tuples, dict as elements"""
        bag = BagCollection([[1, 2], [], [], (3, 7), (3, 7),
                             {1: 1, 2: 2}, {"Dad": 35, "Mom": 34}])
        self.assertEqual(bag.count([1, 2]), 1)
        self.assertEqual(bag.count([]), 2)
        self.assertEqual(bag.count((3, 7)), 2)
        self.assertEqual(bag.count({1: 1, 2: 2}), 1)
        self.assertEqual(bag.count({"Dad": 35, "Mom": 34}), 1)


class RemoveTestCase(unittest.TestCase):

    def test_remove1(self):
        """Test removing from an empty bag."""
        bag = BagCollection()
        with self.assertRaises(ValueError):
            bag.remove(10)

    def test_remove2(self):
        """Test removing an item that isn't in the bag."""
        bag = BagCollection([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(ValueError):
            bag.remove(10)

    def test_remove3(self):
        """Test removing an item of value int."""
        bag = BagCollection([1, 3, 4, 4, 7, 2, 3])
        self.assertEqual(bag.remove(4), 4)
        self.assertEqual(bag.remove(7), 7)

    def test_remove4(self):
        """Test removing an item of value floar, 'double'."""
        bag = BagCollection([1.0, 3.7, 4.2, 4.2, 7.8, 2.79, 3.753])
        self.assertEqual(bag.remove(4.2), 4.2)
        self.assertEqual(bag.remove(3.753), 3.753)

    def test_remove5(self):
        """Test removing an item of value char, string."""
        bag = BagCollection(["Hi", "Hi", "A", 'a', '33'])
        self.assertEqual(bag.remove("Hi"), "Hi")
        self.assertEqual(bag.remove("A"), "A")
        self.assertEqual(bag.remove('a'), 'a')
        self.assertEqual(bag.remove('33'), '33')

    def test_remove6(self):
        """Test removing an item of value bool."""
        bag = BagCollection([True, False])
        self.assertEqual(bag.remove(True), True)
        self.assertEqual(bag.remove(False), False)

    def test_remove7(self):
        """Test removing an item of value list, tuple, dict."""
        bag = BagCollection([[True, False], (1, 2), {33: "Name"}])
        self.assertEqual(bag.remove([True, False]), [True, False])
        self.assertEqual(bag.remove((1, 2)), (1, 2))
        self.assertEqual(bag.remove({33: "Name"}), {33: "Name"})


class GrabTestCase(unittest.TestCase):

    def test_grab1(self):
        """Test granning an item from an empty bag."""
        bag = BagCollection()
        with self.assertRaises(ValueError):
            bag.grab()

    def test_grab2(self):
        """Test granning an item with int values."""
        bag = BagCollection([3, 3, 3])
        init_len = len(bag)
        grabbed_item = bag.grab()
        self.assertEqual(grabbed_item, 3)
        self.assertEqual(len(bag), init_len - 1)

    def test_grab3(self):
        """Test granning an item with float, 'double' values."""
        bag = BagCollection([3.3, 3.3, 3.3])
        init_len = len(bag)
        grabbed_item = bag.grab()
        self.assertEqual(grabbed_item, 3.3)
        self.assertEqual(len(bag), init_len - 1)

    def test_grab4(self):
        """Test granning an item with char, string values."""
        bag1 = BagCollection(['a', 'a', 'a'])
        init_len = len(bag1)
        grabbed_item = bag1.grab()
        self.assertEqual(grabbed_item, 'a')
        self.assertEqual(len(bag1), init_len - 1)

        bag2 = BagCollection(["Hi", "Hi", "Hi"])
        init_len = len(bag2)
        grabbed_item = bag2.grab()
        self.assertEqual(grabbed_item, "Hi")
        self.assertEqual(len(bag2), init_len - 1)

    def test_grab5(self):
        """Test granning an item with lists, tuples, dict."""
        bag1 = BagCollection([[1, 2], [1, 2], [1, 2]])
        init_len = len(bag1)
        grabbed_item = bag1.grab()
        self.assertEqual(grabbed_item, [1, 2])
        self.assertEqual(len(bag1), init_len - 1)

        bag2 = BagCollection([(1, 2), (1, 2), (1, 2)])
        init_len = len(bag2)
        grabbed_item = bag2.grab()
        self.assertEqual(grabbed_item, (1, 2))
        self.assertEqual(len(bag2), init_len - 1)

        bag3 = BagCollection([{1: 2}, {1: 2}, {1: 2}])
        init_len = len(bag3)
        grabbed_item = bag3.grab()
        self.assertEqual(grabbed_item, {1: 2})
        self.assertEqual(len(bag3), init_len - 1)


class DunderAddTestCase(unittest.TestCase):

    def test_dunder_add1(self):
        """Test dunder add with elems that are not BagCollections."""
        bag = BagCollection([1, 5, 6, 8])
        not_bag = "Hi"
        with self.assertRaises(TypeError):
            bag3 = bag + not_bag

    def test_dunder_add2(self):
        """Test dunder add with empty BagCollections."""
        bag1 = BagCollection([1, 5, 6, 8])
        bag2 = BagCollection()
        bag3 = bag1 + bag2
        bag1 = BagCollection([1, 5, 6, 8])
        bag2 = BagCollection()
        bag3 = bag1 + bag2
        self.assertEqual(bag3, BagCollection([1, 5, 6, 8]))

        bag4 = BagCollection()
        bag5 = BagCollection()
        bag6 = bag4 + bag5
        self.assertEqual(bag6, BagCollection([]))

    def test_dunder_add3(self):
        """Test dunder add with BagCollections (int values)."""
        bag1 = BagCollection([1, 5, 6, 8])
        bag2 = BagCollection([40, 80, 90])
        bag3 = bag1 + bag2
        self.assertEqual(bag3, BagCollection([1, 5, 6, 8, 40, 80, 90]))

    def test_dunder_add4(self):
        """Test dunder add with BagCollections (float, 'double' values)."""
        bag1 = BagCollection([1.0, 5.0, 6.0, 8.0])
        bag2 = BagCollection([40.0])
        bag3 = bag1 + bag2
        self.assertEqual(bag3, BagCollection([1.0, 5.0, 6.0, 8.0, 40.0]))

    def test_dunder_add5(self):
        """Test dunder add with BagCollections (char, string values)."""
        bag1 = BagCollection(['a', "Hi"])
        bag2 = BagCollection(["Bee"])
        bag3 = bag1 + bag2
        self.assertEqual(bag3, BagCollection(['a', "Hi", "Bee"]))

    def test_dunder_add6(self):
        """Test dunder add with BagCollections (lists, tuples, dict values)."""
        bag1 = BagCollection([[1, 2], (1, 2)])
        bag2 = BagCollection([{1: 2}])
        bag3 = bag1 + bag2
        self.assertEqual(bag3, BagCollection([[1, 2], (1, 2), {1: 2}]))


class EqTestCase(unittest.TestCase):

    def test_eq1(self):
        """Test __eq__ with objects that are not BagCollections."""
        bag1 = BagCollection([1, 5, 6, 8])
        not_bag1 = "Hi"
        self.assertFalse(bag1 == not_bag1)

        bag2 = BagCollection([1, 5, 6, 8])
        not_bag2 = [1, 5, 6, 8]
        self.assertFalse(bag2 == not_bag2)

    def test_eq2(self):
        """Test __eq__ with objects that are BagCollections."""
        bag1 = BagCollection([1, 5, 6, 8])
        bag2 = BagCollection([1, 5, 6, 8])
        bag3 = bag2
        bag4 = BagCollection([40, 80, 90])
        bag5 = BagCollection(['a', "Hello"])
        bag6 = bag5
        self.assertTrue(bag1 == bag1)
        self.assertTrue(bag1 == bag2)
        self.assertTrue(bag1 == bag3)
        self.assertTrue(bag2 == bag3)
        self.assertFalse(bag1 == bag4)
        self.assertFalse(bag4 == bag5)
        self.assertTrue(bag5 == bag6)

    def test_eq3(self):
        """Test __eq__ with BagCollections and order of elements."""
        bag1 = BagCollection([1, 5, 6, 8])
        bag2 = BagCollection([8, 5, 6, 1])
        bag3 = BagCollection([1.1, 2.2, 3.3])
        bag4 = BagCollection([1.1, 3.3, 2.2])
        bag5 = BagCollection(['a', 'b'])
        bag6 = BagCollection(['b', 'a'])
        bag7 = BagCollection([[1, 2], (1, 2), {1: 2}])
        bag8 = BagCollection([{1: 2}, [1, 2], (1, 2)])
        self.assertTrue(bag1 == bag2)
        self.assertTrue(bag3 == bag4)
        self.assertTrue(bag5 == bag6)
        self.assertTrue(bag7 == bag8)


if __name__ == '__main__':
    unittest.main(verbosity=2)
