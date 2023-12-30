import json, tkinter as tk

# Read JSON data from file
with open('env_secure.json', 'r') as file:
    data = json.load(file)

def info_packet(root, lbl, info, rw):
    tk.Label(root, text=lbl).grid(row=rw, column=1, sticky='nw')
    tk.Label(root, text=info).grid(row=rw, column=2, sticky='w')


root=tk.Tk()

#personal info
personal_info = data.get('Personal Info', {})
info_packet(root, "Name: ", personal_info.get("name", ""), 3)
info_packet(root, "Date of Birth: ",personal_info.get("dob", ""),4)
info_packet(root, "Phone Number: ",personal_info.get("num",""),5)

#allergies
allergies = data.get('Allergies', {})
info_packet(root, "Medication Allergies: ",allergies.get("med_al", ''),7)
info_packet(root,"Food Allergies: ",allergies.get("food_al"),8)
info_packet(root,"Allergy Treatment: ",allergies.get("al_treat",''),9)

#autism
autism = data.get("Autism", {})
info_packet(root, "Autism Disorder",autism.get("aut_type", ''),11)
info_packet(root,"Autism Trigger", autism.get("aut_trig", ''),12)
info_packet(root, "Autism treatment",autism.get("aut_treat", ''),13)

#cardiovascular risk
cd_risk = data.get("Cardiovascular Disease", {})
info_packet(root, "Cardiovascular Risk: ",cd_risk.get("CD_Risk"),15)

#active medication list
act_med = data.get("Active Medications", {})
med_current = act_med.get("med_current", {})
med_list=''
for item in med_current:
    med_list += item + ': '+ med_current[item]+'\n'
info_packet(root,"List of Medications: ",med_list[:-1],17)

#epilepsy
epilepsy = data.get("Epilepsy",{})
info_packet(root, "Epilepsy trigger: ",epilepsy.get("EP_trig", ''),19)
info_packet(root, "Epilepsy treatment: ", epilepsy.get("EP_treat", ''), 20)

#mental illness
men_ill = data.get("Mental Illness", {})
info_packet(root, "Type of Mental Illness: ", men_ill.get("mi_type", ''), 22)
info_packet(root, "Mental Illness trigger: ", men_ill.get("mi_trig", ''), 23)
info_packet(root, "Mental Illness treatment: ", men_ill.get("mi_treat", ''), 24)

#medical card info
med_info = data.get("Medical Info", {})
info_packet(root, "Insurance Company: ", med_info.get("ins_com", ''), 26)
info_packet(root, "Policy Number: ", med_info.get("pol_num", ''), 27)
info_packet(root, "Gorup Number: ", med_info.get("group_num", ''), 28)
info_packet(root, "Primary Care Provider: ", med_info.get("PCP", ''), 29)
info_packet(root, "     Phone Number: ", med_info.get("PCP_num", ''), 30)
info_packet(root, "Emergency Contact: ", med_info.get("emg_contact",''),31)
info_packet(root, "     Relation: ", med_info.get("emg_con_rel", ''), 32)
info_packet(root, "     Phone Number: ", med_info.get("emg_con_rel", ''), 33)

root.mainloop()