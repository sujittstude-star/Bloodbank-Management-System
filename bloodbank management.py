import pickle
def create():
    f=open("BloodBank.dat","wb")
    ans="y"
    dets=[]
    while ans=="y":
        doid=int(input("Enter donor id-"))
        nm=input("Enter donor's name-")
        add=input("Enter donor's address-")
        phno=int(input("Enter donor's phoneno-"))
        bg=input("Enter donor's blood group-")
        gen=input("Enter donor's gender-")
        dob=input("Enter donor's date of birth-")
        ldb=input("Enter last donation date-")
        mh=input("Enter donor's medical history-")
        adhid=int(input("Enter adhar id-"))
        dets+=[[doid,nm,add,phno,bg,gen,dob,ldb,mh,adhid]]
        pickle.dump(dets,f)
        ans=input("do u want to continue(y/n)-")
        if ans in "Nn":
            break
    f.close()
def append():
    f=open("BloodBank.dat","ab")
    ans="y"
    dets=[]
    while ans=="y":
        doid=int(input("Enter donor id-"))
        nm=input("Enter donor's name-")
        add=input("Enter donor's address-")
        phno=int(input("Enter donor's phoneno-"))
        bg=input("Enter donor's blood group-")
        gen=input("Enter donor's gender-")
        dob=int(input("Enter donor's date of birth-"))
        ldb=int(input("Enter last donation date-"))
        mh=input("Enter donor's medical history-")
        adhid=int(input("Enter adhar id-"))
        dets+=[doid,nm,add,phno,bg,gen,dob,ldb,mh,adhid]
        pickle.dump(dets,f)
        ans=input("do u want to continue(y/n)-")
        if ans in "Nn":
            break
    f.close()
def display():
    f=open("BloodBank.dat","rb")
    d=pickle.load(f)
    print(d)
    f.close()
def srch_dnrid():
    sdoid=int(input("Enter donor id to search"))
    try:
        with open("BloodBank.dat","rb")as f:
            while True:
                d=pickle.load(f)
                if d[0]==sdoid:
                    print("donor id-",d[0])
                    print("name-",d[1])
                    print("address-",d[2])
                    print("phone no-",d[3])
                    print("blood group-",d[4])
                    print("gender-",d[5])
                    print("date of birth-",d[6])
                    print("last donation date-",d[7])
                    print("Medical history-",d[8])
                    print("adhar id-",d[9])
                    break
    except EOFError:
        print("Record not found")

def srch_nm():
    sdoid=int(input("Enter donor name to search"))
    try:
        with open("BloodBank.dat","rb")as f:
            while True:
                d=pickle.load(f)
                if d[1]==sdoid:
                    print("donor id-",d[0])
                    print("name-",d[1])
                    print("address-",d[2])
                    print("phone no-",d[3])
                    print("blood group-",d[4])
                    print("gender-",d[5])
                    print("date of birth-",d[6])
                    print("last donation date-",d[7])
                    print("Medical history-",d[8])
                    print("adhar id-",d[9])
                    break
    except EOFError:
        print("Record not found")
def srch_adhrid():
    sdoid=int(input("Enter donor adhar id to search"))
    try:
        with open("BloodBank.dat","rb")as f:
            while True:
                d=pickle.load(f)
                if d[9]==sdoid:
                    print("donor id-",d[0])
                    print("name-",d[1])
                    print("address-",d[2])
                    print("phone no-",d[3])
                    print("blood group-",d[4])
                    print("gender-",d[5])
                    print("date of birth-",d[6])
                    print("last donation date-",d[7])
                    print("Medical history-",d[8])
                    print("adhar id-",d[9])
                    break
    except EOFError:
        print("Record not found")
def srch_phnno():
    sdoid=int(input("Enter donor's phone number to search"))
    try:
        with open("BloodBank.dat","rb")as f:
            while True:
                d=pickle.load(f)
                if d[3]==sdoid:
                    print("donor id-",d[0])
                    print("name-",d[1])
                    print("address-",d[2])
                    print("phone no-",d[3])
                    print("blood group-",d[4])
                    print("gender-",d[5])
                    print("date of birth-",d[6])
                    print("last donation date-",d[7])
                    print("Medical history-",d[8])
                    print("adhar id-",d[9])
                    break
    except EOFError:
        print("Record not found")
def cnt_all_rec():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    print("number of records in the Blood bank are-", len(fr))
    f.close()
