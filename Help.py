#check if the passwords match
def password_match(confirm_pass,passw):
    if confirm_pass==passw:
        return True
    return False

#check if the password as the requierments in the project
def password_as_reuirements(passw):
    if len(passw)<8 or len(passw)>10:
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


def check_password_error(password,password_found):
    x=''
    if password_found==False:
        x+='Password does not match the username\n'
    if len(password)<8:
        x+= 'your password is not long enough!\n'
    if len(password)>10:
        x+= 'your password is too much long!\n'
    nums=0
    chars=0
    symbols=0
    pass_chars=list(password)
    special_characters = "! @ ' ' # $ % ^ & * ( ) - + ? _ = , < > /"
    special_chars=special_characters.split()
    for i in range(len(pass_chars)):
        if pass_chars[i].isalpha()==True:
            chars+=1
        if pass_chars[i].isdigit()==True:
            nums+=1
        if pass_chars[i] in special_chars:
            symbols+=1

    if nums==0: #or chars==0 or symbols==0 :
        x+= 'your password does not include numbers\n'
    if chars==0:
        x+= 'your password does not include chars\n'
    if symbols==0:
        x+= 'your password does not include special chars\n'
    return x

def check_id_error(id,id_found):
    x=''
    if id_found==False:
        x+='Incorrect id'
    if len(id)>9:
        x+='your id includes more than 9 digits\n'
    if len(id)<9:
        x+='your id number includes less than 9 digits\n'

    if id.isdigit()==False:
        x+='your id number includes chars!\n'
    return x

def check_username_error(username):
    x=''
    if  len(username)<6:# or len(username_info_check)>8:
        x+='your username is not long enough\n'
    if len(username)>8:
        x+='your username too much long\n'

    username_chars=list(username)
    nums=0
    chars=0

    for i in range (len(username_chars)):
        if username_chars[i].isdigit()==True:
            nums+=1
        if username_chars[i].isalpha():
            chars+=1
    if chars==0:
        x+='your username does not include letters\n'
    if nums > 2:
        x += 'your username includes more than 2 digits\n'
    if nums==0:
        x+='your username does not include numbers\n'
    return x


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
    if age<=4:
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



def get_patient_diagnosis(patient_high_low_values,age,smoking,gender,ethnic,fever):
    diseases=[]
    if patient_high_low_values['wbc']=="high":
        if fever=="yes":
            diseases.append("infection")
        else:
            diseases.append("blood disease")
            diseases.append("cancer")

    if patient_high_low_values['wbc']=="low":
        diseases.append("viral disease")

    if patient_high_low_values['neut']=="low":
        diseases.append("infection")

    if patient_high_low_values['neut']=="low":
        diseases.append("disruption of blood production")
        diseases.append("infection")

    if patient_high_low_values['lymph']=="high":
        diseases.append("disruption of blood production")

    if patient_high_low_values['lymph']=="low":
        diseases.append("infection")
        diseases.append("cancer")

    if patient_high_low_values['rbc']=="high":
        diseases.append("disruption of blood production")

    if patient_high_low_values['rbc']=="low":
        diseases.append("anemia")

    if patient_high_low_values['hct']=="high":
        if smoking=="yes":
            diseases.append("smoking")
            diseases.append("lung disease")

    if patient_high_low_values['hct']=="low":
        diseases.append("bleeding")
        diseases.append("anemia")

    if patient_high_low_values['urea']=="high":
        diseases.append("kidney diseases")
        diseases.append("dehydration")
        diseases.append("diet disease")

    if patient_high_low_values['urea']=="low":
        diseases.append("diet disease")
        diseases.append("malnutrition")
        diseases.append("liver disease")

    if patient_high_low_values['hb']=="low":
        diseases.append("anemia")
        diseases.append("hematological disorder")
        diseases.append("iron deficiency")
        diseases.append("bleeding")

    if patient_high_low_values['creatine']=="high":
        diseases.append("kidney diseases")
        diseases.append("muscle disease")
        diseases.append("increased consumption of meat")

    if patient_high_low_values['creatine']=="low":
        diseases.append("malnutrition")
        diseases.append("iron deficiency")
        diseases.append("diet disease")

    if patient_high_low_values['iron']=="high":
        diseases.append("iron poisoning")

    if patient_high_low_values['iron']=="low":
        diseases.append("malnutrition")
        diseases.append("iron deficiency")
        diseases.append("bleeding")

    if patient_high_low_values['hdl']=="low":
        diseases.append("heart disease")
        diseases.append("hyperlipidemia")
        diseases.append("adult diabetes mellitus")

    if patient_high_low_values['ap']=="high":
        diseases.append("liver disease")
        diseases.append("biliary tract")
        diseases.append("overactive thyroid gland")
        diseases.append("use of various medications")

    if patient_high_low_values['ap']=="high":
        diseases.append("malnutrition")
        diseases.append("vitamin deficiency")

    diseases_reduction=reduction_diseases(diseases)
    return diseases_reduction




def reduction_diseases(diseases):
    for i in diseases:
        count=0
        for j in diseases:
            if i==j:
                count+=1
                if count>1:
                    diseases.remove(j)
    return diseases





'''
treatments={'anemia':'2 pills 10mg of B12 a day for a month','diet':'Schedule an appointment with a nutritionist'
            ,'bleeding':'go to hospital immediatly','hyperlipidemia':'Schedule an appointment with a nutritionist and one pill 5mg of smobell a day for  one week'
            ,'disruption of blood production':'one pill 10mg of B12 a day for a week and one pill 5mg of folic acid','hematological disorder':'An injection of a hormone to encourage red blood cell production'
            ,'iron poisoning':'go to hospital','dehydration':'drink a lot of water and drinks and have rest for awhile'
            ,'infection':'Dedicated antibiotic','vitamin deficiency':'ave a blood test to idenitify the missing vitamins'
            ,'viral disease':'have a rest in your house','biliary tract':'have a surgical treatment','heart disease':'Schedule an appointment with a nutritionist'
            ,'blood disease':'A combination of cyclophosphamide and corticosteroids','liver disease':'Referral to a specific diagnosis for the purpose of determining treatment'
            ,'kidney diseases':'Balance blood sugar levels','iron deficiency':'Two 10 mg pills of B12 a day for a month','muscle disease':'Two 5 mg pills of Altman c3 turmeric a day for a month'
            ,'smoking':'Stop smoking','lung disease':'Stop smoking and refer to X-ray of the lungs','overactive thyroid gland':'Propylthiouracil to reduce thyroid activity'
            ,'adult diabetes mellitus':'Insulin adjustment','cancer':'Entrectinib','increased consumption of meat':'Schedule an appointment with a nutritionist'
            ,'use of various medications':'Referral to a family doctor for a match between medications','malnutrition':'Schedule an appointment with a nutritionist'}
'''