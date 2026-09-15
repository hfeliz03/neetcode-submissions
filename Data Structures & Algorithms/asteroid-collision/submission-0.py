class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        q = deque(asteroids)

        def collide():
            nonlocal stack
            while len(stack) > 1:
                if stack[-2] > 0 and stack[-1] < 0:
                    asteroid = stack.pop()
                    if abs(stack[-1]) < abs(asteroid):
                        stack[-1] = asteroid
                    elif abs(stack[-1]) == abs(asteroid):
                        stack.pop()                        
                else:
                    return
                
        for asteroid in q:
            stack.append(asteroid)
            if len(stack) > 1 and asteroid < 0 and stack[-2] > 0 :
                collide()
        return stack
            