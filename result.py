print(" Welcome to The Result Generator ")
print(" We are  pleased to have you Onboard ")
print("--------------------------------------")
schoo=input(" Enter The Name of your school ")
En=input(" Enter your Exam seat Number ")
stu=input(" Enter the name of the Student ---> ")
mar=int(input(" Enter the marks scored by Student out of 100 ---> "))
if (mar>=90):
  print("",stu," of ",schoo," having seat number ",En,"got an A+ grade Congrats!!!!!!!!")
elif (mar>=80):
  print("",stu," of ",schoo," having seat number ",En,"got an A grade Congrats!!!!!!!!")
elif (mar>=70):
  print("",stu," of ",schoo," having seat number ",En,"got an B+ grade Congrats!!!!!!!!")
elif (mar>=60):
  print("",stu," of ",schoo," having seat number ",En,"got an B grade Congrats!!!!!!!!")
elif (mar>=50):
  print("",stu," of ",schoo," having seat number ",En,"got an C+ grade Congrats!!!!!!!!")
else:
  print(" The above Student has Failed in the examination. Practice makes a Man perfect please hard next year ")