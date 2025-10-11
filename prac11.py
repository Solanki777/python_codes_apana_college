di={}
print(type(di))

x=int(input("enter phy:"))
di.update({"phy":x})

x=int(input("enter Maths:"))
di.update({"Maths":x})

x=int(input("enter Chem:"))
di.update({"Chem":x})
# di["physics"]=int(input("enter marks of physics:"))
# di["maths"]=int(input("enter marks of maths:"))
# di["chemistry"]=int(input("enter marks of chemistry:"))

print(di)