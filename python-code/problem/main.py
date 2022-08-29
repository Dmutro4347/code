b = []

with open('/usr/share/doc/picom/picom.conf.example', 'r') as fl:
    for i in fl.readlines():
        if i[0] != '#':
            print(i)
for i in range(1, 11):
    print(i)

    # asdas