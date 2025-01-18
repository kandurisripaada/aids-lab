p=int(input("enter project score:"))

i=int(input("enter internal score:"))

e=int(input("enter external score:"))

if(p>=50 and i>=50 and e>=50):

   total=(0.7 * p) + (0.1 * i) + (0.2 * e)

   if int(total) >= 90:

       print("A grade")

   elif int(total)>=80 and int(total)<90:

       print("B grade")

   elif int(total)>=50 and int(total)<80:

       print("C grade")

   else:

       print("D grade")

else:

   if p < 90:

       print("failed in project")

   if i < 44:

       print("failed in internal")

   if e < 45:

       print("Failed in external")