#class Solution:
    # @param A : integer
    # @return an integer
#    def fibsum(self, A):
class Solution:
    def generate_fib(self, A):
        arr, tmp, prev = [1], 1, 1

        while tmp <= A:
            arr.append(tmp)
            tmp, prev = tmp + prev, tmp

        return arr

    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fib, sol = self.generate_fib(A), 0
        for n in reversed(fib):
            if n > A:
                continue
            elif n == A:
                return sol + 1
            else:
                sol, A = sol + 1, A - n

        return 0
