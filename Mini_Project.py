import csv as c
import pandas as pd
import numpy as np


def Order(): #หน้าเมนู
    order=["[1]ปีกไก่ออริจินอล","[2]ปีกไก่พริกไทยดำ","[3]ปีกไก่พริกกระเทียม","[4]อกไก่ออริจินอล","[5]อกไก่วิ้งแซบ","[6]อกไก่พริกไทยดำ","[7]อกไก่เทอริยากิ","[8]อกไก่บอนชอน",
           "[9]อกไก่พริกกระเทียม","[10]น่องไก่ออริจินอล","[11]น่องไก่วิ้งแซบ","[12]น่องไก่พริกไทยดำ","[13]น่องไก่เทอริยากิ","[14]น่องไก่บอนชอน","[15]เบอร์เกอร์สเต็กไก่","[16]เบอร์เกอร์ไก่ราดซอสเทอริยากิ",
           "[17]เบอร์เกอร์ไก่พริกไทยดำ","[18]จ้อไก่","[19]นักเก็ต","[20]ไก่ป๊อป"]
    Original=[10,10,10,20,20,20,20,20,20,20,20,20,20,20,40,40,40,20,5,2]
    Cheese=[15,15,15,25,25,25,25,25,25,25,25,25,25,25,50,50,50,25,7,3]
    Pieces=["บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น",
            "บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น","บาท/ชิ้น"]
    print("MENU","\t\t\t\tธรรมดา","\tชีส")
    print("="*50)
    for i in range(20):
        print(order[i],"\t\t\t\t",Original[i],"\t",Cheese[i],"\t",Pieces[i])
    print("="*50)
  
  
def select_order(so): #เลือกเมนู
    selectorder = so
    
    if selectorder == 1 :                           
        order1 = "ปีกไก่ออริจินอล"
        yourorder.append(order1)
    elif selectorder == 2 :
        order2 = "ปีกไก่พริกไทยดำ"
        yourorder.append(order2)
    elif selectorder == 3 :
        order3 = "ปีกไก่พริกกระเทียม"
        yourorder.append(order3)
    elif selectorder == 4 :
        order4 = "อกไก่ออริจินอล"
        yourorder.append(order4)
    elif selectorder == 5 :
        order5 = "อกไก่วิ้งแซบ"
        yourorder.append(order5)
    elif selectorder == 6 :
        order6 = "อกไก่พริกไทยดำ"
        yourorder.append(order6)
    elif selectorder == 7 :
        order7 = "อกไก่เทอริยากิ"
        yourorder.append(order7)
    elif selectorder == 8 :
        order8 = "อกไก่บอนชอน"
        yourorder.append(order8)
    elif selectorder == 9 :
        order9 = "อกไก่พริกกระเทียม"
        yourorder.append(order9)
    elif selectorder == 10 :
        order10 = "น่องไก่ออริจินอล"
        yourorder.append(order10)
    elif selectorder == 11 :
        order11 = "น่องไก่วิ้งแซบ"
        yourorder.append(order11)
    elif selectorder == 12 :
        order12 = "น่องไก่พริกไทยดำ"
        yourorder.append(order12)
    elif selectorder == 13 :
        order13 = "น่องไก่บอนชอน"
        yourorder.append(order13)
    elif selectorder == 14 :
        order14 = "น่องไก่พริกกระเทียม"
        yourorder.append(order14)
    elif selectorder == 15 :
        order15 = "เบอร์เกอร์สเต็กไก่"
        yourorder.append(order15)
    elif selectorder == 16 :
        order16 = "เบอร์เกอร์ไก่ราดซอสเทอริยากิ"
        yourorder.append(order16)
    elif selectorder == 17 :
        order17 = "เบอร์เกอร์ไก่พริกไทยดำ"
        yourorder.append(order17)
    elif selectorder == 18 :
        order18 = "จ้อไก่"
        yourorder.append(order18)
    elif selectorder == 19 :
        order19 = "นักเก็ต"
        yourorder.append(order19)
    elif selectorder == 20 :
        order20 = "ไก่ป๊อป"
        yourorder.append(order20)
    return selectorder


def Order_list(so,tl): #รสชาติ,คิดจำนวนเงิน
    selectorder = so
    type_list = tl
       
    if selectorder == 1 and type_list == 1 :
        polist = 10*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 1 and type_list == 2 :
        polist = 15*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 2 and type_list == 1 :
        polist = 10*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 2 and type_list == 2 :
        polist = 15*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)

    elif selectorder == 3 and type_list == 1 :
        polist = 10*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 3 and type_list == 2 :
        polist = 15*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 4 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 4 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 5 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 5 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 6 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 6 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)

    elif selectorder == 7 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 7 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)

    elif selectorder == 8 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 8 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)

    elif selectorder == 9 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)        
    elif selectorder == 9 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 10 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 10 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 11 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 11 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 12 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 12 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 13 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 13 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 14 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 14 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 15 and type_list == 1 :
        polist = 40*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 15 and type_list == 2 :
        polist = 50*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 16 and type_list == 1 :
        polist = 40*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 16 and type_list == 2 :
        polist = 50*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 17 and type_list == 1 :
        polist = 40*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 17 and type_list == 2 :
        polist = 50*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 18 and type_list == 1 :
        polist = 20*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 18 and type_list == 2 :
        polist = 25*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 19 and type_list == 1 :
        polist = 5*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 19 and type_list == 2 :
        polist = 7*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
        
    elif selectorder == 20 and type_list == 1 :
        polist = 2*OPP
        yourtype.append(polist)
        vol = "ธรรมดา"
        yourvolume.append(vol)       
    elif selectorder == 20 and type_list == 2 :
        polist = 3*OPP
        yourtype.append(polist)
        vol = "ชีส"
        yourvolume.append(vol)
   
   
