from MainMemory import MainMemory

proccess_vriables = {}
variable_found = False


def main():
    print(proccess_vriables)
    Mem = MainMemory()
    while (True):
        instr = input().split()
        if (instr[0] == 'Request'):
            var_name = instr[1]
            for key in proccess_vriables.keys():
                if var_name in proccess_vriables[key].keys():
                    variable_found = True

                    logical_address = Mem.logical(
                        proccess_vriables[key], var_name)
                    print(
                        f'Logical: Page {logical_address[0]} - Offset {logical_address[1]}')

                    physical_Address = Mem.physical(
                        proccess_vriables[key], var_name, key)
                    print(
                        f'Physical: Frame {physical_Address[0]} - Offset {physical_Address[1]}')

            if variable_found == False:
                print("Variable Could Not Be Found!")

            variable_found = False
        else:
            print("Invalid Input!")


if __name__ == "__main__":
    with open("Memory-Management\Processes.txt") as f:
        proc_vars = f.readlines()
        process_name = None
        vrs = {}
        for line in proc_vars:
            x = line.split()
            if x[0] == 'Process':
                if process_name == None:
                    pass
                else:
                    proccess_vriables[process_name] = vrs
                    vrs = {}
                process_name = x[1]

            else:
                vrs[x[1]] = int(x[2])
        proccess_vriables[process_name] = vrs

    main()
