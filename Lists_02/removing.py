motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)
motorcycles.remove('yamaha')
print(motorcycles,"\n")
                #OR
too_expensive = ('honda')
motorcycles.remove(too_expensive)
print(motorcycles)
print (f"\nA {too_expensive.title()} is too expensive for me.")



Laptops_company = ['asus','acer','HP','dell','msi']
Laptops_company_popped = Laptops_company.pop()
print(Laptops_company)
print(Laptops_company_popped,"\n")

laptop = ['asus','hp','lenovo','acer']
print(laptop)
laptop.append("predeator")      #remember delete is for deleting the data & 
del laptop[0]                   #pop for giving last element
p = laptop.pop(3)
print(p,"\n")
                  

motercycle = ['honda',"ducati",'bmw','yamaha']
print (motercycle)
                            # for deleting specific element on the list
del motercycle[1]           # removing second element
del motercycle[1]           # removing secondlast (2ed) element
del motercycle[-2]               
print (motercycle,'\n')

refrigrator = ['haier','       5 star','idk','idk2']
pop = refrigrator.pop(1)
print(refrigrator) 

print (f"the first refrigrator i owned was a {pop.lstrip()}\n")
                                #  its remove the last added element and help to print in list, it's only useble in ist not strings

  
