import re
import sys

InpProgram = sys.argv[1]
program = os.path.abspath(os.path.join("..", "programs", f"{InpProgram}.psep"))
lines = []

with open(program, "r") as file:
    for line in file:
        lines.append(line.strip())

processedlines = []

for line in lines:
    line = re.sub(r'2(?=[a-zA-Z])', '', line)
    line = re.sub(r'\b2\b', ' ', line)
    processedlines.append(line)

out = ''

for char in processedlines:
    out += char

print(out)