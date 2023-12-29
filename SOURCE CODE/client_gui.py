from environs import Env

data = Env()
data.read_env("env_secure.env")

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

