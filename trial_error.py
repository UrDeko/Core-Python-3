coordinates = eval("(3, 4), (4, 5)")
for v, k in coordinates:
    print(f"{v}: {k}")

txt = "/Users/denisstratiev/Documents/Work/Python/simple_file.txt"
with open(txt, "r") as f:
    line = f.readline()
    while (line != ""):
        print(line)
        line = f.readline()

numbers = list("345")
numbers = [int(x) for x in numbers]
print(numbers)

w1 = "okey"
w2 = str(w1)
w2 = "b3"
print(w2, w1, sep = ", ")

seq = ["e", "br"]
print(max(seq, key=len))

for x, y in enumerate(seq):
    print(f"{x}: {y}")