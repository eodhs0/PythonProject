from tkinter import *
import pickle

#-*- coding: utf-8 -*-

window = Tk()
window.title("StudentManager")

info_display = []
db = [] # 데이터 저장할 리스트
dbName = [] # 이름 저장(db안에)
dbCnt = 0
studentID = 0

# click function
def click(BT):
    global db
    global dbCnt
    global studentID

    def isNumber(s):
        try:
            temp = float(s)
            return True
        except ValueError:
            return False
    
    if BT == '추가':
        judge = 1 #0이면 추가 오류
        if name_display.get() == "": # 공백
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[4])
            judge = 0
            errorString = "[추가실패] 이름이 공백입니다."
            raise
        if info_display[0].get() == "": # 공백
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[4])
            judge = 0
            errorString = "[추가실패] 이름이 공백입니다."
            raise
        for a in range(0, dbCnt):
            if name_display.get() == db[a][1]: # 같은이름이 존재한다면
                state_display.delete(0.0, END)
                state_display.insert(END, state_list[5])
                judge = 0
                errorString = "[추가실패] 같은 이름이 존재합니다."
                break
        if isNumber(info_display[0].get()) == False: # 점수에 숫자가 아닐때 
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[6])
            judge = 0
            errorString = "[추가실패] 점수가 숫자가 아닙니다."
            raise

        if eval(info_display[0].get()) < 0:
            errorString = "[추가실패] 점수가 음수입니다."
            judge = 0
            raise
        if judge == 1:
            dbCnt = dbCnt + 1
            studentID = studentID + 1
            db.append([studentID, name_display.get(), info_display[0].get()])        
            s=str(db[dbCnt-1][0])+"\t"+str(db[dbCnt-1][1])+"\t"+ str(float(db[dbCnt-1][2]))+"\n"       
            dataPrint_display.insert(END, s)
            name_display.delete(0, END) # 저장 후 초기화
            info_display[0].delete(0, END) # 저장 후 초기화
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[0])
        else:
            state_display.delete(0.0, END)
            state_display.insert(END, errorString)
        
    elif BT == '삭제':
        try:
            if not isNumber(info_display[1].get()):
                raise
            
            if dbCnt >= 1:
                removeNum = eval(info_display[1].get()) # get은 문자로 받아오니까 eval로 숫자로 변형
                for check in range(0, dbCnt):
                    if removeNum == db[check][0]:
                       removeNum = check
                       break
                del db[removeNum]
                dataPrint_display.delete(1.0, END)
                for cnt in range(0,dbCnt-1):
                    S=str(db[cnt][0])+"\t"+str(db[cnt][1])+"\t"+ str(float(db[cnt][2]))+"\n"
                    dataPrint_display.insert(END, S)   
                dbCnt = dbCnt - 1
                state_display.delete(0.0, END)
                state_display.insert(END, state_list[1])
            else:
                raise
        except:
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[7])
                
    elif BT == '저장':
        dbCnt = dbCnt
        fileName = info_display[2].get()+'.txt'
        try:
            if fileName.find('\\') != -1:
                raise
            if fileName.find('/') != -1:
                raise
            if fileName.find(':') != -1:
                raise
            if fileName.find('?') != -1:
                raise
            if fileName.find('"') != -1:
                raise
            if fileName.find('<') != -1:
                raise
            if fileName.find('>') != -1:
                raise
            if fileName.find('|') != -1:
                raise
            else:
                f = open(fileName, 'wb')
                pickle.dump(db, f)
                f.close()
                state_display.delete(0.0, END)
                state_display.insert(END, state_list[2]+" (파일이름: "+fileName+")")           
        except:
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[8])
        
    elif BT == '열기':
        try:
            fileName = info_display[3].get()+'.txt'
            f = open(fileName, 'rb')
            dataTemp = pickle.load(f)
            db = dataTemp
            dataPrint_display.delete(1.0, END) # 화면 지우기
        
            dbCnt = len(dataTemp)
            studentID = dbCnt
            for cnt in range(0, dbCnt):
                S = str(db[cnt][0])+"\t"+str(dataTemp[cnt][1])+"\t"+str(float(dataTemp[cnt][2]))+"\n"
                dataPrint_display.insert(END, S)
        
                state_display.delete(0.0, END)
                state_display.insert(END, state_list[3] + " (파일이름: "+fileName+")")
        except:
            state_display.delete(0.0, END)
            state_display.insert(END, state_list[9] + " (파일이름: "+fileName+")")

    # 정렬 #
    
    elif BT == '번호순':
        state_display.delete(0.0, END)
        dataPrint_display.delete(1.0, END)
        for cnt in range(0,dbCnt):
            S=str(db[cnt][0])+"\t"+str(db[cnt][1])+"\t"+ str(float(db[cnt][2]))+"\n"
            dataPrint_display.insert(END, S)

    elif BT == '이름순':
        state_display.delete(0.0, END)
        dbTemp = []
        def valueSort(db):
            return db[1]
        dbTemp = sorted(db, reverse = False, key = valueSort)
        dataPrint_display.delete(1.0, END)
        for cnt in range(0,dbCnt):
            S=str(dbTemp[cnt][0])+"\t"+str(dbTemp[cnt][1])+"\t"+ str(float(dbTemp[cnt][2]))+"\n"
            dataPrint_display.insert(END, S)

    elif BT == '점수내림차순':
        state_display.delete(0.0, END)
        def valueSort(db):
            return db[2]
        dbTemp = sorted(db, reverse = True, key = valueSort)
        dataPrint_display.delete(1.0, END)
        for cnt in range(0,dbCnt):
            S=str(dbTemp[cnt][0])+"\t"+str(dbTemp[cnt][1])+"\t"+ str(float(dbTemp[cnt][2]))+"\n"
            dataPrint_display.insert(END, S)

    elif BT == '점수오름차순':
        state_display.delete(0.0, END)
        def valueSort(db):
            return db[2]
        dbTemp = sorted(db, reverse = False, key = valueSort)
        dataPrint_display.delete(1.0, END)
        for cnt in range(0,dbCnt):
            S=str(dbTemp[cnt][0])+"\t"+str(dbTemp[cnt][1])+"\t"+ str(float(dbTemp[cnt][2]))+"\n"
            dataPrint_display.insert(END, S)

