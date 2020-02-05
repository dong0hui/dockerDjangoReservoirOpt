from fsas.CosmosMongo import _Users

print("=>")
print("Function _create() testing...")
newuser = _Users("hui_dong1", "nexusjobstorage", "nexusqa")
print(newuser._create())
newuser = _Users("hui_dong1")
print(newuser._create())
print("_create() passed.")
print("==>")

print("===>")
# If error occurs, check the info in Database
print("Function _getBlobConnectionString() testing...")
newuser = _Users("hui_dong1", "nexusjobstorage", "nexusqa")
print(newuser._getBlobConnectionString())
print("_getBlobConnectionString() passed.")
print("====>")
