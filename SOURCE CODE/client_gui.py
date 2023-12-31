import tkinter as tk, json
from tkinter import ttk

with open('env_secure.json', 'r') as file:
    data = json.load(file)

def on_configure(event):
    canvas.configure(scrollregion=(0,0,0,710))

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root = tk.Tk()
root.title("Scrollable Labels")

# Create a Canvas widget
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)

# Create a Scrollbar and associate it with the Canvas
scrollbar = ttk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a Frame inside the Canvas to hold the labels
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

def info_packet(frame, lbl, info, rw):
    tk.Label(frame, text=lbl).grid(row=rw, column=1, columnspan=1, sticky='nw')
    tk.Label(frame, text=info).grid(row=rw, column=2, columnspan=1, sticky='nw')

def title_packet(frame, lbl, rw):
    tk.Label(frame, text=lbl).grid(row=rw, column=1, columnspan=2)

#personal info
title_packet(frame, "Personal Info", 2)
personal_info = data.get('Personal Info', {})
title_packet(frame, f"VITALINK INFO FOR {personal_info.get("name", '').upper()}", 1)
info_packet(frame, "Name: ", personal_info.get("name", ""), 3)
info_packet(frame, "Date of Birth: ",personal_info.get("dob", ""),4)
info_packet(frame, "Phone Number: ",personal_info.get("num",""),5)

#allergies
title_packet(frame, "Allergy Information", 6)
allergies = data.get('Allergies', {})
info_packet(frame, "Medication Allergies: ",allergies.get("med_al", ''),7)
info_packet(frame,"Food Allergies: ",allergies.get("food_al"),8)
info_packet(frame,"Allergy Treatment: ",allergies.get("al_treat",''),9)

#autism
title_packet(frame, "Autism Information", 10)
autism = data.get("Autism", {})
info_packet(frame, "Autism Disorder",autism.get("aut_type", ''),11)
info_packet(frame,"Autism Trigger", autism.get("aut_trig", ''),12)
info_packet(frame, "Autism treatment",autism.get("aut_treat", ''),13)

#cardiovascular risk
title_packet(frame, "Cardiovascular Info", 14)
cd_risk = data.get("Cardiovascular Disease", {})
info_packet(frame, "Cardiovascular Risk: ",cd_risk.get("CD_Risk"),15)

#active medication list
title_packet(frame, "Active Medications", 16)
act_med = data.get("Active Medications", {})
med_current = act_med.get("med_current", {})
med_list=''
for item in med_current:
    med_list += item + ': '+ med_current[item]+'\n'
info_packet(frame,"List of Medications: ",med_list[:-1],17)

#epilepsy
title_packet(frame, "Epilepsy Information",18)
epilepsy = data.get("Epilepsy",{})
info_packet(frame, "Epilepsy trigger: ",epilepsy.get("EP_trig", ''),19)
info_packet(frame, "Epilepsy treatment: ", epilepsy.get("EP_treat", ''), 20)

#mental illness
title_packet(frame, "Mental Illness information", 21)
men_ill = data.get("Mental Illness", {})
info_packet(frame, "Type of Mental Illness: ", men_ill.get("mi_type", ''), 22)
info_packet(frame, "Mental Illness trigger: ", men_ill.get("mi_trig", ''), 23)
info_packet(frame, "Mental Illness treatment: ", men_ill.get("mi_treat", ''), 24)

#medical card info
title_packet(frame, "Medical Info", 25)
med_info = data.get("Medical Info", {})
info_packet(frame, "Insurance Company: ", med_info.get("ins_com", ''), 26)
info_packet(frame, "Policy Number: ", med_info.get("pol_num", ''), 27)
info_packet(frame, "Gorup Number: ", med_info.get("group_num", ''), 28)
info_packet(frame, "Primary Care Provider: ", med_info.get("PCP", ''), 29)
info_packet(frame, "     Phone Number: ", med_info.get("PCP_num", ''), 30)
info_packet(frame, "Emergency Contact: ", med_info.get("emg_contact",''),31)
info_packet(frame, "     Relation: ", med_info.get("emg_con_rel", ''), 32)
info_packet(frame, "     Phone Number: ", med_info.get("emg_con_num", ''), 33)

# Bind the on_configure function to the Configure event of the Canvas
canvas.bind('<Configure>', on_configure)

# Bind the on_mousewheel function to the MouseWheel event of the Canvas
canvas.bind_all('<MouseWheel>', on_mousewheel)

root.mainloop()
