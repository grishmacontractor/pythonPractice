# -------------------------functions
def avrg(first, *rests):
    return (first+ sum(rests))

print(avrg(1, 2))
print(avrg(1, 2, 3))
print(avrg(1, 2, 3, 4))