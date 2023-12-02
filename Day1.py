f = open("Day1.txt", "r")
sum = 0;

for line in f:
    first = ""
    last = ""
    for c in line:
        if c.isdigit():
            if(first == ""):
                first = str(c)
                last =  str(c)
            else:
                last = str(c)
    sum += int(first + last)
print(sum)
