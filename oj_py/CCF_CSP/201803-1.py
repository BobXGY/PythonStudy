if __name__ == '__main__':
    game = str(input())
    op_list = game.split(" ")
    combo = False
    base_score = 1
    total_score = 0
    for op in op_list[:-1:]:
        if op == "0":
            break
        if op == "1":
            combo = False
            base_score = 1
        elif op == "2":
            combo = True
            if base_score == 1:
                base_score += 1
            else:
                base_score += 2

        total_score += base_score

    print(total_score)
