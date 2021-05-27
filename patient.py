from tkinter import *
def add_patient():
    global add_patient_screen
    add_patient_screen=Toplevel()
    add_patient_screen.geometry("500x500")
    add_patient_screen.title("patient details and diagnosis")
    Label(add_patient_screen,text="enter the patient details and start the diagnosis").pack()
    Label(add_patient_screen,text="").pack()

    global name,name_entry,age,age_entry,smoking,smoking_entry,gender,gender_entry,ethnic,ethnic_entry

    name=StringVar()
    age=StringVar()
    smoking=StringVar()
    gender=StringVar()
    ethnic=StringVar()

    Label(add_patient_screen,text="").pack()
    Label(add_patient_screen,text="Name").pack()
    name_entry=Entry(add_patient_screen,textvariable=name)
    name_entry.pack()

    Label(add_patient_screen,text="").pack()
    Label(add_patient_screen,text="Age").pack()
    age_entry=Entry(add_patient_screen,textvariable=age)
    age_entry.pack()

    Label(add_patient_screen,text="").pack()
    Label(add_patient_screen,text="Smoking").pack()
    smoking_entry=Entry(add_patient_screen,textvariable=smoking)
    smoking_entry.pack()

    Label(add_patient_screen,text="").pack()
    Label(add_patient_screen,text="Gender").pack()
    gender_entry=Entry(add_patient_screen, textvariable=gender)
    gender_entry.pack()

    Label(add_patient_screen,text="").pack()
    Label(add_patient_screen,text="Ethnic").pack()
    ethnic_entry=Entry(add_patient_screen, textvariable=ethnic)
    ethnic_entry.pack()



    Label(text="\n").pack()
    Button(add_patient_screen,text="Diagnosis",bg="light green",height="1",width="20",command=diagnosis).pack()
    Label(text="").pack()



def diagnosis():
    global diagnosis_screen
    diagnosis_screen=Toplevel(add_patient_screen)
    diagnosis_screen.geometry("500x500")
    diagnosis_screen.title("Diagnosis")
    global wbc,neut,lymph,rbc,hct,urea,hb,creatine,iron,hdl,ap

    wbc=StringVar()
    neut=StringVar()
    lymph=StringVar()
    rbc=StringVar()
    hct=StringVar()
    urea=StringVar()
    hb = StringVar()
    creatine=StringVar()
    iron=StringVar()
    hdl=StringVar()
    ap=StringVar()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Wbc",bg="light green").pack()
    wbc_entry=Entry(diagnosis_screen, textvariable=wbc)
    wbc_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Neutrophil",bg="light green").pack()
    neut_entry=Entry(diagnosis_screen, textvariable=neut)
    neut_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Lymphocytes",bg="light green").pack()
    lymph_entry=Entry(diagnosis_screen, textvariable=lymph)
    lymph_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Red Blood Cells",bg="light green").pack()
    rbc_entry=Entry(diagnosis_screen, textvariable=rbc)
    rbc_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="HCT",bg="light green").pack()
    hct_entry=Entry(diagnosis_screen, textvariable=hct)
    hct_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Urea",bg="light green").pack()
    urea_entry=Entry(diagnosis_screen, textvariable=urea)
    urea_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Hb",bg="light green").pack()
    hb_entry=Entry(diagnosis_screen, textvariable=hb)
    hb_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Creatine",bg="light green").pack()
    creatine_entry=Entry(diagnosis_screen, textvariable=creatine)
    creatine_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Iron",bg="light green").pack()
    iron_entry=Entry(diagnosis_screen, textvariable=iron)
    iron_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="High Density Lipoprotein",bg="light green").pack()
    hdl_entry=Entry(diagnosis_screen, textvariable=hdl)
    hdl_entry.pack()

    #Label(diagnosis_screen,text="").pack()
    Label(diagnosis_screen,text="Alkaline Phosphatase",bg="light green").pack()
    ap_entry=Entry(diagnosis_screen, textvariable=ap)
    ap_entry.pack()

    Label(diagnosis_screen,text="")
    Button(diagnosis_screen,bg="light green",text="tepol",height="2", width="30",command=check_patient_data).pack()



def check_patient_data():
    patient_details_names=['wbc','neut','lymph','rbc','hct','urea','hb','creatine','iron','hdl','ap']
    patient_details_values=[int(wbc.get()),int(neut.get()),int(lymph.get()),int(rbc.get()),int(hct.get()),int(urea.get()),int(hb.get()),int(creatine.get()),int(iron.get()),int(hdl.get()),int(ap.get())]
    patient_details={}
    for i in range(len(patient_details_values)):
        patient_details[patient_details_names[i]]=patient_details_values[i]



















