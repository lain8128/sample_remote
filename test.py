input_dict = {}

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if ':' in line:
            input_dict[int(line.split(':')[0])] = line.split(':')[1].rstrip()
        else:
            m = int(line.rstrip())

sorted_input = {}
for k, v in sorted(input_dict.items(), key=lambda x: x[0]):
    sorted_input[k] = v

for i, s in sorted_input.items():
    if m % i == 0:
        print(s)
