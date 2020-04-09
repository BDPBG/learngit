class Curriculum:
    def __init__(self):
        self.number = 1001
        self.name = 'Python'
        self.teacher = "小明"
        self.__address = "s教学楼4002室"
    def __str__(self):
        return """
        课程编号：%d   
        课程名称：%s   
        任课教师：%s   
        上课地点：%s"""%(self.number,self.name,self.teacher,self.__address)
curri = Curriculum()
print(curri)