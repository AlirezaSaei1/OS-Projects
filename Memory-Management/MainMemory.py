class MainMemory():
    def __init__(self) -> None:
        self.frames = ['D.0', 'B.1', 'B.0',
                       'D.2', 'D.1', '-', '-', '-', '-', '-']

    def logical(self, proc_vars, var_name):
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

    def physical(self, proc_vars, var_name, proc_name):
        logical = self.logical(proc_vars, var_name)
        return (self.frames.index(f'{proc_name}.{logical[0]-1}'), logical[1])
