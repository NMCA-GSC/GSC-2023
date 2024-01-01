import tkinter as tk, json, os, shutil
from tkinter import ttk

def exec():
    with open('env_secure.json', 'r+') as file:
        data = json.load(file)
        file.close()

    def on_configure(event):
        canvas.configure(width=300, scrollregion=(0,0,0,710))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_close():
        try:
            os.remove('env_secure.json')
        except: pass
        try: 
            shutil.rmtree('__pycache__')
        except: pass
        root.destroy()


    root = tk.Tk()
    root.title("VITALINK")
    root.iconbitmap("VL.ico")
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
        tk.Label(frame, text=lbl, bg=frame['bg']).grid(row=rw, column=1, columnspan=1, sticky='n')
        tk.Label(frame, text=info, bg=frame['bg']).grid(row=rw, column=2, columnspan=1, sticky='nw')

    def title_packet(frame, lbl, rw):
        tk.Label(frame, text=lbl, bg=frame['bg']).grid(row=rw, column=1, columnspan=2, sticky='n')

    #personal info
    pers_info_frame=tk.Frame(frame,background="#80D1EA")
    pers_info_frame.grid(row=1, column=1, columnspan=2, sticky='ew')
    root_frame=tk.Frame(frame, background="#3396E8")
    root_frame.grid(row=0, column=1,columnspan=2, sticky='ew')
    title_packet(pers_info_frame, "Personal Info", 2)
    personal_info = data.get('Personal Info', {})
    title_packet(root_frame, f"VITALINK INFO FOR {personal_info.get("name", '').upper()}", 1)
    info_packet(pers_info_frame, "Name: ", personal_info.get("name", ""), 3)
    info_packet(pers_info_frame, "Date of Birth: ",personal_info.get("dob", ""),4)
    info_packet(pers_info_frame, "Phone Number: ",personal_info.get("num",""),5)

    #allergies
    allergy_frame=tk.Frame(frame, background="#3396E8")
    allergy_frame.grid(row=2, column=1,columnspan=2, sticky='ew')
    title_packet(allergy_frame, "Allergy Information", 6)
    allergies = data.get('Allergies', {})
    info_packet(allergy_frame, "Medication Allergies: ",allergies.get("med_al", ''),7)
    info_packet(allergy_frame,"Food Allergies: ",allergies.get("food_al"),8)
    info_packet(allergy_frame,"Allergy Treatment: ",allergies.get("al_treat",''),9)

    #autism
    autism_frame=tk.Frame(frame, background="#80D1EA")
    autism_frame.grid(row=3, column=1, columnspan=2, sticky='ew')
    title_packet(autism_frame, "Autism Information", 10)
    autism = data.get("Autism", {})
    info_packet(autism_frame, "Autism Disorder: ",autism.get("aut_type", ''),11)
    info_packet(autism_frame,"Autism Trigger: ", autism.get("aut_trig", ''),12)
    info_packet(autism_frame, "Autism treatment: ",autism.get("aut_treat", ''),13)

    #cardiovascular risk
    cd_frame=tk.Frame(frame, background="#3396E8")
    cd_frame.grid(row=4, column=1,columnspan=2, sticky='ew')
    title_packet(cd_frame, "Cardiovascular Info", 14)
    cd_risk = data.get("Cardiovascular Disease", {})
    info_packet(cd_frame, "Cardiovascular Risk: ",cd_risk.get("CD_Risk"),15)

    #active medication list
    med_frame=tk.Frame(frame, background="#80D1EA")
    med_frame.grid(row=5, column=1, columnspan=2, sticky='ew')
    title_packet(med_frame, "Active Medications", 16)
    act_med = data.get("Active Medications", {})
    med_current = act_med.get("med_current", {})
    med_list=''
    for item in med_current:
        med_list += item + ': '+ med_current[item]+'\n'
    info_packet(med_frame,"List of Medications: ",med_list[:-1],17)

    #epilepsy
    epilepsy_frame=tk.Frame(frame, background="#3396E8")
    epilepsy_frame.grid(row=6, column=1,columnspan=2, sticky='ew')
    title_packet(epilepsy_frame, "Epilepsy Information",18)
    epilepsy = data.get("Epilepsy",{})
    info_packet(epilepsy_frame, "Epilepsy trigger: ",epilepsy.get("EP_trig", ''),19)
    info_packet(epilepsy_frame, "Epilepsy treatment: ", epilepsy.get("EP_treat", ''), 20)

    #mental illness
    men_ill_frame=tk.Frame(frame, bg="#80D1EA")
    men_ill_frame.grid(row=7, column=1, columnspan=2, sticky='ew')
    title_packet(men_ill_frame, "Mental Illness information", 21)
    men_ill = data.get("Mental Illness", {})
    info_packet(men_ill_frame, "Type of Mental Illness: ", men_ill.get("mi_type", ''), 22)
    info_packet(men_ill_frame, "Mental Illness trigger: ", men_ill.get("mi_trig", ''), 23)
    info_packet(men_ill_frame, "Mental Illness treatment: ", men_ill.get("mi_treat", ''), 24)

    #medical card info
    med_info_frame=tk.Frame(frame, background="#3396E8")
    med_info_frame.grid(row=8, column=1,columnspan=2, sticky='ew')
    title_packet(med_info_frame, "Medical Info", 25)
    med_info = data.get("Medical Info", {})
    info_packet(med_info_frame, "Insurance Company: ", med_info.get("ins_com", ''), 26)
    info_packet(med_info_frame, "Policy Number: ", med_info.get("pol_num", ''), 27)
    info_packet(med_info_frame, "Gorup Number: ", med_info.get("group_num", ''), 28)
    info_packet(med_info_frame, "Primary Care Provider: ", med_info.get("PCP", ''), 29)
    info_packet(med_info_frame, "     Phone Number: ", med_info.get("PCP_num", ''), 30)
    info_packet(med_info_frame, "Emergency Contact: ", med_info.get("emg_contact",''),31)
    info_packet(med_info_frame, "     Relation: ", med_info.get("emg_con_rel", ''), 32)
    info_packet(med_info_frame, "     Phone Number: ", med_info.get("emg_con_num", ''), 33)

    # Bind the on_configure function to the Configure event of the Canvas
    canvas.bind('<Configure>', on_configure)

    # Bind the on_mousewheel function to the MouseWheel event of the Canvas
    canvas.bind_all('<MouseWheel>', on_mousewheel)
    canvas.update_idletasks()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == '__main__':
    exec()