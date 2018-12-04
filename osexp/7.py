disk_req_list = [150, 54, 71, 24, 58, 19, 38, 193, 3, 55, 10]
arm = 69  # 磁头所在位置
direct = True  # 当前磁臂移动方向，True表示向里（磁道号增大方向）


def main():
    cmd = ''
    global disk_req_list
    global direct
    while True:
        cmd = input('cmd:>> ').split()
        # print(cmd)
        if cmd[0].lower() == 'exit' and len(cmd) == 1:
            return

        elif cmd[0].lower() == 'set' and len(cmd) == 2:
            if cmd[1].lower() == 'req':
                try:
                    disk_req_list = list(map(int, input("input track request(s):").split()))
                    print(disk_req_list)
                except ValueError:
                    print("bad param(s)!")

            elif cmd[1].lower() == 'arm':
                try:
                    global arm
                    arm = int(input("input arm position:  "))
                except ValueError:
                    print("bad param(s)!\n")

            elif cmd[1].lower() in ['direction', 'direct']:
                try:
                    temp = input("input direction (1 mean in, 0 mean out): ")
                    if temp == '1':
                        direct = True
                    elif temp == '0':
                        direct = False
                    else:
                        print("bad param(s)!\n")
                except ValueError:
                    print("bad param(s)!\n")

            else:
                print("bad param(s)!\n")


        elif cmd[0].lower() == 'scan' and len(cmd) == 1:
            scan()

        elif cmd[0].lower() == 'show' and len(cmd) == 2:
            if cmd[1].lower() == 'req':
                print("disk request list:")
                print(disk_req_list)
                print()

            elif cmd[1].lower() == 'arm':
                print("arm at: {}\n".format(arm))

            elif cmd[1].lower() in ['direct', 'direction']:
                if direct:
                    print('in\n')
                else:
                    print('out\n')

            else:
                print("bad param(s)!\n")

        else:
            print("bad command!\n")


def scan():
    global direct
    global arm
    total_dist = 0
    while len(disk_req_list):
        find = False
        if direct:
            disk_req_list.sort()
            for req in disk_req_list:
                if req >= arm:
                    find = True
                    total_dist += req - arm
                    print("  {:<5} ->   {:<5}".format(arm, req))
                    arm = req
                    disk_req_list.pop(disk_req_list.index(req))
                    break
            if not find:
                direct = False
        else:
            disk_req_list.sort(reverse=True)
            for req in disk_req_list:
                if req <= arm:
                    find = True
                    total_dist += arm - req
                    print("  {:<5} ->   {:<5}".format(arm, req))
                    arm = req
                    disk_req_list.pop(disk_req_list.index(req))
                    break
            if not find:
                direct = True

    print("total distance: {}\n".format(total_dist))


main()
