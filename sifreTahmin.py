from random import *
print("""
'   $$$$$$\  $$\  $$$$$$\                           $$$$$$$$\        $$\                     $$\           
'  $$  __$$\ \__|$$  __$$\                          \__$$  __|       $$ |                    \__|          
'  $$ /  \__|$$\ $$ /  \__|$$$$$$\   $$$$$$\           $$ | $$$$$$\  $$$$$$$\  $$$$$$\$$$$\  $$\ $$$$$$$\  
'  \$$$$$$\  $$ |$$$$\    $$  __$$\ $$  __$$\          $$ | \____$$\ $$  __$$\ $$  _$$  _$$\ $$ |$$  __$$\ 
'   \____$$\ $$ |$$  _|   $$ |  \__|$$$$$$$$ |         $$ | $$$$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |$$ |  $$ |
'  $$\   $$ |$$ |$$ |     $$ |      $$   ____|         $$ |$$  __$$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |
'  \$$$$$$  |$$ |$$ |     $$ |      \$$$$$$$\          $$ |\$$$$$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |
'   \______/ \__|\__|     \__|       \_______|         \__| \_______|\__|  \__|\__| \__| \__|\__|\__|  \__|
'                                                                                                                                                                                                                   
""")
user_pass = input("Şifrenizi Giriniz:")
password=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z,']
guess=""
while(guess!=user_pass):
    guess=""
    for letter in range(len(user_pass)):
        guess_letter=password[randint(0, 25)]
        guess=str(guess_letter)+str(guess)
    print(guess)
print("Şifreniz: ",guess)