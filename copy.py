import os
import shutil 
  


 
source="C:/Users/user/Downloads/C102_assets-main/C102_assets-main/Badminton.gif"
destination="C:/Users/user/Downloads/C102_assets-main/C102_assets-main/1" 


dest=shutil.copy(source,destination)
print(dest)