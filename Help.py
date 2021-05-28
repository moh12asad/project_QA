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

def check_patient_wbc(wbc_value,age):
    if age>=18:
        if wbc_value>11000:
            return "high"
        if wbc_value<4500:
            return "low"
    if age>4 and age<17:
        if wbc_value>15500:
            return "high"
        if wbc_value<5500:
            return "low"
    else:
        if wbc_value>17500:
            return "high"
        if wbc_value<6000:
            return "low"
    return "good"

def check_patient_neut(neut_value):
    if neut_value>0.54:
        return "high"
    if neut_value<0.28:
        return "low"
    return "good"

def check_patient_lymph(lymph_value):
    if lymph_value>0.52:
        return "high"
    if lymph_value<0.36:
        return "low"
    return "good"

def check_patient_rbc(rbc_value):
    if rbc_value>6:
        return "high"
    if rbc_value<4.5:
        return "low"
    return "good"

def check_patient_hct(hct_value,gender):
    if gender=="male":
        if hct_value>0.54:
            return "high"
        if hct_value<0.37:
            return "low"
        return "good"
    if gender=="female":
        if hct_value>0.47:
            return "high"
        if hct_value<0.33:
            return "low"
        return "good"

def check_patient_urea(urea_value,ethnic):
    if ethnic=="eastern":
        if urea_value>1.1*43:
            return "high"
        if urea_value<1.1*17:
            return "low"
        return "good"
    else:
        if urea_value>43:
            return "high"
        if urea_value<17:
            return "low"
        return "good"

def check_patient_hb(hb_value,gender,age):
    if age>0 and age<17:
        if hb_value>15.5:
            return "high"
        if hb_value<11.5:
            return "low"
        return "good"
    if gender=="female":
        if hb_value>16:
            return "high"
        if hb_value<12:
            return "low"
        return "good"
    if gender=="male":
        if hb_value>18:
            return "high"
        if hb_value<12:
            return "low"
        return "good"

def check_patient_creatine(creatine_value,age):
    if age>=0 and age<=2:
        if creatine_value>0.5:
            return "high"
        if creatine_value<0.2:
            return "low"
        return "good"
    if age>=3 and age<=17:
        if creatine_value<0.5:
            return "low"
        if creatine_value>1:
            return "high"
        return "good"
    if age>=18 and age<=59:
        if creatine_value>1:
            return "high"
        if creatine_value<0.6:
            return "low"
        return "good"
    if age>=60:
        if creatine_value>1.2:
            return "high"
        if creatine_value<0.6:
            return "low"
        return "good"

def check_patient_iron(iron_value,gender):
    if gender=="female":
        if iron_value>160*0.8:
            return "high"
        if iron_value<60*0.8:
            return "low"
        return "good"
    if gender=="male":
        if iron_value>160:
            return "high"
        if iron_value<60:
            return "low"
        return "good"

def check_patient_hdl(hdl_value,gender,ethnic):
    if ethnic=="ethiopian":
        if gender=="male":
            if hdl_value>62*1.2:
                return "high"
            if hdl_value<29*1.2:
                return "low"
            return "good"
        if gender=="female":
            if hdl_value>82*1.2:
                return "high"
            if hdl_value<34*1.2:
                return "low"
            return "good"
    else:
        if gender=="male":
            if hdl_value>62:
                return "high"
            if hdl_value<29:
                return "low"
            return "good"
        if gender=="female":
            if hdl_value>82:
                return "high"
            if hdl_value<34:
                return "low"
            return "good"

def check_patient_ap(ap_value,ethnic):
    if ethnic=="eastern":
        if ap_value<60:
            return "low"
        if ap_value>120:
            return "high"
        return "good"
    else:
        if ap_value>90:
            return "high"
        if ap_value<30:
            return "low"
        return "good"




#function for patient
def check_patient_data(patient_details,age,smoking,gender,ethnic):
    patient_wbc=check_patient_wbc(patient_details['wbc'],age)
    patient_details['wbc']=patient_wbc

    patient_neut=check_patient_neut(patient_details['neut'])
    patient_details['neut']=patient_neut

    patient_lymph=check_patient_lymph(patient_details['lymph'])
    patient_details['lymph']=patient_lymph

    patient_rbc=check_patient_rbc(patient_details['rbc'])
    patient_details['rbc']=patient_rbc

    patient_hct=check_patient_hct(patient_details['hct'],gender)
    patient_details['hct']=patient_hct

    patient_urea=check_patient_urea(patient_details['urea'],ethnic)
    patient_details['urea']=patient_urea

    patient_hb=check_patient_hb(patient_details['hb'],gender,age)
    patient_details['hb']=patient_hb

    patient_creatine=check_patient_creatine(patient_details['creatine'],age)
    patient_details['creatine']=patient_creatine

    patient_iron=check_patient_iron(patient_details['iron'],gender)
    patient_details['iron']=patient_iron

    patient_hdl=check_patient_hdl(patient_details['hdl'],gender,ethnic)
    patient_details['hdl']=patient_hdl

    patient_ap=check_patient_ap(patient_details['ap'],ethnic)
    patient_details['ap']=patient_ap

    return patient_details







