from dotenv import set_key
import tkinter as tk, hashlib
from environs import Env

password='FIRST TIME'

def init_root_screen():
    root = tk.Tk()
    
    title=tk.Label(root, text="SET VITALINK PASSWORD")
    title.grid(column=1, row=1, columnspan=2)

    cur_pass_lbl=tk.Label(root, text="Input Current Password: ")
    cur_pass_lbl.grid(column=1, row=2, columnspan=1)
    cur_pass_entry=tk.Entry(root)
    cur_pass_entry.grid(column=2, row=2, columnspan=1)

    new_pass_lbl=tk.Label(root, text="Input New Password: ")
    new_pass_lbl.grid(column=1, row=3, columnspan=1)
    new_pass_entry=tk.Entry(root)
    new_pass_entry.grid(column=2, row=3, columnspan=1)
    
    cfrm_pass_lbl=tk.Label(root, text="Confirm new Password")
    cfrm_pass_lbl.grid(column=1, row=4, columnspan=1)
    cfrm_pass_entry=tk.Entry(root)
    cfrm_pass_entry.grid(column=2, row=4, columnspan=1)

    sbmt_btn=tk.Button(root, text="Submit", command=root.quit)
    sbmt_btn.grid(column=1, row=5, columnspan=2)

    root.mainloop()

    try_set_key(cur_pass_entry.get(),
                new_pass_entry.get(),
                cfrm_pass_entry.get(), root)
    
def try_set_key(cur_pass,new_pass,cfrm_pass, root):
    root.destroy()
    hash = Env()
    hash.read_env("env_hash.env")
    password=hashlib.new("SHA512", hash("HASH").encode()).hexdigest()
    if cur_pass != password:
        ERROR_GUI("Incorrect Password")
        init_root_screen()
    if new_pass != cfrm_pass:
        ERROR_GUI("Passwords do not match")
        init_root_screen()
    else:
        set_key("env_hash.env", 
                key_to_set="HASH", 
                value_to_set=hashlib.new("SHA512", 
                                        new_pass.encode()
                                ).hexdigest()
        )
    
def ERROR_GUI(err_msg):
    err_root=tk.Tk()
    error_lbl=tk.Label(err_root, text="ERROR 400:")
    err_msg_lbl=tk.Label(err_root, text=err_msg)
    error_lbl.grid(row=1, column=1, columnspan=1)
    err_msg_lbl.grid(row=2, column=1, columnspan=1)

    cls_btn = tk.Button(err_root, text="Close", command=err_root.destroy)
    cls_btn.grid(column=1, row=3, columnspan=1)
    err_root.mainloop()