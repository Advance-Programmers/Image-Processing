n = int(input("tedad aks to pooshe: "))
#Reading Points From Data(i).txt s:
for o in range(n):
    listFile = open('./data/data{}.txt'.format(o),'r')
    a = listFile.read()
    a = list(a.split("\n"))
    #no = Index Of Points
    #nox = X Position Of Points
    #noy = Y Position Of Points
    #noox = X Position Of Border & Important Points
    #nooy = Y Position Of Border & Important Points
    no = []
    nox = []
    noy = []
    noox = []
    nooy = []
    #Making All Array 0:
    for i in range(1000):
        b = 0
        noox.append(b)
        nooy.append(b)
    #Saving X & Y Position & Index From File:
    for i in range(len(a) - 1): 
        cleanedRow = list(a[i].split(','))
        cleanedRow[-1] = cleanedRow[-1].replace('\n','')
        no.append(int(cleanedRow[0]))
        nox.append(int(cleanedRow[1]))
        noy.append(int(cleanedRow[2]))
    listFile.close()
    #Saving Border & Important Points Position:
    noox[30] = nox[30]
    noox[0] = nox[0]
    noox[16] = nox[16]
    noox[24] = nox[24]
    noox[30] = nox[30]
    noox[8] = nox[8]
    noox[19] = nox[19]
    nooy[30] = noy[30]
    nooy[0] = noy[0]
    nooy[16] = noy[16]
    nooy[24] = noy[24]
    nooy[30] = noy[30]
    nooy[8] = noy[8]
    nooy[19] = noy[19]
    #Negasht Be 400 * 400:
    for i in no:
        if 14 <= no[i] <= 16 or 42 <= no[i] <= 47 or 22 <= no[i] <= 26 or 27 <= no[i] <= 30 :
            nox[i] = int(200 + (nox[i] - noox[30]) * (200 / (noox[16] - noox[30])))
            noy[i] = int(200 - (-noy[i] + nooy[30]) * (200 / (-nooy[24] + nooy[30])))

        if 17 <= no[i] <= 21 or 36 <= no[i] <= 41 or 0 <= no[i] <= 2  :
            nox[i] = int(200 - (-nox[i] + noox[30]) * (200 / (noox[30] - noox[0])))
            noy[i] = int(200 - (-noy[i] + nooy[30]) * (200 / (-nooy[19] + nooy[30])))

        if 3 <= no[i] <= 8 or 48 <= no[i] <= 51 or 57 <= no[i] <= 59 or 60 <= no[i] <= 61 or no[i] == 67 or 31 <= no[i] <= 33 or no[i] == 62 or no[i] == 66:
            nox[i] = int(200 - (-nox[i] + noox[30]) * (200 / (noox[30] - noox[0])))
            noy[i] = int(200 + (noy[i] - nooy[30]) * (200 / (nooy[8] - nooy[30])))

        if 9 <= no[i] <= 13 or 52 <= no[i] <= 56 or 63 <= no[i] <= 65 or 34 <= no[i] <= 35:
            nox[i] = int(200 + (nox[i] - noox[30]) * (200 / (noox[16] - noox[30])))
            noy[i] = int(200 + (noy[i] - nooy[30]) * (200 / (nooy[8] - nooy[30])))
    #Save Noghat Negasht Shode Dar Points(i).txt s:
    listFile = open('./point/points{}.txt'.format(o),'w')
    for c in no:
        listFile.write(str(no[c]) + "," + str(nox[c]) + "," + str(noy[c]) + '\n')
    listFile.close()