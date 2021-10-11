import math
import unittest
import TeoriaQ as tq


class theory_test(unittest.TestCase):

    def test_pp(self):
        self.assertEqual(tq.prob_position(2, [(-3, -1), (0, -2), (0, 1), (2, 0)]), 0.053)

    def test_amt(self):
        self.assertEqual(
            tq.amplitud_tran([(-1, -4), (2, -3), (-7, 6), (-1, 1), (-5, -3), (5, 0), (5, 8), (4, -4), (8, -7), (2, -7)],
                             [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]),
            (-3, 19))

    def test_esvalue(self):
        self.assertEqual(
            tq.expected_value([[(1, 0), (0, -1)], [(0, 1), (2, 0)]], [(math.sqrt(2) / 2, 0), (0, math.sqrt(2) / 2)]),
            (2.5, 0))

    def test_mediavar(self):
        self.assertEqual(
            tq.mediaandvar([[(1, 0), (0, -1)], [(0, 1), (2, 0)]], [(math.sqrt(2) / 2, 0), (0, math.sqrt(2) / 2)]),
            ([[(0.0, 1.0), (-0.5, 0.0)], [(0.0, 1.0), (-0.5, 0.0)]], (1.2, 0)))

    def test_441(self):
        self.assertEqual(
            tq.cuatro1([[(0, 0), (1, 0)], [(1, 0), (0, 0)]], [[(math.sqrt(2)/2, 0), (math.sqrt(2)/2, 0)],
                                                                           [(math.sqrt(2)/2, 0),
                                                                            (-math.sqrt(2)/2, 0)]]), True)



if __name__ == "__main__":
    unittest.main()
