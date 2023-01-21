class MainMemory():
    def __init__(self) -> None:
        self.rows = [None] * 1000
        self.frame_size = 400
        self.frames = ['D0', 'B1', 'B0', 'D2', 'D1', '-', '-', '-', '-', '-']
