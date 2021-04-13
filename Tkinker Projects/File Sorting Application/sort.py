import os, shutil
folders={
    'videos':['.mp4'],
    'audios':['.wav','.mp3'],
    'images':['.jpg','.png'],
    'documents':['.doc','.xlsx','xls','.pdf','.zip','rar']
}

# print(folders)
# for folder_name in folders:
#     print(folder_name, folders[folder_name])


def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,folder))==True:
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))
def create_move(ext, file_name):
    find=False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name in os.listdir(directory):
                os.mkdir(os.path.join(directory.folder_name)) # mkdir is for makedirectory which creates new folders as per the folder names in the dictionary
            shutil.move(os.path,join(directory,file_name), os.path,join(directory,folder_name)) # if the folder is already present then it moves the files in that extension to particular folder
            find=True
            # print("Found", folder_name)
            break
    if find!=True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory, other_name)) # It will make a directory or folder named other_name
        shutil.move(os.path.join(directory,file_name), os.path.join(directory,other_name))



directory=input("Enter the Location: ")
other_name=input("Enter the folder name for Unknown Files: ")
rename_folder()
all_files=os.listdir(directory)
length=len(all_files)
count=1
# print(all_files)

for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True: # Checks if file is present or not and os.path.join adds path to directory to find files
        create_move(i.split('.')[-1],i) # gets the last part of extension (i.e. .mp3) and i gives the file name
    print(f"Total Files: {length} | Done: {count} | Left: {length-count}")
    count+=1

