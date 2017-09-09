import os.path
import databases.github.Accounts
a = databases.github.Accounts.Accounts()
a.Initialize(os.path.abspath(os.path.dirname(__file__)))
#print(a.DirectoryPath)
print(a.Filename)
#print(a.Extension)
#print(a.Path)
for t in a.Tables: print(t.Name)

