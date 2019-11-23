#每个空行表示，隔离开每次编写的小程序
print("hello world")
a,b=23423,346666#一行中无法a=1,b=2这样直接定义两个变量，或者以列表的方式也
password=int(input("please import password:"))
if password==13156126936:
    c=a+b
    print("""you are genuis!
    that is right.
    you have control the systeam""")#3个引号表示跨多行打印
else:
    print("you are wrong")

for list1 in ["魏","凌","潇"]:
    print(list1)
print()
list=["666"," ","w","t"]
list.pop(1)#此处提供索引，一切索引从0开始,也可直接提供元素
print(list)

#此代码尝试，创建字典，并向其中加入元素，以及调用打印其中的元素
dictionary1={"wlx":13156126936,"lmr":"20001225"}
print(dictionary1["wlx"])#[]内表示要打印的字典中的键的名称，键必须是不可变量
dictionary1["ffe"]=324934983#向字典中加入键值对
print(dictionary1)

#此代码尝试对列表进行排序，并尝试替换其中的指定元素。
a=input("the first name:")
b=input("second name:")
c=input("third name:")#此处代码可简化，可进行五次循环输入，每次用append()函数加入列表
d=input("fourth name:")
e=input("fifth name:")
name_list=[a,b,c,d,e]
for name in name_list:
    print(name,end=" ")#end是强制输出不换行，引号中的空格不加就挤在一起了。
print()#此处是强制换行
print("The names are:",a,b,c,d,e)
print(name_list)
new_list=sorted(name_list)#sorted函数建立的是原列表的副本，并排序
print("排序后为：",new_list)
print("the third name is:",c)
R=int(input("which name you want to replace(1-5):"))#以下三行是替换一个元素,注意此处不能用float函数！，因为R接下来将作为一个索引，须为整数！
rname=input("replace to what:")
name_list.insert(R,rname)#可直接name_list[索引]=，进行替换
name_list.remove(c)#remove可直接提供元素，也可提供变量名，不可索引
print("替换后为：",name_list)

#此代码编写了一个用户可自行加入单词及释义的字典，并且可进行查询
dic2={}
for i in range(0,999):#可以使用很多次
    wt1=input("what you want to use?,a or s:")
    if wt1=="add":
        dic2[input("the word:")]=input("its mean:")
        print("word add!")
    elif wt1=="seek":
         wd=input("what word you want cheak:")
         if wd in dic2.keys():#进行判断是否有这个词
             print("its mean is :",dic2[wd])
         else:
             print("sorry,the word is not in dic")
    else:
             print("not ture")

#此代码块尝试向定义函数中加入参数，且参数被包含在列表中。成功！
ag1,ag2=input("the first argument:"),input("second:")
argument=[ag1,ag2]
def print_name(argument):#无论是否引入这个参数，都不影响后续调用
    print(argument[0],end=(""))#逗号强制不换行已经在3.0版本及以上失效，需用end语句
    print(argument[1])#列表方括号中，只能提供索引，不能提供变量名
print_name(argument)

#此代码建立了一个可以收集个人信息并一一打印的函数。且在要求输入时，针对每次需要提出不同问题的解决上，巧妙地运用了循环，列表的有序性及其索引！
def print_personal_list(plist):
    print(plist[0])
    print(plist[1])
    print(plist[2])
plist=[]
for i in range(0,3):
    questions=["you name:","you address:","you phonenumber:"]
    plist.append(input(questions[i]))#此处想在输入时每次提出不同的问题，那么建立了一个问题字符串列表，以循环中i为索引，每次在input函数中引入不同的问题，非常成功，大大简洁了代码
print_personal_list(plist)

#此代码在原编写时出现了一个巨大错误，详情参见Word文档：global关键字的重点错误！！！
def a(shuilv):
    global price
    price=price*shuilv
    print(price)
price=float(input("laiba:"))
a(99)
print(price)

