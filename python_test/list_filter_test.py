import unittest

class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class ListFilterTest(unittest.TestCase):
    
    def test_small_int_list(self):
        ls = [1, 4, 5]
        self.assertEqual(ls.filter(lambda x: x>2), [4, 5])
        self.assertEqual(len(ls.filter(lambda x: x>2)), 2)
    
    def test_small_float_list(self):
        ls = [1.2, 3.4, 5.6]
        self.assertEqual(ls.filter(lambda x: x>3.4), [5.6])
    
    def test_large_int_list(self):
        ls = [
            231212340289713793871,
            123234203423412312320,
            212342423309546512039
        ]
        self.assertEqual(ls.filter(lambda x: x > 212342423309546512040), [231212340289713793871])
        
    def test_products(self):
        ls = [
            Product("apple", 100),
            Product("grape", 240),
            Product("rice", 12346),
            Product("hoge", 1234765),
            Product("fuga", 1276534),
            Product("foo", 12343123),
            Product("bar", 122134),
        ]
        self.assertEqual(
            ls.filter(lambda p: len(p.name) == 4)\
                .map(lambda p: p.price).max(), 1276534
        )

if __name__ == '__main__':
    unittest.main()