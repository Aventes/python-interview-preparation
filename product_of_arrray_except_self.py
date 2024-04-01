class ProductOfArrayExceptSelfSolution:

    def productExceptSelf(self, nums):
        n = len(nums)
        product = [0] * n
        product[0] = 1

        for i in range(1, n):
            product[i] = nums[i - 1] * product[i - 1]

        suffix_product = 1

        for i in range(n - 1, -1, -1):
            product[i] = suffix_product * product[i]
            suffix_product = suffix_product * nums[i]

        return product


if __name__ == "__main__":
    ProductOfArrayExceptSelfSolution().productExceptSelf([1, 2, 3, 4])

        # prefix = [0] * n
        # suffix = [-1] * n
        # result = [0] * n
        #
        # prefix[0] = 1
        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]
        #
        # suffix[-1] = 1
        # for i in range(n - 2, -1, -1):
        #     suffix[i] = nums[i + 1] * suffix[i + 1]
        #
        # for i in range(n):
        #     result[i] = prefix[i] * suffix[i]
        #
        # return result
