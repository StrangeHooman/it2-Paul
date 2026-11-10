def lerp(val, min, max):
    return (max-min)*val + min

def invLerp(val, min, max):
    return (val-min)/(max-min)