password = input("Enter a string for password: ")

ls_number = list("0123456789")
ls_alphabets = list("qwertyuiopasdfghjklzxcvbnm")

digit_count = 0
ls_password = list(password)

if len(password)>= 8:
    for i in ls_password:
        if i in ls_alphabets or i in ls_number:
            if i in ls_number:
                digit_count += 1
           
        else:
            print("invalid password")
            break
            
    
    if digit_count>=2:
        print("valid password")
    else:
        print("invalid password")
else:
    print("invalid password")
