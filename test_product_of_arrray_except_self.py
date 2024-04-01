from unittest import TestCase
from parameterized import parameterized
from product_of_arrray_except_self import ProductOfArrayExceptSelfSolution

class TestSolution(TestCase):

    @parameterized.expand([
        [1,2,3,4], [24,12,8,6]
    ])
    def test_product_except_self(self, X, expected):
        solution = ProductOfArrayExceptSelfSolution()

        actual = solution.productExceptSelf(X)
        assert expected == actual
        self.fail()
