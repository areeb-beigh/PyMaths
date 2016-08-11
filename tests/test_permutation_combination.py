# Python imports
import unittest

# Local imports
from src.permutation_combination import calculate


class PermutationCombinationTestCase(unittest.TestCase):
    def setUp(self):
        # ((n,r), answer)
        self.permutations = [((5,2), 20), ((20,10), 670442572800)]
        self.combinations = [((5,2), 10), ((20,10), 184756.0)]

    def test_permutations(self):
        for permutation_tuple in self.permutations:
            n = permutation_tuple[0][0]
            r = permutation_tuple[0][1]
            answer = permutation_tuple[1]
            self.assertEqual(calculate(n,r)[0], answer)

    def test_combinations(self):
        for combination_tuple in self.combinations:
            n = combination_tuple[0][0]
            r = combination_tuple[0][1]
            answer = combination_tuple[1]
            self.assertEqual(calculate(n,r)[1], answer)


if __name__ == '__main__':
    unittest.main()
