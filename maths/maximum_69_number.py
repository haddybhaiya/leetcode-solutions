class Solution:
    def maximum69Number (self, num: int) -> int:
        val = str(num)
        value = ""
        cnt = 1
        for i in val:
            if i == "6" and cnt ==1:
                value += "".join("9")
                cnt-=1
            else:
                value+=i
        return 0 if not value else int(value)