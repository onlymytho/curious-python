import JsonHandler
import pprint

file_path = 'daily_metro/서울메트로 역별 시간대별(일) 승하차 인원 정보 (2013년).json'

datadict = JsonHandler.JsonHandler.OpenJsonFileConvertToDict(file_path)

all_d = len(datadict)
print ("all_d = " + str(all_d))

num = 0

for i in datadict:

    first_d = len(i)
    print ("data " + str(num) + " = " + str(first_d))
    num += 1

    numi = 0
    for ii in i :
        first_d = len(ii)
        print ("data " + str(numi) +"/" + str(num) + " = " + str(first_d))
        numi += 1

        numii = 0
        for iii in ii :
            first_d = len(iii)
            print ("data " + str(numii) + "/" + str(numi) +"/" + str(num) + " = " + str(first_d))
            numi += 1
