import os
import shutil 
#print(dir(os))
# get current working directory=getcwd()
cwd=os.getcwd()
#print(cwd)

#creating a newfloder=mkdir()=> make directory
#os.mkdir("c111")
os.listdir()#list of files in the folder
path="C:/Users/user/Downloads/C102_assets-main/C102_assets-main/Badminton.gif"
isExists=os.path.exists(path)
print(isExists)


#shutil split text
root,ext=os.path.splitext(path)
print("the root",root)
print("the extension",ext)