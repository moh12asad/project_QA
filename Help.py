#check if the passwords match
def password_match(confirm_pass,passw):
    if confirm_pass==passw:
        return True
    return False

#check if the password as the requierments in the project
def password_as_reuirements(passw):
    if len(passw)<8 or len(passw)>10:
        print("length")
        return False
    nums=0
    chars=0
    symbols=0
    pass_chars=list(passw)
    special_characters = "! @ ' ' # $ % ^ & * ( ) - + ? _ = , < > /"
    special_chars=special_characters.split()
    for i in range(len(pass_chars)):
        if pass_chars[i].isalpha()==True:
            chars+=1
        if pass_chars[i].isdigit()==True:
            nums+=1
        if pass_chars[i] in special_chars:
            symbols+=1

    if nums==0 or chars==0 or symbols==0 :
        print(int(symbols))
        print(int(chars))
        print(int(symbols))
        return False

    return True


def username_as_requirements(username_info_check):
    if  len(username_info_check)<6 or len(username_info_check)>8:
        return False
    username_chars=list(username_info_check)
    nums=0
    chars=0
    for i in range (len(username_chars)):
        if username_chars[i].isdigit()==True:
            nums+=1
            if nums>2:
                return False
        if username_chars[i].isalpha():
            chars+=1
    if nums+chars<6:
        return False
    return True

