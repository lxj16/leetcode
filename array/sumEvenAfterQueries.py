class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(i for i in A if i % 2 == 0)
        even_sums = []

        for value, index in queries:
            if A[index] % 2 == 0:
                even_sum -= A[index]
            A[index] += value
            if A[index] % 2 == 0:
                even_sum += A[index]

            even_sums.append(even_sum)

        return even_sums
