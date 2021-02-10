# QUIZ) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.


# - X주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시요


# 조건 : 파일명은 '1주차.txt' '2주차.txt', ... 형식으로 만듭니다.



#1차시도 성공
for i in range(1,4) :
    with open("{0}주차.txt".format(i), "w",encoding="utf8") as report :
        
        print("-{0}주차 주간보고 입니다.".format(i))
        team = input("부서명을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        key = input("업무요약을 입력하세요: ")


        report.write("{0}주차 주간보고-\n".format(i))
        report.write("부서 : {0}\n".format(team))
        report.write("이름 : {0}\n".format(name))
        report.write("업무요약 : {0}\n".format(key))


## 답지

for i in range(1,2) :
    with open(str(i) + "주차.txt", "w",encoding="utf8") as report_file :
        report_file.write( "- {0} 주차 주간보고 -".format(i))
        report_file.write( "\n부서 : ")
        report_file.write( "\n이름 : ")
        report_file.write( "\n업무요약 : ")