def cnt_bld_grp():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    s=input("enter blod group to be counted-")
    c=0
    for i in fr:
        if i[4]==s:
            c+=1
    print("total number of blood group", s,"present is", c)
    f.close()
def cnt_gndr():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    s=input("enter Gender to be counted-")
    c=0
    for i in fr:
        if i[5]==s:
            c+=1
    print("total number of",s,"gender is",c)
    f.close()
def edt_rec():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    s=int(input("enter record to be edited-"))
    l=[]
    for i in range(len(fr)):
        if i!=s:
            l+=[fr[i]]
        elif i==s:
            newid=int(input("enter new donor id-"))
            newname=input("enter new donor name-")
            newadd=eval(input("enter new donor address-"))
            newphno=int(input("enter new donor phone no.-"))
            newbldgrp=input("enter new donor blood group-")
            newgndr=input("enter new gender-")
            newdob=float(input("enter new date of birth-"))
            newdntdat=float(input("enter new donation date-"))
            newmedhstry=input("enter new medical history-")
            newadhrid=int(input("enter new adhaar id-"))
            l+=[[newid,newname,newadd,newphno,newbldgrp,newgndr,newdob,newdntdat,newmedhstry,newadhrid]]
    f.close()
    f=open("BloodBank.dat",'wb')
    pickle.dump(l,f)
    f.close()
def edt_dnrid():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    s=int(input("enter donor id to be edited-"))
    l=[]
    for i in fr:
        if i[0]!=s:
            l+=[i]
        elif i[0]==s:
            newid=int(input("enter new donor id-"))
            newname=input("enter new donor name-")
            newadd=eval(input("enter new donor address-"))
            newphno=int(input("enter new donor phone no.-"))
            newbldgrp=input("enter new donor blood group-")
            newgndr=input("enter new gender-")
            newdob=float(input("enter new date of birth-"))
            newdntdat=float(input("enter new donation date-"))
            newmedhstry=input("enter new medical history-")
            newadhrid=int(input("enter new adhaar id-"))
            l+=[[newid,newname,newadd,newphno,newbldgrp,newgndr,newdob,newdntdat,newmedhstry,newadhrid]]
    f.close()
    f=open("BloodBank.dat",'wb')
    pickle.dump(l,f)
    f.close()
def edt_phno():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    s=int(input("enter phone no. to be edited-"))
    l=[]
    for i in fr:
        if i[3]!=s:
            l+=[i]
        elif i[3]==s:
            newid=int(input("enter new donor id-"))
            newname=input("enter new donor name-")
            newadd=eval(input("enter new donor address-"))
            newphno=int(input("enter new donor phone no.-"))
            newbldgrp=input("enter new donor blood group-")
            newgndr=input("enter new gender-")
            newdob=float(input("enter new date of birth-"))
            newdntdat=float(input("enter new donation date-"))
            newmedhstry=input("enter new medical history-")
            newadhrid=int(input("enter new adhaar id-"))
            l+=[[newid,newname,newadd,newphno,newbldgrp,newgndr,newdob,newdntdat,newmedhstry,newadhrid]]
    f.close()
    f=open("BloodBank.dat",'wb')
    pickle.dump(l,f)
    f.close()
def insrt_rec():
    f=open("BloodBank.dat",'rb')
    fr=pickle.load(f)
    n=int(input("enter record no.-"))
    l=[]
    for i in range(len(fr)):
        if i==n:
            dnrid=int(input("enter donor id-"))
            name=input("enter donor name-")
            add=eval(input("enter donor address-"))
            phno=int(input("enter donor phone no.-"))
            bldgrp=input("enter donor blood group-")
            gndr=input("enter gender-")
            dob=float(input("enter date of birth-"))
            dntdat=float(input("enter donation date-"))
            medhstry=input("enter medical history-")
            adhrid=int(input("enter adhaar id-"))
            l+=[[dnrid,name,add,phno,bldgrp,gndr,dob,dntdat,medhstry,adhrid]]
        else:
            l+=[fr[i]]
    f.close()
    f=open("BloodBank.dat",'wb')
    pickle.dump(l,f)
    f.close()
