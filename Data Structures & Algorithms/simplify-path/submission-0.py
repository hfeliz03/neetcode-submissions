class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = []

        for cmd in path.split("/"):
            if cmd == "" or cmd == ".": continue
            elif cmd == "..": 
                if canonical: canonical.pop()
            else: canonical.append(cmd)
        string = ""
        for cmd in canonical: string += "/" + cmd
        return string if canonical else "/"