#学习创建对象时的一个小尝试
class ball:
    def __init__(self,direction1):
        self.direction=direction1
    def bounce(self):#此括号内不能为空
        if self.direction=="down":
            self.direction="up"
myball=ball("down")  # 创建实例时要注意脱离class的缩进
myball.bounce()
print(ball.direction)  # 此处是一个错误，但系统不会报，运行时才有，详情参见文档Python创建对象

#此代码是14章练习题，建立了一个银行账户类，并在其下建立了子类，继承了父类的方法函数，并自定义一个实例，并可自主进行存储操作
class Bookcount:
    def __init__(self):#进行初始化时，可以如下图进行输入，也可直接在创建实例时用参数进行引入。
        self.count_name=input("count name:")
        self.count_number=int(input("the number:"))
        self.balance=float(input("how much dollar:"))
    def get(self):
        want=float(input("how much money do you want:"))
        self.balance=self.balance-want
        print("the balance is",self.balance)
    def deposit(self):
        put_in=float(input("how much do you want to save:"))
        self.balance=self.balance-put_in
        print("the balance is",self.balance)
class Icount(Bookcount):#建立子类时，一定要加上括号主类，才能继承父类的方法，使用
    def __init__(self,lixi):
        Bookcount.__init__(self)#此处只是强行引入其他类的初始化方法，并未有父子类的继承
        self.lixi=lixi
mycount=Icount(0.1)
print(mycount.count_name)
do1=input("waht do you want to do with you account:")#此下处证明子类继承了主类的函数方法
if do1=="get money":
    mycount.get()#调用类中定义的函数时，一定要是已经创建实例，并且使用点操作法。
elif do1=="save money":
    mycount.deposit()
else:
    print("sorry,I do not understand your meaning")

#此代码是模块章节的一个小尝试
import p_name,time,random#引入了自编写的模块，一个小尝试
for i in range(5):
    x=random.randint(1,10)
    p_name.print_name(x)
    time.sleep(1)

#运用pygame初尝试，建立一个小窗口
import pygame
pygame.init()
screen=pygame.display.set_mode([640,480])
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()

#字符串操作函数的多个尝试
list_a="qqq    w r ww e3ee        rrr"
list_b=list_a.split()#此处默认为以空格为分字符，看看面对许多空格是会怎么分
print(list_b)#最终所有空格都被减去
list_c="0".join(list_b)#连接命令join的独特语法
print(list_c)
list_d=list_a.strip("r")#只会删除末尾的r
print(list_d)
list_e=list_a.upper()#全部大写
print(list_e)

#有关制表符和format函数的小尝试
for i8 in range(1,11):
    print("{0:d} \tcheng 8 is:".format(i8),i8*8)#使用\t，制表控制横向距离，使得当i8=10时，cheng也能对齐
for i_8 in range(1,11):
    result=i_8/8
    print("{1:d}\t/ 8={0:.3f}".format(result,i_8))

#对文件写入读取操作的尝试
my_file=open("file2.txt","w")
print("ni hao a",file=my_file)#print写入时会自动结尾时\n。
my_file.write("\nwo hen hao")
my_file.close()#进行关闭后文件才会保存更行内容
my_file1=open("file2.txt","r")
file_1=my_file1.readlines()
print(file_1)

#此代码是尝试建立文本文件，并尝试使用pickle来打包写入文件，重大错误频出，参见文档python读写文件注意点
questions_list=["your name:","your age:","what is your favorite color:"]
answer_list=[]
for i2 in range(3):
    answer_list.append(input(questions_list[i2]))
    xinxi_file=open("xinxi.txt","a")
    print(answer_list[i2],file=xinxi_file)
    xinxi_file.close()
import pickle
my_file2=open("xxanswer.pkl","wb")#pickle写入文件时都是二进制代码，不能再用w,应改用wb
pickle.dump(answer_list,my_file2)
my_file2.close()
my_file3=open("xxanswer.pkl","rb")
print(pickle.load(my_file3))
#本书阅读完毕