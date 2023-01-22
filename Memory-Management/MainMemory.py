class MainMemory():
    def __init__(self) -> None:
        self.frames = ['D.0', 'B.1', 'B.0',
                       'D.2', 'D.1', 'B.2', 'A.1', 'A.2', 'A.0', 'D.3']
        self.used = {'D.0': 0,
                     'B.1': 2,
                     'B.0': 2,
                     'D.2': 40,
                     'D.1': 5,
                     'B.2': 6,
                     'A.1': 7,
                     'A.2': 8,
                     'A.0': 9,
                     'D.3': 10}

    # hard disk with 4000 bytes capacity - each frame 400 bytes - 10 frames
    # D.4 - B.3 - B.4

    def relative(self, proc_vars, var_name):
        page = 1
        offset = 0
        available_space = 0

        for var in proc_vars.keys():
            if available_space + proc_vars[var] <= 400:
                available_space += proc_vars[var]
            else:
                available_space = 0
                page += 1
                offset = 0

            if var == var_name:
                return (page, offset)

            offset += proc_vars[var]
            if offset == 400:
                offset = 0
                page += 1
                available_space = 0

    def logical(self, proc_vars, var_name, proc_name):
        logical = self.relative(proc_vars, var_name)
        try:
            return (self.frames.index(f'{proc_name}.{logical[0]-1}'), logical[1])
        except:
            print(f'{proc_name}.{logical[0]-1} Not in MainMemory')
            return f'{proc_name}.{logical[0]-1}'

    def hit(self, proc_vars, var_name, proc_name):
        relative = self.relative(proc_vars, var_name)
        frame_name = f'{proc_name}.{relative[0]-1}'
        if frame_name in self.frames:
            print("Frame is already in Main Memory")
            return True
        else:
            print("Frame not found in Main Memory! Page fault occurred")
            return False