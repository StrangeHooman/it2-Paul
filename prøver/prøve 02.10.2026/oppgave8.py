# a)
def konverter_tid(sekunder):
    minutter = sekunder // 60
    timer = sekunder // 3600
    minutter = minutter % 60
    return timer, minutter, sekunder % 60

time = konverter_tid(4000)

print(f"{time[0]} t, {time[1]} m, {time[2]} s")


# b)
def er_sterkt_passord(passord):
    sterkt = True

    if len(passord) < 8:
        sterkt = False

    has_num = False
    has_upper = False
    for char in passord:
        if char.isdigit():
            has_num = True

        if char.isupper():
            has_upper = True

    if not(has_num and has_upper):
        sterkt = False

    return sterkt

print(er_sterkt_passord("hemmelig"))
print(er_sterkt_passord("Hemmelig"))
print(er_sterkt_passord("Hemmelig1"))
