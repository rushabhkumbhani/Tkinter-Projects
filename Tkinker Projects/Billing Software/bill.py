from tkinter import *
import math, random, os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman",30,"bold"), pady=2).pack(fill=X)

        # Variables 

        # Cosmetics variables

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

        # Grocery variables

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        # Cold Drinks

        self.mazaa=IntVar()
        self.coke=IntVar()
        self.thumbs_up=IntVar()
        self.frooty=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        # Total Product Price and Tax Variables

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        # Customer

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(100000000,999999999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        # Customer Details Frame

        F1=LabelFrame(self.root, text="Customer Details", font=("times new roman",15,"bold"), fg="gold", bg=bg_color, bd=10)
        F1.place(x=0,y=80,relwidth=1) # relative width means it will set its width relatively
        
        cname_lbl=Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=0, padx=20, pady=5)
        cname_txt=Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5)

        cphn_lbl=Label(F1, text="Customer Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=2, padx=20, pady=5)
        cphn_txt=Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5)

        c_bill_lbl=Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=4, padx=20, pady=5)
        c_bill_txt=Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5)

        bill_btn=Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold", activebackground="orange").grid(row=0, column=6, padx=10, pady=10)

        # Cosmetics Frame

        F2=LabelFrame(self.root, text="Cosmetics", font=("times new roman",15,"bold"), fg="gold", bg=bg_color, bd=10)
        F2.place(x=0,y=180, width=325, height=370)
        
        bath_lbl=Label(F2, text="Bath Soap", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt=Entry(F2, width=10, textvariable=self.soap, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=10)

        face_cream_lbl=Label(F2, text="Face Cream", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt=Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        face_wash_lbl=Label(F2, text="Face Wash", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        fash_wash_txt=Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        hair_spray_lbl=Label(F2, text="Hair Spray", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_spray_txt=Entry(F2, width=10, textvariable=self.spray, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10, pady=10)
        
        hair_gel_lbl=Label(F2, text="Hair Gel", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_gel_txt=Entry(F2, width=10, textvariable=self.gel, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10, pady=10)

        body_lotion_lbl=Label(F2, text="Body Lotion", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_lotion_txt=Entry(F2, width=10, textvariable=self.lotion, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10, pady=10)

        # Grocery Frame

        F3=LabelFrame(self.root, text="Grocery", font=("times new roman",15,"bold"), fg="gold", bg=bg_color, bd=10)
        F3.place(x=330,y=180, width=325, height=370)
        
        rice_lbl=Label(F3, text="Rice", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_txt=Entry(F3, width=10, textvariable=self.rice, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=10)

        food_oil_lbl=Label(F3, text="Food Oil", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        food_oil_txt=Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        daal_lbl=Label(F3, text="Daal", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_txt=Entry(F3, width=10, textvariable=self.daal, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        wheat_lbl=Label(F3, text="Wheat", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_txt=Entry(F3, width=10, textvariable=self.wheat, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10, pady=10)
        
        sugar_lbl=Label(F3, text="Sugar", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_txt=Entry(F3, width=10, textvariable=self.sugar, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10, pady=10)

        tea_lbl=Label(F3, text="Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_txt=Entry(F3, width=10, textvariable=self.tea, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10, pady=10)

        # Cold Drinks Frame

        F4=LabelFrame(self.root, text="Cold Drinks", font=("times new roman",15,"bold"), fg="gold", bg=bg_color, bd=10)
        F4.place(x=660,y=180, width=325, height=370)
        
        mazaa_lbl=Label(F4, text="Mazaa", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        mazaa_txt=Entry(F4, width=10, textvariable=self.mazaa, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=10)

        coke_lbl=Label(F4, text="Coke", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        coke_txt=Entry(F4, width=10, textvariable=self.coke, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        thumbs_up_lbl=Label(F4, text="Thumbs Up", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        thumbs_up_txt=Entry(F4, width=10, textvariable=self.thumbs_up, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        frooty_lbl=Label(F4, text="Frooty", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        frooty_txt=Entry(F4, width=10, textvariable=self.frooty, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10, pady=10)
        
        limca_lbl=Label(F4, text="Limca", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_txt=Entry(F4, width=10, textvariable=self.limca, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10, pady=10)

        sprite_lbl=Label(F4, text="Sprite", font=("times new roman",16,"bold"), bg=bg_color, fg="lightgrey").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_txt=Entry(F4, width=10, textvariable=self.sprite, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10, pady=10)

        # Bill Area

        F5=LabelFrame(self.root, bd=10)
        F5.place(x=1000,y=180, width=325, height=370)
        bill_title=Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5, yscrollcommand=scroll_y.set) # yscrollcommand sets scrollbar 
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame

        F6=LabelFrame(self.root, text="Bill Menu", font=("times new roman",15,"bold"), fg="gold", bg=bg_color, bd=10)
        F6.place(x=0,y=560, relwidth=1, height=140)

        m1_lbl=Label(F6, text="Total Cosmetics Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt=Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl=Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt=Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl=Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt=Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl=Label(F6, text="Cosmetics Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt=Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl=Label(F6, text="Groceries Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt=Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl=Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt=Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        button_frame=Frame(F6, bd=7, relief=GROOVE)
        button_frame.place(x=750, width=570, height=105)

        total_button=Button(button_frame, command=self.total, text="Total", bg="cadetblue", activebackground="orange", fg="white", pady=15, width=11, font="arial 12 bold", bd=5).grid(row=0, column=0, padx=5, pady=5)
        generate_bill_button=Button(button_frame, text="Generate Bill", command=self.bill_area, activebackground="orange", bg="cadetblue", fg="white", pady=15, width=11, font="arial 12 bold", bd=5).grid(row=0, column=1, padx=5, pady=5)
        clear_button=Button(button_frame, text="Clear", command=self.clear_data, bg="cadetblue", activebackground="orange", fg="white", pady=15, width=11, font="arial 12 bold", bd=5).grid(row=0, column=2, padx=5, pady=5)
        exit_button=Button(button_frame, text="Exit", command=self.Exit_app, bg="cadetblue", activebackground="orange", fg="white", pady=15, width=11, font="arial 12 bold", bd=5).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_sop=self.soap.get()*40
        self.c_facp=self.face_cream.get()*120
        self.c_fawp=self.face_wash.get()*60
        self.c_spp=self.spray.get()*180
        self.c_gep=self.gel.get()*140
        self.c_lop=self.lotion.get()*180
        self.total_cosmetic_price=float(
            (self.c_sop)+ # price per soap is Rs. 40
            (self.c_facp)+ # price per face_cream is Rs. 120
            (self.c_fawp)+ # price per face_wash is Rs. 60
            (self.c_spp)+ # price per spray is Rs. 180
            (self.c_gep)+ # price per gel is Rs. 140
            (self.c_lop) # price per lotion is Rs. 180
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_rip=self.rice.get()*80
        self.g_fop=self.food_oil.get()*180
        self.g_dap=self.daal.get()*60
        self.g_whp=self.wheat.get()*240
        self.g_sup=self.sugar.get()*45
        self.g_tep=self.tea.get()*150

        self.total_grocery_price=float(
            (self.g_rip)+ # price per kg of rice is Rs. 80
            (self.g_fop)+ # price per kg of food_oil is Rs. 180
            (self.g_dap)+ # price per kg of daal is Rs. 60
            (self.g_whp)+ # price per kg of wheat is Rs. 240
            (self.g_sup)+ # price per kg of sugar is Rs. 45
            (self.g_tep) # price per kg of tea is Rs. 150
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cd_map=self.mazaa.get()*60
        self.cd_cop=self.coke.get()*60
        self.cd_thp=self.thumbs_up.get()*50
        self.cd_frp=self.frooty.get()*45
        self.cd_lip=self.limca.get()*40
        self.cd_spp=self.sprite.get()*60


        self.total_cold_drink_price=float(
            (self.cd_map)+ # price per mazaa is Rs. 60
            (self.cd_cop)+ # price per coke is Rs. 60
            (self.cd_thp)+ # price per thumbs_up is Rs. 50
            (self.cd_frp)+ # price per frooty Rs. 45
            (self.cd_lip)+ # price per limca Rs. 40
            (self.cd_spp) # price per sprite is Rs. 60
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax
                            )
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)  # It will everything index 1.0 till the end
        self.txtarea.insert(END,"Welcome to the Laxmi Agency Retail\n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n===================================")
        self.txtarea.insert(END,f"\n Products\t\tQuantity\t    Price")
        self.txtarea.insert(END,f"\n===================================")
        

    def bill_area(self):

        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product selected")  

        else:
            self.welcome_bill()

            # Cosmetics Condition i.e to not show on the bill if not ordered any Quantity

            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_sop}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.c_facp}")    
            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.c_fawp}")
            if self.spray.get()!=0:
                self.txtarea.insert(END, f"\nSpray\t\t{self.spray.get()}\t\t{self.c_spp}")
            if self.gel.get()!=0:
                self.txtarea.insert(END, f"\nGel\t\t{self.gel.get()}\t\t{self.c_gep}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END, f"\nLotion\t\t{self.lotion.get()}\t\t{self.c_lop}")
            
            # Grocery Condition

            if self.rice.get()!=0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_rip}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.g_fop}")    
            if self.daal.get()!=0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t\t{self.g_dap}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_whp}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_sup}")
            if self.tea.get()!=0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t\t{self.g_tep}")

            # Cold Drinks Condition

            if self.mazaa.get()!=0:
                self.txtarea.insert(END, f"\nMazaa\t\t{self.mazaa.get()}\t\t{self.cd_map}")
            if self.coke.get()!=0:
                self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.cd_cop}")    
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END, f"\nThumbs Up\t\t{self.thumbs_up.get()}\t\t{self.cd_thp}")
            if self.frooty.get()!=0:
                self.txtarea.insert(END, f"\nFrooty\t\t{self.frooty.get()}\t\t{self.cd_frp}")
            if self.limca.get()!=0:
                self.txtarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t\t{self.cd_lip}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.cd_spp}")
            
            self.txtarea.insert(END,f"\n----------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            
            self.txtarea.insert(END,f"\n Total Bill: \t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n----------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END) #From first line till the end we have to get the data
            f1=open("C://Users//DELL//Desktop//Vs Code Python//Tkinker Projects//Billing Software//bills//"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("C://Users//DELL//Desktop//Vs Code Python//Tkinker Projects//Billing Software//bills//"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"C://Users//DELL//Desktop//Vs Code Python//Tkinker Projects//Billing Software//bills//{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear the Screen?")
        if op>0:

            # Cosmetics variables

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            # Grocery variables

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # Cold Drinks

            self.mazaa.set(0)
            self.coke.set(0)
            self.thumbs_up.set(0)
            self.frooty.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # Total Product Price and Tax Variables

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # Customer

            self.c_name=StringVar("")
            self.c_phon=StringVar("")
            self.bill_no=StringVar("")
            x=random.randint(100000000,999999999)
            self.bill_no.set(str(x))
            self.search_bill=StringVar("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop() 