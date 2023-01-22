from MainMemory import MainMemory
from HardDisk import HardDisk
from Process import Process

processes = []
variable_found = False


def main():
    Mem = MainMemory()
    hard_disk = HardDisk()
    while (True):
        instr = input().split()
        if (instr[0] == 'r'):
            var_name = instr[1]
            for process in processes:
                if var_name in process.variables.keys():
                    variable_found = True
                    # hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiit
                    if Mem.hit(process.variables, var_name, process.name):
                        logical_address = Mem.relative(
                            process.variables, var_name)
                        print(
                            f'Relative: Page {logical_address[0]} - Offset {logical_address[1]}')

                        physical_Address = Mem.logical(
                            process.variables, var_name, process.name)
                        print(
                            f'Logical: Frame {physical_Address[0]} - Offset {physical_Address[1]}')

                        print(f'Physical: Byte {physical_Address[0]*400 + physical_Address[1]}')
                        x = Mem.frames[physical_Address[0]]
                        # mhptk effecive way!
                        Mem.used[x] += 1
                        print(x, " : ", Mem.used)


                    else:
                        relative = hard_disk.relative(
                            process.variables, var_name)
                        print(
                            f'Hard Disk : Relative: Page {relative[0]} - Offset {relative[1]}')

                        logical = hard_disk.logical(
                            process.variables, var_name, process.name)
                        print(
                            f'Hard Disk : Logical: Frame {logical[0]} - Offset {logical[1]}')
                        new_frame = hard_disk.frames[logical[0]]
                        replaced = ''
                        mh = min(Mem.used.values())
                        for k, v in Mem.used.items():
                            if v == mh:
                                replaced = k
                                Mem.used.pop(k)
                                break
                        Mem.frames[Mem.frames.index(replaced)] = new_frame
                        Mem.used[new_frame] = 0



            if variable_found == False:
                print("Variable Could Not Be Found!")

            variable_found = False
        else:
            print("Invalid Input!")


if __name__ == "__main__":
    with open("Processes.txt") as f:
        proc_vars = f.readlines()
        process_name = None
        vrs = {}
        for line in proc_vars:
            x = line.split()
            if x[0] == 'Process':
                if process_name == None:
                    pass
                else:
                    processes.append(Process(process_name, vrs))
                    vrs = {}
                process_name = x[1]

            else:
                vrs[x[1]] = int(x[2])
        processes.append(Process(process_name, vrs))

    main()
