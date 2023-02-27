def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    height = h * bounce
    while height > window:
        count += 2
        height *= bounce
    return count