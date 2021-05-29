from tkinter import *
from Help import *



def add_patient():
    global add_patient_screen
    add_patient_screen = Toplevel()
    add_patient_screen.geometry("500x500")
    add_patient_screen.title("patient details and diagnosis")

    add_patient_bg = PhotoImage(file=r'C:\Users\mohammed asad\Desktop\photos\500x500.gif')
    add_patient_label = Label(add_patient_screen, image=add_patient_bg)
    add_patient_label.place(x=0, y=0, relwidth=1, relheight=1)
    add_patient_label.image = add_patient_bg

    Label(add_patient_screen, text="enter the patient details and start the diagnosis",width="50", height="2",bg='light green',font=("Calibri", 15)).pack()
    Label(add_patient_screen, text="").pack()

    global name, name_entry, age, age_entry, smoking, smoking_entry, gender, gender_entry, ethnic, ethnic_entry,fever,fever_entry

    name = StringVar()
    age = StringVar()
    smoking = StringVar()
    gender = StringVar()
    ethnic = StringVar()
    fever=StringVar()

    Label(add_patient_screen, text="").pack()
    Label(add_patient_screen, text="Name",bg='light green').pack()
    name_entry = Entry(add_patient_screen, textvariable=name)
    name_entry.pack()

    Label(add_patient_screen, text="").pack()
    Label(add_patient_screen, text="Age",bg='light green').pack()
    age_entry = Entry(add_patient_screen, textvariable=age)
    age_entry.pack()

    Label(add_patient_screen, text="").pack()
    Label(add_patient_screen, text="Smoking",bg='light green').pack()
    smoking_entry = Entry(add_patient_screen, textvariable=smoking)
    smoking_entry.pack()

    Label(add_patient_screen, text="").pack()
    Label(add_patient_screen, text="Gender",bg='light green').pack()
    gender_entry = Entry(add_patient_screen, textvariable=gender)
    gender_entry.pack()

    Label(add_patient_screen, text="").pack()
    Label(add_patient_screen, text="Ethnic",bg='light green').pack()
    ethnic_entry = Entry(add_patient_screen, textvariable=ethnic)
    ethnic_entry.pack()

    Label(add_patient_screen, text="").pack()
    Label(add_patient_screen, text="Do you have a fever?",bg='light green').pack()
    fever_entry = Entry(add_patient_screen, textvariable=fever)
    fever_entry.pack()

    Label(text="\n").pack()
    Button(add_patient_screen, text="Diagnosis", bg="light green", height="1", width="20", command=diagnosis).pack()
    Label(text="").pack()


    name_entry.delete(0, END)
    age_entry.delete(0, END)
    smoking_entry.delete(0, END)
    gender_entry.delete(0, END)
    fever_entry.delete(0, END)
    ethnic_entry.delete(0, END)


def diagnosis():
    global diagnosis_screen
    diagnosis_screen = Toplevel(add_patient_screen)
    diagnosis_screen.geometry("500x500")
    diagnosis_screen.title("Diagnosis")

    diagnosis_screen_bg = PhotoImage(file=r'C:\Users\mohammed asad\Desktop\photos\500x500.gif')
    diagnosis_screen_label = Label(diagnosis_screen, image=diagnosis_screen_bg)
    diagnosis_screen_label.place(x=0, y=0, relwidth=1, relheight=1)

    diagnosis_screen_label.image = diagnosis_screen_bg

    global wbc, neut, lymph, rbc, hct, urea, hb, creatine, iron, hdl, ap
    global wbc_entry, neut_entry, lymph_entry, rbc_entry, hct_entry, urea_entry, hb_entry, creatine_entry, iron_entry, hdl_entry, ap_entry

    wbc = StringVar()
    neut = StringVar()
    lymph = StringVar()
    rbc = StringVar()
    hct = StringVar()
    urea = StringVar()
    hb = StringVar()
    creatine = StringVar()
    iron = StringVar()
    hdl = StringVar()
    ap = StringVar()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="White Blood Cells", bg="light green").pack()
    wbc_entry = Entry(diagnosis_screen, textvariable=wbc)
    wbc_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Neutrophil", bg="light green").pack()
    neut_entry = Entry(diagnosis_screen, textvariable=neut)
    neut_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Lymphocytes", bg="light green").pack()
    lymph_entry = Entry(diagnosis_screen, textvariable=lymph)
    lymph_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Red Blood Cells", bg="light green").pack()
    rbc_entry = Entry(diagnosis_screen, textvariable=rbc)
    rbc_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="HCT", bg="light green").pack()
    hct_entry = Entry(diagnosis_screen, textvariable=hct)
    hct_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Urea", bg="light green").pack()
    urea_entry = Entry(diagnosis_screen, textvariable=urea)
    urea_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Hb", bg="light green").pack()
    hb_entry = Entry(diagnosis_screen, textvariable=hb)
    hb_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Creatine", bg="light green").pack()
    creatine_entry = Entry(diagnosis_screen, textvariable=creatine)
    creatine_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Iron", bg="light green").pack()
    iron_entry = Entry(diagnosis_screen, textvariable=iron)
    iron_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="High Density Lipoprotein", bg="light green").pack()
    hdl_entry = Entry(diagnosis_screen, textvariable=hdl)
    hdl_entry.pack()

    # Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen, text="Alkaline Phosphatase", bg="light green").pack()
    ap_entry = Entry(diagnosis_screen, textvariable=ap)
    ap_entry.pack()

    Label(diagnosis_screen, text="")
    Button(diagnosis_screen, bg="light green", text="treatment", height="2", width="30",command=arranged_patient_data).pack()



