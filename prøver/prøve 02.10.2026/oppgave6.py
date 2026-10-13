temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]

# a)
print(f"Det er {len(temperaturer)} målinger")
print(f"Den første målingen er {temperaturer[0]} og den siste målingen er {temperaturer[-1]}")

# b)
avg = round(sum(temperaturer)/len(temperaturer), 2)
print(f"Gjennomsnittstemperaturen er {avg}")

# c)
dager_under_null = 0
for temp in temperaturer:
    if temp < 0:
        dager_under_null += 1

print(f"Dager under null grader er {dager_under_null}")

# d)
dager_over_null = []
for temp in temperaturer:
    if temp > 0:
        dager_over_null.append(temp)

dager_over_null = sorted(dager_over_null, reverse=True)

print(f"Temperaturene på dagene over 0 grader var {dager_over_null}")
