class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ""
        cnt=0
        for i in str(n)[::-1]:
           
            if cnt>0 and cnt %3==0:
                ans+="."
            ans+=i
            cnt+=1
        return ans[::-1]