def insrt_aftdnrid():
    f=open("BloodBank.dat",'rb+')
    fr=pickle.load(f)
    ctr=0
    s=int(input("enter donor id-"))
    l=[]
    for i in fr:
        ctr+=1
        if i[0]==n:
            dnrid=int(input("enter donor id-"))
            name=input("enter donor name-")
            add=eval(input("enter donor address-"))
            phno=int(input("enter donor phone no.-"))
            bldgrp=input("enter donor blood group-")
            gndr=input("enter gender-")
            dob=float(input("enter date of birth-"))
            dntdat=float(input("enter donation date-"))
            medhstry=input("enter medical history-")
            adhrid=int(input("enter adhaar id-"))
            l+=[[dnrid,name,add,phno,bldgrp,gndr,dob,dntdat,medhstry,adhrid]]
            fr.insert(ctr-1,l)
            f.seek(0)
            pickle.dump(fr,f)
    f.close()
def insrt_bfrdnrid():
    f=open("BloodBank.dat",'rb+')
    fr=pickle.load(f)
    ctr=0
    n=int(input("enter donor id-"))
    l=[]
    for i in fr:
        ctr+=1
        if i[0]==n:
            dnrid=int(input("enter donor id-"))
            name=input("enter donor name-")
            add=eval(input("enter donor address-"))
            phno=int(input("enter donor phone no.-"))
            bldgrp=input("enter donor blood group-")
            gndr=input("enter gender-")
            dob=float(input("enter date of birth-"))
            dntdat=float(input("enter donation date-"))
            medhstry=input("enter medical history-")
            adhrid=int(input("enter adhaar id-"))
            l+=[[dnrid,name,add,phno,bldgrp,gndr,dob,dntdat,medhstry,adhrid]]
            fr.insert(ctr,l)
            f.seek(0)
            pickle.dump(fr,f)
    f.close()
def del_recno():
    f=open("BloodBank.dat",'rb')
    s=int(input("enter record to be deleted-"))
    fr=pickle.load(f)
    l=[]
    found=0
    for i in range(len(fr)):
        if i==s:
            found=1
        else:
            l+=[i]
    f.close()
    if found==1:
        f=open("BloodBank.dat",'wb')
        pickle.dump(l,f)
        f.close()
    else:
        print("no such record")
def del_dnrid():
    f=open("BloodBank.dat",'rb')
    s=int(input("enter donor id to be deleted-"))
    fr=pickle.load(f)
    l=[]
    found=0
    for i in fr:
        if i[0]==s:
            found=1
        else:
            l+=[i]
    f.close()
    if found==1:
        f=open("BloodBank.dat",'wb')
        pickle.dump(l,f)
        f.close()
    else:
        print("no such record")
def del_nam():
    f=open("BloodBank.dat",'rb')
    s=int(input("enter name to be deleted-"))
    fr=pickle.load(f)
    l=[]
    found=0
    for i in fr:
        if i[1]==s:
            found=1
        else:
            l+=[i]
    f.close()
    if found==1:
        f=open("BloodBank.dat",'wb')
        pickle.dump(l,f)
        f.close()
    else:
        print("no such record")
while True:
    print("1)Create 2)Append 3)Display all 4)Search on 5)Count 6)Edit 7)Insert 8) Delete")
    m=int(input("enter choice-"))
    if m==1:
        create()
    elif m==2:
        append()
    elif m==3:
        display()
    elif m==4:
        print("1-Donor id 2-Name 3-Aadhar id 4-Phone no")
        n=int(input("enter choice-"))
        if n==1:
            srch_dnrid()
        elif n==2:
            srch_nm()
        elif n==3:
            srch_adhrid()
        elif n==4:
            srch_phnno()
    elif m==5:
        print("1-All records 2-Blood group 3-Gender")
        n=int(input("enter choice-"))
        if n==1:
            cnt_all_rec()
        elif n==2:
            cnt_bld_grp()
        elif n==3:
            cnt_gndr()
    elif m==6:
        print("1-record no 2-donor id 3-phone no")
        n=int(input("enter choice-"))
        if n==1:
            edt_rec()
        elif n==2:
            edt_dnrid()
        elif n==3:
            edt_phno()
    elif m==7:
        print("1-record no 2-after donor id 3-before donor id")
        n=int(input("enter choice-"))
        if n==1:
            insrt_rec()
        elif n==2:
            insrt_aftdnrid()
        elif n==3:
            insrt_bfrdnrid()
    elif m==8:
        print("1-record no 2-donor id 3-name")
        n=int(input("enter choice-"))
        if n==1:
            del_recno()
        elif n==2:
            del_dnrid()
        elif n==3:
            del_nam()
