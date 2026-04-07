class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False
        # Total steps to return to (0,0)
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        self.moved = True
        # Use modulo to handle large step counts
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        s = self.pos
        w, h = self.w, self.h
        
        # Determine (x, y) based on the current step count s
        if 0 <= s < w:
            return [s, 0]
        elif w <= s < w + h - 1:
            return [w - 1, s - (w - 1)]
        elif w + h - 1 <= s < 2 * w + h - 2:
            return [w - 1 - (s - (w + h - 2)), h - 1]
        else: # 2*w + h - 2 <= s < perimeter
            return [0, h - 1 - (s - (2 * w + h - 3))]

    def getDir(self) -> str:
        s = self.pos
        w, h = self.w, self.h
        
        # Special case: If we moved and landed at (0,0) via modulo
        if self.moved and s == 0:
            return "South"
            
        # Standard direction boundaries
        if 1 <= s < w:
            return "East"
        elif w <= s < w + h - 1:
            return "North"
        elif w + h - 1 <= s < 2 * w + h - 2:
            return "West"
        elif 2 * w + h - 2 <= s < self.perimeter or s == 0:
            return "South" if self.moved else "East"
        
        return "East"