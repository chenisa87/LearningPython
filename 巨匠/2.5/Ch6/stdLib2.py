import os

print(os.name) # 顯示系統名稱 'posix'/'nt'/'ce'/'java'
print(os.getcwd()) # 顯示當前目錄
os.chdir(r"C:\Python38")  #切換路徑
print(os.getcwd()) # 顯示當前目錄
print(os.listdir (r"C:\Python38")) #列出目錄內容
os.system('mkdir tmp') #執行系統命令
