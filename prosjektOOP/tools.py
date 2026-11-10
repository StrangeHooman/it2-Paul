def lerp(val, min, max):
    return (max-min)*val + min

def invLerp(val, min, max):
    return (val-min)/(max-min)

def sign(x):
    (x>0)-(x<0)

def percentage(x, y):
    return x * y if y > 0 else x / y