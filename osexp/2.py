def main():
    cmd = ''
    pli = [[0, None]]
    while True:
        cmd = input('cmd:>> ').split(' ')
        if len(cmd) == 3 and cmd[0] == 'createpc':
            exist = False
            parent_exist = False
            for each_progress in pli:

                # 判断进程是否已经存在
                if each_progress[0] == int(cmd[1]):
                    print('progress has already exist!')
                    exist = True
                    break

                # 判断父进程是否存在
                if each_progress[0] == int(cmd[2]):
                    parent_exist = True
                    break

            if exist:
                continue
            if not parent_exist:
                print('can not find parent progress!')
                continue
            else:
                pid = int(cmd[1])
                ppid = int(cmd[2])
                pli.append([pid, ppid])

        elif len(cmd) == 2 and cmd[0] == 'delete':
            for each_p in pli:
                if each_p[0] == int(cmd[1]):
                    pli.pop(pli.index(each_p))
                if each_p[1] == int(cmd[1]):
                    pli.pop(pli.index(each_p))

        elif len(cmd) == 1 and cmd[0] == 'show':
            # print(pli)
            for each_p in pli:
                print(each_p, end=': ')
                for each in pli:
                    if each[1] == each_p[0]:
                        print(each, end='  ')
                print()

        else:
            print('bad command!')


if __name__ == '__main__':
    main()
