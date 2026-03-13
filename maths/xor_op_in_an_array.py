class Solution(object):
    def xorOperation(self, n, start):
        arr = []
        result = 0
        for i in range(n):
            arr.append(start +(2*i))
            result ^= arr[i]
        return result
      '''could be done using 
      curr = start + (2*i)
      result ^= curr '''
