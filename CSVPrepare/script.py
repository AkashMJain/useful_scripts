'''

filepath = 'shuf1.csv'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:

        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1
'''
filepath = 'shuf1.csv'
count = 0
newfile = 'newfile.csv'

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    file = open(newfile, 'w')
    file.write('emotion,pixels,Usage\n')
    while line:
        if count == 1:
            if cnt < 408:
                file.write(line.strip() + ',Training\n')
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
            elif cnt > 408 and cnt < 460:
                file.write(line.strip() + ',PublicTest\n')
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
            else:
                file.write(line.strip() + ',PrivateTest\n')
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1

        else:
            line = fp.readline()
            cnt += 1
            count = 1
