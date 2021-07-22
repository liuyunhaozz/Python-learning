import os
import time
import re
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk

data_dict = dict({
    "抽纸" : "CA001",
    "卷纸" : "CA002",
    "牙刷（去包装）" : "CA003",
    "胶带" : "CA004",
    "苹果" : "CD001",
    "水晶梨" : "CD002",
    "哈密瓜" : "CD003",
    "猕猴桃" : "CD004",
    "柚子" : "CD005",
    "香蕉" : "CD006",
    "舒肤佳柠檬清香型香皂（115g）" : "ZA001",
    "瓶装蓝月亮芦荟抑菌洗手液" : "ZA002",
    "黑人双重薄荷牙膏（225g）" : "ZA003",
    "六神花露水（经典花露水、 195ml）" : "ZA004",
    "满趣健婴幼儿童宝宝戏水洗澡玩具" : "ZA005",
    "迪士尼文具盒（EVA 笔袋-美队盾牌版）" : "ZA006",
    "娃哈哈八宝粥（桂圆莲子、 360g）" : "ZB001",
    "老干妈（风味豆豉油制辣椒酱、280g）" : "ZB002",
    "皇冠曲奇饼（454g）" : "ZB003",
    "果珍阳光甜橙壶嘴装（400g）" : "ZB004",
    "绿箭口香糖（薄荷味、 64g）" : "ZB005",
    "公仔面（迷你碗仔面、 海鲜味）" : "ZB006",
    "太平梳打饼干（海苔口、 100g）" : "ZB007",
    "可比克原味薯片（105g）" : "ZB008",
    "乐事 真脆薯条芝士黄油味（电影杯）" : "ZB009",
    "洽洽香瓜子（五香味、 308g）" : "ZB010",
    "罐装雪碧（柠檬味, 330ml）" : "ZC001",
    "罐装可口可乐（330ml）" : "ZC002",
    "罐装芬达（橙味、 330ml）" : "ZC003",
    "罐装红牛（250ml）" : "ZC004",
    "娃哈哈 AD 钙奶（220ml）" : "ZC005",
    "美汁源果粒橙（420ml）" : "ZC006",
    "罐装王老吉（310ml）" : "ZC007",
    "罐装加多宝（310ml）" : "ZC008",
    "瓶装康师傅冰红茶（500ml）" : "ZC009",
    "瓶装康师傅绿茶（500ml）" : "ZC010",
    "康师傅冰糖雪梨（500ml）" : "ZC011",
    "茶派（玫瑰荔枝红茶、 500ml）" : "ZC012",
    "罐装椰树牌椰汁（245ml）" : "ZC013",
    "农夫山泉（550ml）" : "ZC014",
    "娃哈哈（596ml）" : "ZC015",
    "百岁山（570ml）" : "ZC016",
    "怡宝（555ml）" : "ZC017",
    "恒大冰泉（500ml）" : "ZC018",
    "康师傅（550ml）" : "ZC019",
    "今麦郎（500ml）" : "ZC020",
    "昆仑山（510ml）" : "ZC021",
    "雀巢优活（550ml）" : "ZC022",
    "冰露（550ml）" : "ZC023"
})

path = "G:/QQ/2351579300/FileRecv/val/val"
path_txt = "G:/QQ/2351579300/FileRecv/val/txt/"

def textCreate(name, msg):
    full_path = path_txt + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'a')
    file.write(msg)   #msg也就是下面的Hello world!
    file.close()

def textRecreate(name, msg):
    full_path = path_txt + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)   #msg也就是下面的Hello world!
    file.close()

def findNum(file):
    return "".join(re.findall("\d+",file))

def escCallBack():
    exit()

def nxtCallBack(f,window):
    textCreate(f,"END\n")
    window.destroy()
def insCallBack(f,str,num):
    textCreate(f,"Goal_ID="+data_dict[str]+";Num="+num+"\n")
# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            ff = "color" + findNum(f)
            print(findNum(f))
            print(os.path.join(root, f))
            window = tk.Tk()
            window.title(f)
            textRecreate(ff,"START\n")
            im=Image.open(os.path.join(root, f))
            img=ImageTk.PhotoImage(im)
            imLabel=tk.Label(window,image=img).place(x=0, y=0, anchor=tk.NW)
            L1 = tk.Label(text="个")
            L1.place(x=550,y=505,anchor=tk.NW)
            en = tk.Entry(window,show=None)
            en.place(x=400,y=505,anchor=tk.NW)
            var = tk.StringVar()
            ins = tk.Button(text ="添加", command = lambda:insCallBack(ff,var.get(),en.get()))
            ins.place(x=580,y=500,anchor=tk.NW)
            optionMenu = tk.OptionMenu(window, var, *list(data_dict))
            optionMenu.place(x=10,y=500,anchor=tk.NW)
            esc = tk.Button(text ="退出程序", command = escCallBack)
            esc.place(x=10,y=540,anchor=tk.NW)
            nxt = tk.Button(text ="下一张", command = lambda:nxtCallBack(ff,window))
            nxt.place(x=120,y=540,anchor=tk.NW)
            window.geometry("640x580+50+50")
            window.mainloop()
            #print(os.path.join(root, f))

def main():
    walkFile("G:/QQ/2351579300/FileRecv/val/val")


if __name__ == '__main__':
    main()