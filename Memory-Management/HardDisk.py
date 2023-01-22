class HardDisk():
    def __init__(self) -> None:
        self.frames = ['B.4', 'A.2', 'D.4', 'D.0', 'B.1', 'B.0',
                       'D.2', 'D.1', 'B.2', 'A.1', 'B.3', 'A.0', 'D.3']

    # hard disk with 400000000 bytes capacity - each frame 400 bytes - 1000000 frames

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
            return (self.frames.index(f'{proc_name}.{logical[0] - 1}'), logical[1])
        except:
            print(f'{proc_name}.{logical[0] - 1} Not in Hard Disk')
            return f'{proc_name}.{logical[0] - 1}'
