import re

file = open("data_raw.csv", "r")
out = open("output", "w")

for line in file:
    if len(re.findall("[-][0][1][\"]", line)) > 0:
        out.write(re.sub("[\"][\S]+[;]", "", line))

file.close()
out.close()
