import string
line1= "PWJJMA"
line_2= """PWJJMA:[8]
IT DTZ MFAJ FS NIJF KTW[5]
GEPZMR:[4]
NDJG EGDYTRI NTI?[15]
TU, O'S CGOZOTM LU OTYVOXGZOUT.[6]
BZKUHM:[25]
ZPV DBO'U KVTU UVSO PO[1]
APCYRGTGRW JGIC Y DYSACR.[24]
HXD QJEN CX KN RW CQN[9]
VMKLX QSSH.[4]
YFSSVJ:[17]
BMFY RTTI NX YMFY?[5]
XVGQDI:[21]
GVNO HDIPOZ KVIDX.[21]"""

lines=line_2.count("\n") + 1

listed = []
numbers = []
words = []

splitted_n = line_2.split("[")
for i in splitted_n:
    i= i.replace("]","")
    i = i.replace(":","")
    i= i.replace(" ","")
    s = i.split("\n")
    listed.append(s)

for x in range(1,len(listed)):
    numbers.append(listed[x][0])
    continue

words.append(listed[0][0])
for x in range(1,(len(listed)-1)):
    words.append(listed[x][1])
    continue

ABC = []
for i in string.ascii_uppercase:
    ABC.append(i)

for a in range(len(words)):
    g = int(numbers[a])
    for b in words[a]:
        for i in range(len(ABC)):
            if b == ABC[i]:
                print(ABC[i-g], end= "")
    print()
