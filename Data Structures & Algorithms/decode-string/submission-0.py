class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []

        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                str_stack.append(curr)
                num_stack.append(num)

                curr = ""
                num = 0

            elif ch == "]":
                repeat = num_stack.pop()
                prev = str_stack.pop()

                curr = prev + curr * repeat

            else:
                curr += ch

        return curr