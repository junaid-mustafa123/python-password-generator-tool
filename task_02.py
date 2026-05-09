import random
import string
class PasswordGeneratorTool:

    def show(self):
        print("-----------------------------------")
        print("Project 2 – Password Generator Tool")
        print("-------------------------------------")
        try:
            length = int(input("ENTER THE LENGTH OF PASSWORD WHICH YOU NEED : "))
            if length<=0:
                print("Sorry ! I can't generate zero length password")
                exit() 
        except Exception as e:
            print(f"Error : {e}")    
   
        all_chars = string.digits + string.ascii_lowercase + string.punctuation
        password = ""
        for i in range(length):
            password += random.choice(all_chars)
        print("------------------------------------")    
        print("FINALLY GERNERATED PASSWORD IS : ") 
        print(f"PASSWORD : {password}")  
        print(f"LENGTH OF PASSWORD IS : {len(password)}") 
        print("--------------------------------------")
        
pgt = PasswordGeneratorTool()
pgt.show()

