first_lane = [i for i in input().split()]
second_lane = [i for i in input().split()]
third_lane = [i for i in input().split()]

board = [first_lane, second_lane, third_lane]


def check_plr(bo, le):
    return ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or  # across the top
            (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or  # across the middle
            (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or  # across the bottom
            (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or  # down the left side
            (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or  # down the middle
            (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or  # down the right side
            (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or  # diagonal
            (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le))  # diagonal


check_plr_1 = check_plr(board, "1")
check_plr_2 = check_plr(board, "2")

if check_plr_1:
    print("First player won")
elif check_plr_2:
    print("Second player won")
else:
    print("Draw!")
