class Process(object):
    def __init__(self, pid: int, atime: int, stime: int):
        self.pid = pid
        self.arrive_time = atime
        self.service_time = stime
        self.start_time = -1


pli = []
time = 0


def createpc(command: list):
    pli.append(Process(int(command[1]), int(command[2]), int(command[3])))


def show():
    print()
    print("  {:^8} | {:^8} | {:^8}  ".format("pid", "atime", "stime"))
    print('  ' + '-' * 28 + '  ')
    for prog in pli:
        print("  {:<8} | {:<8} | {:<8}  ".format(prog.pid, prog.arrive_time, prog.service_time))


def fcfs():
    pli.sort(key=lambda p: p.arrive_time)
    global time
    print('{:-^45}'.format('fcfs'))
    print("  {:^8} | {:^8} | {:^8} | {:^8}  ".format("pid", "atime", "service", "start"))
    print('  ' + '-' * 41 + '  ')
    for p in pli:
        if time < p.arrive_time:
            p.start_time = p.arrive_time
        else:
            p.start_time = time
        time += p.service_time
        print("  {:<8} | {:<8} | {:<8} | {:^8}  ".format(p.pid, p.arrive_time, p.service_time, p.start_time))
    # pli.clear()


def edit_p(pid: int):
    p_exist = False  # 进程存在标记
    for p in pli:
        if p.pid == pid:
            p_exist = True
            while True:
                try:
                    new_atime = input("pid: {} new arrive time:".format(pid))
                    new_atime = int(new_atime)
                    break
                except ValueError:
                    print("bad command!")
            p.arrive_time = new_atime
            print("change accepted!")

    if p_exist == False:
        print("process do not exist!")


def main():
    cmd = ''
    while True:
        cmd = input('cmd:>> ').split(' ')
        # print(cmd)
        if cmd[0] == 'createpc' and len(cmd) == 4:
            exist = False
            for progress in pli:
                if progress.pid == int(cmd[1]):
                    exist = True
                    break
            if exist:
                print("process already exists!")
                continue

            createpc(cmd)

        elif cmd[0] == 'show' and len(cmd) == 1:
            show()

        elif cmd[0] == 'fcfs' and len(cmd) == 1:
            fcfs()
            global time
            time = 0

            print("do you want to change arrive time?")
            # 处理更改到达时间
            while True:
                temp_in = input("continue? (Y/N): ")
                if temp_in == 'Y' or temp_in == 'y':
                    edit_pid = -1
                    while True:
                        try:
                            edit_pid = int(input("input pid that you want to edit: "))
                            break
                        except ValueError:
                            print('bad command!')
                    edit_p(edit_pid)
                elif temp_in == 'N' or temp_in == 'n':
                    break
                else:
                    print("bad command!")

        elif cmd[0] == 'clear' and len(cmd) == 1:
            pli.clear()

        else:
            print("bad command!")


main()
