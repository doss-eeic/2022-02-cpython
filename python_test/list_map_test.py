import unittest

class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class ListMapTest(unittest.TestCase):
    
    def test_small_int_list(self):
        ls = [1, 4, 5]
        self.assertEqual(ls.map(lambda x:x+1), [2,5,6])
    
    def test_small_float_list(self):
        ls = [1.2, 3.4, 5.6]
        self.assertEqual(ls.map(lambda x:x*1.1), [1.32, 3.74, 6.16])
    
    def test_large_int_list(self):
        ls = [
            231212340289713793871,
            123234203423412312320,
            212342423309546512039
        ]
        self.assertEqual(ls.map(lambda x: x+1000000000), [231212340290713793871, 123234203424412312320, 212342423310546512039])
        
    def test_products(self):
        ls = [
            Product("apple", 100),
            Product("grape", 240),
            Product("rice", 1234)
        ]
        self.assertEqual(
            ls.map(lambda p: p.price).max(), 1234
        )

if __name__ == '__main__':
    unittest.main()