def lerp(val, min, max):
    return (max-min)*val + min

def invLerp(val, min, max):
    if min == max:
        return 0
    else:
        return (val-min)/(max-min)

def sign(x):
    return (x>0)-(x<0)

def clamp(x, min, max):
    if x > max:
        return max
    elif x < min:
        return min
    else:
        return x

def percentage(x, y):
    return x * y if y > 0 else abs(x / y)

def distToPercent(x, y):
    if x <= y:
        return y/x

    else:
        return -(x/y)