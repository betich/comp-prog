cid = str(input())
id = [int(i) for i in cid]
checksum = (11 - (13 * id[0] + 12 * id[1] + 11 * id[2] +
            10 * id[3] + 9 * id[4] + 8 * id[5] + 7 * id[6] + 6 * id[7] + 5 * id[8] + 4 * id[9] + 3 * id[10] + 2 * id[11]) % 11) % 10
print(cid[0:1], cid[1:5], cid[5:10], cid[10:12], checksum)
