class MainMemory():
    def __init__(self) -> None:
        self.frames = ['D0', 'B1', 'B0', 'D2', 'D1', '-', '-', '-', '-', '-']

    def logical(self, proc_vars, var_name):
        print(proc_vars)
        print(var_name)
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
                return f'Logical: Page {page} - Offset {offset}'

            offset += proc_vars[var]
            if offset == 400:
                offset = 0
                page += 1
                available_space = 0

    def physical(self, process, proc_ame, var_name, space):
        pass
