"""
Problem Overview: Network Failure Point:

We have a mesh network connected by routers labeled from 1 to 6 in a directed manner. Write
an algorithm that can detect the routers with the highest number of connections so we might
know which routers will cause a network failure if removed. Multiple connections between the
same routers should be treated as separate connections. A tie for the most number of
connections is possible.

"""


def network(value):
    s = value.split(" -> ")

    arr = []
    arr_new = []
    yo = []
    final = ""
    for i in range(0, len(s)):
        if i == 0:
            list = [s[0], 0, 1, 1]
            arr.append(list)
            arr_new.append(s[0])
        elif i == (len(s) - 1):
            if s[i] not in arr_new:
                list = [s[i], 1, 0, 1]
                arr.append(list)
                arr_new.append(s[i])

                break
            elif s[i] in arr_new:
                for j in range(0, len(arr)):
                    if s[i] == arr[j][0]:
                        arr[j][1] += 1
                        arr[j][3] += 1

                        break

        elif s[i] not in arr_new:

            list = [s[i], 1, 1, 2]
            arr.append(list)
            arr_new.append(s[i])
        elif s[i] in arr_new:
            for j in range(0, len(arr)):
                if s[i] == arr[j][0]:
                    arr[j][1] += 1
                    arr[j][2] += 1
                    arr[j][3] += 2

    for i in range(0, len(arr)):
        yo.append(arr[i][3])

    t = max(yo)
    for i in range(0, len(arr)):
        if t == arr[i][3]:
            final += str(arr[i][0]) + ","
    print(final[:-1])
    return final[:-1]


assert network("1 -> 2 -> 3 -> 5 -> 2 -> 1") == "2"
assert network("1 -> 3 -> 5 -> 6 -> 4 -> 5 -> 2 -> 6") == "5"
assert network("2 -> 4 -> 6 -> 2 -> 5 -> 6") == "2,6"