def arranged_patient_data():
    patient_details_names = ['wbc', 'neut', 'lymph', 'rbc', 'hct', 'urea', 'hb', 'creatine', 'iron', 'hdl', 'ap']
    patient_details_values = [float(wbc.get()), float(neut.get()), float(lymph.get()), float(rbc.get()), float(hct.get()),
                              float(urea.get()), float(hb.get()), float(creatine.get()), float(iron.get()),
                              float(hdl.get()), float(ap.get())]
    patient_details = {}  # dictionary that contains the things and thier values
    for i in range(len(patient_details_values)):
        patient_details[patient_details_names[i]] = patient_details_values[i]
    copy_patient_details = patient_details.copy()

    name1 = name.get()
    age1 = age.get()
    smoking1 = smoking.get()
    gender1 = gender.get()
    ethnic1 = ethnic.get()
    fever1=fever.get()

    patient_high_low_values = check_patient_data(copy_patient_details, int(age.get()), smoking.get(), gender.get(),ethnic.get())
    patient_diagnosis=get_patient_diagnosis(patient_high_low_values.copy(),age1,smoking1,gender1,ethnic1,fever1)
    treatments = {'anemia': '2 pills 10mg of B12 a day for a month',
                  'diet disease': 'Schedule an appointment with a nutritionist'
        , 'bleeding': 'go to hospital immediatly',
                  'hyperlipidemia': 'Schedule an appointment with a nutritionist and one pill 5mg of smobell a day for  one week'
        , 'disruption of blood production': 'one pill 10mg of B12 a day for a week and one pill 5mg of folic acid',
                  'hematological disorder': 'An injection of a hormone to encourage red blood cell production'
        , 'iron poisoning': 'go to hospital', 'dehydration': 'drink a lot of water and drinks and have rest for awhile'
        , 'infection': 'Dedicated antibiotic',
                  'vitamin deficiency': 'ave a blood test to idenitify the missing vitamins'
        , 'viral disease': 'have a rest in your house', 'biliary tract': 'have a surgical treatment',
                  'heart disease': 'Schedule an appointment with a nutritionist'
        , 'blood disease': 'A combination of cyclophosphamide and corticosteroids',
                  'liver disease': 'Referral to a specific diagnosis for the purpose of determining treatment'
        , 'kidney diseases': 'Balance blood sugar levels',
                  'iron deficiency': 'Two 10 mg pills of B12 a day for a month',
                  'muscle disease': 'Two 5 mg pills of Altman c3 turmeric a day for a month'
        , 'smoking': 'Stop smoking', 'lung disease': 'Stop smoking and refer to X-ray of the lungs',
                  'overactive thyroid gland': 'Propylthiouracil to reduce thyroid activity'
        , 'adult diabetes mellitus': 'Insulin adjustment', 'cancer': 'Entrectinib',
                  'increased consumption of meat': 'Schedule an appointment with a nutritionist'
        , 'use of various medications': 'Referral to a family doctor for a match between medications',
                  'malnutrition': 'Schedule an appointment with a nutritionist'}
    wbc_entry.delete(0, END)
    neut_entry.delete(0, END)
    lymph_entry.delete(0, END)
    rbc_entry.delete(0, END)
    hct_entry.delete(0, END)
    urea_entry.delete(0, END)
    hb_entry.delete(0, END)
    creatine_entry.delete(0, END)
    iron_entry.delete(0, END)
    hdl_entry.delete(0, END)
    ap_entry.delete(0, END)

    patient_file(patient_details, patient_high_low_values, name1, age1, smoking1, gender1, ethnic1,treatments,patient_diagnosis)


