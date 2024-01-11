import json, tkinter as tk
import serial, time
import encryption, random

def split_string_nth(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

def Title(boolean:bool):
    if boolean:
        return 2
    else:
        return 1

def add_label(root, row, text, isTitle=False):
    tk.Label(root, text=text).grid(row=row, column=1, columnspan=Title(isTitle))

def add_entry(root, row):
    entry=tk.Entry(root)
    entry.grid(row=row, column=2)
    return entry

root = tk.Tk()
root.iconbitmap("VL.ico")
add_label(root, 1, "VITALINK: INFORMATION UPDATE", isTitle=True)

add_label(root, 2, "Personal Information", isTitle=True)
add_label(root, 3, "Name: ")
add_label(root, 4, "Date of Birth: ")
add_label(root, 5, "Phone Number: ")
pi_name=add_entry(root, 3)
pi_dob=add_entry(root,4)
pi_num=add_entry(root,5)

add_label(root, 6, "Allergy Information", isTitle=True)
add_label(root, 7, "Medicine allergies: ")
add_label(root, 8, "Food Allergies: ")
add_label(root, 9, "Allergy treatment: ")
med_al = add_entry(root, 7)
food_al= add_entry(root, 8)
treat_al=add_entry(root, 9)

add_label(root, 10, "Autism Information", isTitle=True)
add_label(root, 11, "Disorder Name: ")
add_label(root, 12, "Triggers: ")
add_label(root, 13, "Treatment: ")
aut_type = add_entry(root, 11)
aut_trig = add_entry(root, 12)
aut_treat= add_entry(root, 13)

add_label(root, 14, "Cardiovascular Information", isTitle=True)
add_label(root, 15, "Cardiovascular Risk: ")
cd_risk=add_entry(root, 15)

add_label(root, 16, "Active Medications", isTitle=True)
add_label(root, 17, "One per line Medication: Purpose\ne.g. Fexofenadine: Allergies")
meds=tk.Text(root, width=45, height=10)
meds.grid(row=17, column=2)

sbmt_btn = tk.Button(root, text="Next", command=lambda: root.quit())
sbmt_btn.grid(row=18, column=1, columnspan=2)

root.mainloop()
pi_name=pi_name.get()
pi_dob=pi_dob.get()
pi_num=pi_num.get()
med_al=med_al.get()
food_al=food_al.get()
treat_al=treat_al.get()
aut_type=aut_type.get()
aut_trig=aut_trig.get()
aut_treat=aut_treat.get()
cd_risk=cd_risk.get()
meds=meds.get(1.0, 'end')
root.destroy()

root=tk.Tk()
add_label(root, 1, "VITAFILE INFORMATION UPDATE 2", isTitle=True)
add_label(root, 2, "Epilepsy Information", isTitle=True)
add_label(root, 3, "Epilepsy Triggers: ")
add_label(root, 4, "Epilepsy Treatment: ")
ep_trig=add_entry(root, 3)
ep_treat=add_entry(root, 4)

add_label(root, 5, "Mental Illness", isTitle=True)
add_label(root, 6, "Mental Illness type: ")
add_label(root, 7, "Mental Illness Triggers: ")
add_label(root, 8, "Mental Illness treatment: ")
mi_type=add_entry(root, 6)
mi_trig=add_entry(root, 7)
mi_treat=add_entry(root,8)

add_label(root, 9, "Medical Card Information", isTitle=True)
add_label(root, 10, "Insurance Company: ")
add_label(root, 11, "Policy Number: ")
add_label(root, 12, "Group Number: ")
add_label(root, 13, "Primary Care Provider: ")
add_label(root, 14, "     number: ")
add_label(root, 15, "Emergency Contact: ")
add_label(root, 16, "     Contact relation:")
add_label(root, 17, "     Contact Number: ")
ins_com=add_entry(root, 10)
pol_num=add_entry(root, 11)
group_num=add_entry(root,12)
pcp=add_entry(root, 13)
pcp_num=add_entry(root, 14)
emg_con=add_entry(root, 15)
emg_con_rel=add_entry(root, 16)
emg_con_num=add_entry(root, 17)

sbmt_btn = tk.Button(root, text="Submit", command=lambda: root.quit())
sbmt_btn.grid(row=18, column=1, columnspan=2)

root.mainloop()
ep_trig=ep_trig.get()
ep_treat=ep_treat.get()
mi_type=mi_type.get()
mi_trig=mi_trig.get()
mi_treat=mi_treat.get()
ins_com=ins_com.get()
pol_num=pol_num.get()
group_num=group_num.get()
pcp=pcp.get()
pcp_num=pcp_num.get()
emg_con=emg_con.get()
emg_con_rel=emg_con_rel.get()
emg_con_num=emg_con_num.get()
root.destroy()

act_meds={}
meds=meds.split("\n")
for i in meds:
    if i == '':
        pass
    else: 
        x=i.split(": ")
        act_meds.update({x[0]:x[1]})


vitalink_info={
    "Personal Info": {
        "name": pi_name,
        "dob": pi_dob,
        "num": pi_num
    },
    "Allergies":{
        "med_al": med_al,
        "food_al": food_al,
        "al_treat": treat_al
    },
    "Autism": {
        "aut_type": aut_type,
        "aut_trig": aut_trig,
        "aut_treat": aut_treat
    },
    "Cardiovascular Disease": {
        "CD_Risk": cd_risk
    },
    "Active Medications": {
        "med_current": act_meds
    },
    "Epilepsy": {
        "EP_trig": ep_trig,
        "EP_treat": ep_treat
    },
    "Mental Illness": {
        "mi_type": mi_type,
        "mi_trig": mi_trig,
        "mi_treat": mi_treat
    },
    "Medical Info": {
        "ins_com": ins_com,
        "pol_num": pol_num,
        "group_num":group_num,
        "PCP":pcp,
        "PCP_num": pcp_num,
        "emg_contact": emg_con,
        "emg_con_rel": emg_con_rel,
        "emg_con_num": emg_con_num
    }
}


with open("env_secure.json", 'w+') as outfile:
    json.dump(vitalink_info, outfile, indent=4)

passkey = random.randbytes(32)
nonce = random.randbytes(8)

enc = encryption.File_Enc()
enc.enc("env_secure.json", passkey, nonce)

s = serial.Serial('COM5', 9600, timeout=10)
with open("env_secure.json", "rb+") as infile:
    for line in infile:
        sections = split_string_nth(line, 7)
        for section in sections:
            s.write(section+b'\n')
            time.sleep(0.1)

# Send data to the server. File used for simplicity.
with open("../server/server", "wb+") as outfile:
    outfile.write(passkey + b'\n\n' + nonce)
