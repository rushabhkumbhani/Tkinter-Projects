from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os, shutil

class Sorting_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Application")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="C://Users//DELL//Desktop//Vs Code Python//Tkinker Projects//File Sorting Application//Images//folders.png")
        title = Label(self.root, text="File Sorting Application", image=self.logo_icon,compound=LEFT, padx=30, font=("impact",40), bg="#023548", fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        #---- Section 1 --------------------------------

        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root, text="Select Folder", font=("times new roman",25)).place(x=50, y=100)
        folder_name=Entry(self.root, textvariable=self.var_foldername, font=("times new roman",15), bg="lightyellow", state="readonly").place(x=250, y=100, height=40, width=600)
        btn_browse=Button(self.root, command=self.browse_function, text="Browse", font=("times new roman",15,"bold"), background="#262626", fg="white", activebackground="#262626", activeforeground="white", cursor="hand2").place(x=900, y=95, height=45, width=150)
        hr=Label(self.root, bg="lightgray").place(x=50, y=160, height=2, width=1250)

        #---- Section 2 --------------------------------
        #---- All Extensions ---------------------------

        self.image_extensions=["Image Extensions",".png", ".jpg"]
        self.audio_extensions=["Audio Extensions", ".amr", ".mp3"]
        self.video_extensions=["Video Extensions", ".mp4", ".avi", ".mpe4", ".3gp"]
        self.doc_extensions=["Document Extensions", ".doc", ".xlsx", ".ppt", ".pptx", ".xls", ".pdf", ".zip", ".rar", ".csv", ".txt"]

        self.folders={
            'videos':self.video_extensions,
            'audios':self.audio_extensions,
            'images':self.image_extensions,
            'documents':self.doc_extensions
            }


        lbl_support_ext=Label(self.root, text="Various Supported Extensions", font=("times new roman",25), bg="white").place(x=50, y=170)

        self.image_box=ttk.Combobox(self.root, values=self.image_extensions, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.image_box.place(x=60, y=230, width=270, height=35)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root, values=self.video_extensions, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.video_box.place(x=360, y=230, width=270, height=35)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root, values=self.audio_extensions, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.audio_box.place(x=700, y=230, width=270, height=35)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root, values=self.doc_extensions, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.doc_box.place(x=1010, y=230, width=270, height=35)
        self.doc_box.current(0)

        #---- Section 3 --------------------------------
        #---- All Image Icons ---------------------------

        self.image_icon=PhotoImage(file="C:\\Users\\DELL\\Desktop\\Vs Code Python\\Tkinker Projects\\File Sorting Application\\Images\\images.png")
        self.audio_icon=PhotoImage(file="C:\\Users\\DELL\\Desktop\\Vs Code Python\\Tkinker Projects\\File Sorting Application\\Images\\audios.png")
        self.video_icon=PhotoImage(file="C:\\Users\\DELL\\Desktop\\Vs Code Python\\Tkinker Projects\\File Sorting Application\\Images\\videos.png")
        self.document_icon=PhotoImage(file="C:\\Users\\DELL\\Desktop\\Vs Code Python\\Tkinker Projects\\File Sorting Application\\Images\\documents.png")
        self.other_icon=PhotoImage(file="C:\\Users\\DELL\\Desktop\\Vs Code Python\\Tkinker Projects\\File Sorting Application\\Images\\others.png")

        Frame1=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame1.place(x=50, y=300, width=1250, height=300)
        self.lbl_total_files=Label(Frame1, text="Total files", font=("times new roman", 20), bg="white")
        self.lbl_total_files.place(x=10, y=10)

        self.lbl_total_image=Label(Frame1, bd=2, relief=RAISED, font=("times new roman",20,"bold"), image=self.image_icon, compound=TOP, bg="#087587", fg="white")
        self.lbl_total_image.place(x=20, y=60, width=230, height=200)

        self.lbl_total_audio=Label(Frame1, bd=2, relief=RAISED, font=("times new roman",20,"bold"), image=self.audio_icon, compound=TOP, bg="#008EA4", fg="white")
        self.lbl_total_audio.place(x=260, y=60, width=230, height=200)

        self.lbl_total_video=Label(Frame1, bd=2, relief=RAISED, font=("times new roman",20,"bold"), image=self.video_icon, compound=TOP, bg="#DF002A", fg="white")
        self.lbl_total_video=Label(Frame1, text="Total").place(x=500, y=60, width=230, height=200)

        self.lbl_total_document=Label(Frame1, bd=2, relief=RAISED, font=("times new roman",20,"bold"), image=self.document_icon, compound=TOP, bg="#008EA4", fg="white")
        self.lbl_total_document.place(x=740, y=60, width=230, height=200)

        self.lbl_total_other=Label(Frame1, bd=2, relief=RAISED, font=("times new roman",20,"bold"), image=self.other_icon, compound=TOP, bg="gray", fg="white")
        self.lbl_total_other.place(x=980, y=60, width=230, height=200)

        #---- Section 4 --------------------------------

        lbl_status = Label(self.root, text="Status", font=("times new roman",20), bg="white").place(x=50, y=620)
        self.lbl_st_total = Label(self.root, text="", font=("times new roman",18), bg="white", fg="green")
        self.lbl_st_total.place(x=300, y=170)

        self.lbl_st_moved=Label(self.root, text="", font=("times new roman",18), bg="white", fg="blue")
        self.lbl_st_moved.place(x=500, y=170)

        self.lbl_st_left=Label(self.root, text="", font=("times new roman",18), bg="white", fg="orange")
        self.lbl_st_left.place(x=700, y=170)

        #---- Buttons --------------------------------

        self.btn_clear=Button(self.root, text="Clear", command=self.clear, font=("times new roman",15,"bold"), bd=4, relief=RIDGE, bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white", cursor="hand2")
        self.btn_clear.place(x=880, y=610, height=45, width=200)

        self.btn_start=Button(self.root, state=DISABLED, command=self.start_function, text="Start", font=("times new roman",15,"bold"), bd=4, relief=RIDGE, bg="#ff5722", fg="white", activebackground="#ff5722", activeforeground="white", cursor="hand2")
        self.btn_start.place(x=1100, y=610, height=45, width=200)
    
    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        combine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True: # Checks if file is present or not and os.path.join adds path to directory to find files
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    #print(folder_name)
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents+=1

        # This is for calculating other files

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True: # Checks if file is present or not and os.path.join adds path to directory to find files
                ext="."+i.split(".")[-1]
                if ext.lower() not in combine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))             
        self.lbl_total_other.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))

    def browse_function(self):
        op=filedialog.askdirectory(title="Select Folder for Sorting")
        if op!=None:
            # print(op)
            self.var_foldername.set(str(op))
            self.directory=self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directory)
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            # print(self.all_files)
    
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True: # Checks if file is present or not and os.path.join adds path to directory to find files
                    c+=1
                    self.create_move(i.split('.')[-1],i) # gets the last part of extension (i.e. .mp3) and i gives the file name
                    self.lbl_st_total.config(text="Total: "+str(self.count))
                    self.lbl_st_moved.config(text="Moved: "+str(c))
                    self.lbl_st_left.config(text="Left: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()

            messagebox.showinfo("Success","All files has moved successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please select Folder")

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_document.config(text="")             
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files")

    def rename_folder():
        for folder in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,folder.lower()))

    def create_move(ext, file_name):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory.folder_name)) # mkdir is for makedirectory which creates new self.folders as per the folder names in the dictionary
                shutil.move(os.path,join(self.directory,file_name), os.path,join(directory,folder_name)) # if the folder is already present then it moves the files in that extension to particular folder
                find=True
                # print("Found", folder_name)
                break
        if find!=True:
            if self.other_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory, self.other_name)) # It will make a directory or folder named self.other_name
            shutil.move(os.path.join(directory,file_name), os.path.join(directory,self.other_name))





root = Tk()
obj=Sorting_App(root)
root.mainloop() 