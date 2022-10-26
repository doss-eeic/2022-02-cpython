import unittest


class ListSubscriptTest(unittest.TestCase):
    def test_small_list(self):
        ls = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(ls[1, 2], 6)

    def test_large_list(self):
        ls = [[[[[[[[[[123456789]]]]]]]]]]
        self.assertEqual(ls[(0,) * 9], [123456789])

    def test_slice(self):
        ls = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertEqual(ls[2:3, -1, ::-1, 1::2], [11, 9])

    def test_assign(self):
        ls = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        ls[1, 2] = 60
        self.assertEqual(ls[1, 2], 60)


if __name__ == '__main__':
    unittest.main()
