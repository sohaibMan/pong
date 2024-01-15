def calculate_reward(bar, ball):
    if bar.top <= ball.centery <= bar.bottom:
        return 1
    else:
        return -1


def centre_to_state(centre, screen_height, bar_height):
    a = 0
    b = bar_height
    s = 0
    for i in range(int(screen_height / bar_height)):
        if a < centre < b:
            s = (b / bar_height) - 1
        else:
            a += bar_height
            b += bar_height
    return int(s)
