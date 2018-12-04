class Pc(object):
    def __init__(self, pid: int, pages: int):
        self.pid = pid
        self.pages = pages


class PgFrame(object):
    def __init__(self, size: int):
        self.size = size
        self.frames = []
        for i in range(size):
            self.frames.append([0, 0, "NULL"])
        self.frame_pointer = -1

    def show(self):  # 查看所有页框
        print("-" * 27)
        print("{:^7}|{:^5}|{:^5}|{:^7}".format("frame", "A", "M", "page"))
        print("-" * 27)
        i = 0
        for each in self.frames:
            print("{:^7}|{:^5}|{:^5}|{:^7}".format(i, each[0], each[1], each[2]))
            i += 1
        print("-" * 27)
        print()

    def go1(self, page: int):  # 操作1：寻找1类页面并替换
        # print("操作1：req page =", page)
        temp_p = self.frame_pointer  # 用temp_p暂存指针当前位置

        while True:
            self.frame_pointer = (self.frame_pointer + 1) % self.size
            if self.frames[self.frame_pointer][0] == 0 and self.frames[self.frame_pointer][1] == 0:  # 1类页面
                print(
                    "replace:\nframe: {:^5}, page:{:^5}".format(self.frame_pointer, self.frames[self.frame_pointer][2]))
                self.frames[self.frame_pointer] = [1, 0, page]
                return True

            if self.frame_pointer == temp_p:  # 扫描一周后停止
                # print("操作1未找到\n")
                break
        return False

    def go2(self, page: int):  # 操作2：寻找A=0,M=1的二类页面
        # print("操作2：req page =", page)
        temp_p = self.frame_pointer  # 用temp_p暂存指针当前位置
        while True:
            self.frame_pointer = (self.frame_pointer + 1) % self.size
            if self.frames[self.frame_pointer][0] == 0 and self.frames[self.frame_pointer][1] == 1:  # 2类页面
                print(
                    "replace:\nframe: {:^5}, page:{:^5}".format(self.frame_pointer, self.frames[self.frame_pointer][2]))
                self.frames[self.frame_pointer] = [1, 0, page]
                return True
            self.frames[self.frame_pointer][0] = 0  # 修改访问位为0

            if self.frame_pointer == temp_p:  # 扫描一周后停止
                # print("操作2未找到\n")
                break

        return False

    def frame_req(self, page: int):
        for frame in self.frames:
            if page == frame[2]:
                print("page already in frame!")
                return

        success = False
        while not success:
            # 第一轮循环
            success = self.go1(page)
            if success:  # 如果第一轮置换成功则直接退出
                break

            # 第二轮循环
            success = self.go2(page)
            if success:
                break  # 如果第二轮成功则退出
            else:
                self.frame_pointer = -1
        print("sucess!\n")

    def edit(self, frame_no: int, content: list):
        self.frames[frame_no] = content


def main():
    frame1 = PgFrame(4)
    pc1 = Pc(0, 12)

    cmd = ''
    while True:
        cmd = input('cmd:>> ').split()
        # print(cmd)
        if cmd[0] == 'exit' and len(cmd) == 1:
            return
        elif cmd[0] == 'req' and len(cmd) == 2:
            try:
                req_page = int(cmd[1])
            except ValueError:
                print("bad param!")
                continue

            if 0 <= req_page < pc1.pages:
                frame1.frame_req(req_page)
            else:
                print("bad param!")

        elif cmd[0] == 'show' and len(cmd) == 1:
            frame1.show()

        elif cmd[0] == 'edit' and len(cmd) == 5:
            try:
                fid = int(cmd[1])
                flag_a = int(cmd[2])
                flag_m = int(cmd[3])
                page_no = int(cmd[4])
            except ValueError:
                print("bad params!")
                continue

            if flag_a in [0, 1] and flag_m in [0, 1] and 0 <= page_no:
                frame1.edit(fid, [flag_a, flag_m, page_no])
            else:
                print("bad params!")

        else:
            print("bad command!")


main()