def patient_file(patient_details, patient_high_low_values, name1, age1, smoking1, gender1, ethnic1,treatments,patient_diagnosis):
    patient_details_file = open("Patient_" + name1 + ".txt", "a")
    patient_details_file.write(
        "name: " + name1 + " age: " + age1 + " gender: " + gender1 + " ethnic: " + ethnic1 + " smoking: " + smoking1 + "\n")
    patient_details_file.write(
        "WBC: " + str(patient_details['wbc']) + " " + patient_high_low_values['wbc'] + " \nNeut: " + str(
            patient_details['neut']) + " " + patient_high_low_values['neut'] + " \nLymph: " + str(
            patient_details['lymph']) + " " + patient_high_low_values['lymph'] + "\nRBC: " + str(
            patient_details['rbc']) +" "+patient_high_low_values['rbc']+
        "\nHCT: " + str(patient_details['hct']) + " " + patient_high_low_values['hct'] + "\nUrea: " + str(
            patient_details['urea'])+" " + patient_high_low_values['urea'] + "\nHB: " + str(
            patient_details['hb']) + " " + patient_high_low_values['hb'] + "\nCreatine: " + str(
            patient_details['creatine']) + " " + patient_high_low_values['creatine'] +
        "\nIron: " + str(patient_details['iron']) + " " + patient_high_low_values['iron'] + "\nHDL: " + str(
            patient_details['hdl']) + " " + patient_high_low_values['hdl'] + "\nAlkaline Phosphatase: " + str(
            patient_details['ap']) + " " + patient_high_low_values['ap'] + "\n")

    treatment=[]
    patient_details_file.write("diseases: \n")
    counter=0
    for i in patient_diagnosis:
        counter+=1
        if counter%5==0:
            patient_details_file.write("\n")
        patient_details_file.write(i +",")
    for i in patient_diagnosis:
        treatment.append(treatments[i])

    patient_details_file.write("\nTreatment: \n")
    counter=0
    for i in treatment:
        counter+=1
        if counter%5==0:
            patient_details_file.write("\n")
        patient_details_file.write(i+',')
    patient_details_file.close()
    treatment_screen(name1)

def treatment_screen(name):
    global patient_details_treatments_screen
    patient_details_treatments_screen=Toplevel()
    patient_details_treatments_screen.geometry("1000x1000")
    patient_details_treatments_screen.title("Patient details and treatments")

    patient_details_treatments_screen_bg=PhotoImage(file=r'C:\Users\mohammed asad\Desktop\photos\treatment background.gif')
    patient_details_treatments_screen_label=Label(patient_details_treatments_screen, image=patient_details_treatments_screen_bg)
    patient_details_treatments_screen_label.place(x=0,y=0,relwidth=1,relheight=1)

    patient_details_treatments_screen_label.image = patient_details_treatments_screen_bg

    treatments_file=open("Patient_" + name + ".txt","r")
    flag=0
    for line in treatments_file.readlines():
        if flag == 0:
            Label(patient_details_treatments_screen, text=line, width="10000", font=("Calibri", 9), anchor=W).pack()
        if line=='Treatment:':
            flag=1
        if flag ==1:
            Label(patient_details_treatments_screen, text=line, width="10000", font=("Calibri", 9), fg='red', anchor=W).pack()

    treatments_file.close()

    Button(patient_details_treatments_screen,text="close",bg="light green", height="2", width="30", command=close_patient_details_treatments_screen).pack()

def close_patient_details_treatments_screen():
    patient_details_treatments_screen.withdraw()
    diagnosis_screen.withdraw()
    add_patient_screen.withdraw()
