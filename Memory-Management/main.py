from MainMemory import MainMemory

proccess_vriables = {}


def main():
    print(proccess_vriables)
    Mem = MainMemory()
    while (True):
        instr = input().split()
        if (instr[0] == 'Request'):
            var_name = instr[1]

            # run instruction

        else:
            print("Invalid Input!")


if __name__ == "__main__":
    with open("Memory-Management\Processes.txt") as f:
        proc_vars = f.readlines()
        print(proc_vars)
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
                print(vrs)
        proccess_vriables[process_name] = vrs

    main()
