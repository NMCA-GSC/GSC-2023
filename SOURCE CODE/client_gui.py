from environs import Env
import tkinter as tk

data = Env()
data.read_env("env_secure.env")

#personal info
name = data("name")
dob = data("dob")
num = data("num")

#allergies
med_al = data("Med_al")
food_al = data("Food_al")
al_treat = data("al_treat")

#autism
aut_type = data("aut_type")
aut_trig = data("aut_trig")
aut_treat = data("aut_treat")

#Cardiovascular Disease
cd_risk = data("CD_risk")

#active Meds
med_current = data("med_current")

#Epilepsy
ep_trig = data("EP_trig")
ep_treat = data("EP_treat")

#Mental Illness
mi_types = data("mi_types")
mi_trig = data("mi_trig")
mi_treat = data("mi_treat")

#medical info
ins_com = data("ins_com")
pol_num = data("Pol_num")
group_num = data("Group_num")
pcp = data("PCP")
pcp_num = data("PCP_num")
emg_contact = data("emg_contact")
emg_con_rel = data("emg_con_rel")
emg_con_num = data("emg_con_num")

#display window
root = tk.Tk()
root.title(f"Medical info for {name}")

title_lbl = tk.Label(root, text=f"MEDICAL INFORMATION FOR {name.upper()}")
title_lbl.grid(row=1, column=1, columnspan=2)

pi_info_lbl = tk.Label(root, text="Personal Info:")
pi_info_lbl.grid(row=2, column=1, columnspan=2)

name_index_lbl = tk.Label(root, text="Name: ")
name_index_lbl.grid(row=3, column=1, columnspan=1)
name_info_lbl = tk.Label(root, text=name)
name_info_lbl.grid(row=3, column=2, columnspan=1)

dob_index_lbl = tk.Label(root, text="Date of Birth: ")
dob_index_lbl.grid(row=4, column=1, columnspan=1)
dob_info_lbl = tk.Label(root, text=dob)
dob_info_lbl.grid(row=4, column=2, columnspan=1)

num_index_lbl = tk.Label(root, text="Phone Number: ")
num_index_lbl.grid(row=5, column=1, columnspan=1)
num_info_lbl = tk.Label(root, text=num)
num_info_lbl.grid(row=5, column=2, columnspan=1)

al_info_lbl = tk.Label(root, text="Allergies Info:")
al_info_lbl.grid(row=6, column=1, columnspan=2)

ma_index_lbl = tk.Label(root, text="Medicine Allergies: ")
ma_index_lbl.grid(row=7, column=1, columnspan=1)
ma_info_lbl = tk.Label(root, text=med_al)
ma_info_lbl.grid(row=7, column=2, columnspan=1)

fa_index_lbl = tk.Label(root, text="Food Allergies: ")
fa_index_lbl.grid(row=8, column=1, columnspan=1)
fa_info_lbl = tk.Label(root, text=food_al)
fa_info_lbl.grid(row=8, column=2, columnspan=1)

at_index_lbl = tk.Label(root, text="Allergy Treatment: ")
at_index_lbl.grid(row=9, column=1, columnspan=1)
at_info_lbl = tk.Label(root, text=al_treat)
at_info_lbl.grid(row=9, column=2, columnspan=1)

root.mainloop()