def tang_ton(): # เงินทอน
    money       = tang-sum(yourtype)
    money       = int(money)
    
    print("เงินทอนของคุณ : ", money ,"บาท")
    b1000   = (money//1000)
    tangton.append(b1000)
    b500    = (money%1000//500)
    tangton.append(b500)
    b100    = (money%1000//100)-(b500*5)
    tangton.append(b100)
    b50     = (money%100//50)
    tangton.append(b50)
    b20     = ((money%100-b50*50)//20)
    tangton.append(b20)
    b10     = ((money%100-b50*50-b20*20)//10)
    tangton.append(b10)
    b5      = (money%10//5)
    tangton.append(b5)
    b1      = (money%10//1)-b5*5
    tangton.append(b1)  
    if tangton[0] > 0 :
        print("ธนบัตร 1000 บาท จำนวน :",b1000,"ฉบับ")
    if tangton[1] > 0 :
        print("ธนบัตร 500 บาท จำนวน :",b500,"ฉบับ")
    if tangton[2] > 0 :
        print("ธนบัตร 100 บาท จำนวน :",b100,"ฉบับ")
    if tangton[3] > 0 :
        print("ธนบัตร 50 บาท จำนวน :",b50,"ฉบับ")
    if tangton[4] > 0 :
        print("ธนบัตร 20 บาท จำนวน :",b20,"ฉบับ")
    if tangton[5] > 0 :
        print("เหรียญ 10 บาท จำนวน :",b10,"เหรียญ")
    if tangton[6] > 0 :
        print("เหรียญ 5 บาท จำนวน :",b5,"เหรียญ")
    if tangton[7] > 0 :
        print("เหรียญ 1 บาท จำนวน :",b1,"เหรียญ")
        

def comment():
    a = input("แสดงความคิดเห็น : ")
    ment.append(a)
    with open('miniproject.csv', 'w', newline='') as file:
            writer = c.writer(file)
            writer.writerow(ment)
    pd.read_csv('miniproject.csv')
    df = pd.DataFrame(pd.read_csv('miniproject.csv'))
    df = np.transpose(df)
    #com = len(ment)
   # for i in range(com):
     #   print(ment[i])
   
   
tangton    = [] #เก็บข้อมูลราคา
yourtype   = [] #เก็บข้อมูลจำนวน
yourvolume = [] #เก็บข้อมูลรสชาติ
yourorder  = [] #เก็บเมนูลูกค้า
listmenu   = [] #จำนวนการซื้อ
ment = [] #ความคิดเห็น

x = "Y"

while x .upper() in ["Y"] :
 
    print("-"*30,"ไก่ทอด กะต๊ากกะต๊าก","-"*30)
    while True:
        try:
            print("="*50)
            Order()
            so = int(input("กรุณาเลือกเมนู(1-20) : "))
            if so in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] :
                select_order(so)
                print("="*45)
                print("คุณต้องการ ธรรมดา หรือ ชีส")
                print("(1) ธรรมดา")
                print("(2) ชีส")
                break
            else :
                print("กรุณาใส่หมายเลขของเมนูให้ถูกต้อง!!!")
        except:
            print("กรุณาใส่หมายเลขของเมนูให้ถูกต้อง!!!")


    while True :
        try:
            tl = int(input("กรุณาเลือกประเภท(1-2) : "))
            if tl in [1,2] :
                OPP = int(input("จำนวนชิ้นที่ต้องการ : "))
                if OPP >= 1 :
                    listmenu.append(OPP)
                    Order_list(so,tl)
                    print("="*45)
                    break
                elif OPP < 1 :
                    print("กรุณาใส่ตัวเลขให้ถูกต้อง!!!")
            else :
                print("กรุณาใส่ประเภทของเมนูให้ถูกต้อง!!!")
        except:
            print("กรุณาใส่หมายเลขของเมนูให้ถูกต้อง!!!")
            print("คุณต้องการ ธรรมดา หรือ ชีส")
            print("(1) ธรรมดา")
            print("(2) ชีส")

    print("ต้องการเลือกเมนูเพิ่มเติมหรือไม่")
    x = input("กรุณาใส่ตัวอักษร(Y/N) : ")
    while x .upper()not in ["Y","N"]:
            print("ใส่คำสั่งไม่ถูกต้อง")
            x = input("กรุณาใส่ตัวอักษร(Y/N) : ")
    print("="*45)
        
print("No.","\tMANU","\t\t\tNUMBER OF PIECES","\t\t\tPRICE")
for i in range(len(yourorder)):
    print(i+1,"\t",yourorder[i],"(",yourvolume[i],")","\t\t\t",listmenu[i],"ชิ้น","\t\t\t",yourtype[i],"บาท")
print("ยอดเงินรวม ",sum(yourtype)," บาท")

while True :
    try:
        tang = int(input("กรุณาใส่จำนวนเงิน : "))
        if tang >= sum(yourtype) :
            tang_ton()
            break
        else :
            print("กรุณาใส่จำนวนเงินให้ถูกต้อง!!!")
            print("="*45)
            print("ยอดเงินรวม ",sum(yourtype)," บาท")
    except:
        print("กรุณาใส่จำนวนเงินให้ถูกต้อง!!!")
        print("="*45)

comment()
print("ขอบคุณที่อุดหนุน")