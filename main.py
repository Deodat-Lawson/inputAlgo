# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputL = pd.read_csv('LBN_Buddy_Registration_Form_(Su2023-06-19_07_29_01.csv').values.tolist()
    ouput = open('out.txt','w')

    print(len(inputL))
    print(len(inputL[0]))
    for i in range(0,len(inputL)):
        for j in range(0, len(inputL[0])):
            strWithOutNewLines = str(inputL[i][j]).replace('\n',' ')
            ouput.write(''+ strWithOutNewLines + '\n')
    ouput.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