# name Frame
name_pad = Frame(window)
name_pad.grid(row=0, column=0, sticky=N)
Label(name_pad, text="이름: ") \
    .grid(row=0, column=0, sticky=N)
name_display = Entry(name_pad, width=20, bg="light green")
name_display.grid(row=0, column=1)

## info Frame
info_pad = Frame(window)
info_pad.grid(row=0, column=1, sticky=E)

info_list = {'score': ["점수: ", 7, "light green"], \
             'number': ["번호: ", 5, 'light green'], \
             'fileName1': ['파일이름:', 20, 'light blue'], \
             'fileName2': ['파일이름:', 20, 'light blue'],
             }
info_name_list = ('score', 'number', 'fileName1', 'fileName2')
rowNum = 0
for key in info_name_list:
    Label(info_pad, text=info_list[key][0]) \
        .grid(row=rowNum, column=5, sticky=E)
    print(key)
    info_display.append(Entry(info_pad, width=info_list[key][1], \
                         bg=info_list[key][2]))
    info_display[rowNum].grid(row=rowNum, column=7, sticky=W)
    rowNum = rowNum + 1

# function Frame
func_list = ['추가', '삭제', '저장', '열기']

rowNum = 0
for btn_text in func_list:
    def cmd(x = btn_text):
        click(x)
    Button(info_pad, text = btn_text, width = 10, command = cmd).grid(row = rowNum, column = 10)
    rowNum = rowNum + 1
rowNum = 0

# sortFunc Frame
sortFunc_pad = Frame(window)
sortFunc_pad.grid(row=1, column=0, columnspan=2)
sort_list = ['번호순', '이름순', '점수내림차순', '점수오름차순']
colNum = 0

for key in sort_list:
    def cmd(x = key):
        click(x)
    if colNum < 2:
        Button(sortFunc_pad, text = key, width = 5, command = cmd).grid(row = 0, column = colNum)
    else:
        Button(sortFunc_pad, text = key, width = 15, command = cmd).grid(row = 0, column = colNum)
        
    colNum = colNum + 1

# dataPrint Frame
dataPrint_pad = Frame(window)
dataPrint_pad.grid(row=2, column=0, columnspan=2)
dataPrint_display = Text(dataPrint_pad, width=75, height=10, bg="light yellow")
dataPrint_display.grid(row=2, column=0)

# state Frame
state_pad = Frame(window)
state_pad.grid(row=3, column=0, columnspan=2)
state_display = Text(state_pad, width=75, height=1, bg="red")
state_display.grid(row=3, column=0)
state_list = ['성공적으로 추가하였습니다.', '성공적으로 삭제하였습니다.',
              '성공적으로 저장하였습니다', '성공적으로 파일을 읽었습니다.',
              '[추가실패] 공백입니다.', '[추가실패] 동일한 이름이 존재합니다',
              '점수가 숫자가 아닙니다.', '삭제에 실패하였습니다.',
              '파일 저장에 실패하였습니다', '파일 불러오기에 실패하였습니다',
              ]
