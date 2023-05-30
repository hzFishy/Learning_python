# Made by hzFishy, <https://github.com/hzFishy/Learning_python/blob/main/Apps/Alarm/App.py>
# Using python 3.9.7 64-bit
from tkinter import *
from datetime import *

# globals
global Gfont
Gfont = "Roboto"
global entries
entries = []
global colors
colors = {
    "bg0" : "#1E1E1E",
    "bg1" : "#2d2d2d",
    "bg2" : "#454545",
    "bg3" : "#3a3a3a",
    "white" : "#FFFFFF",
    "b0" : "#e0ffff",
    "b1" : "#69b4ff",
    "b2" : "#0085ff",
    "b3" : "#006fff",
    "gray" : "#9e9e9e",
}

# basic config
window = Tk()
window.title("Do It")
window.configure(bg=colors["bg0"])

window_width = 600
window_height = 700

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

middle_x = (screen_width - window_width) // 2
middle_y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{middle_x}+{middle_y}")
window.minsize(window_width,window_height)

### Content
def create_frame_Main():
    global frame_Main
    frame_Main = Frame(window, bg=colors["bg1"])
    frame_Main.pack(pady= 20, padx= 20,fill=BOTH,expand=True)
create_frame_Main()


def create_frame_buttons():
    global frame_buttons
    frame_buttons = Frame(window, bg=colors["bg1"])
    frame_buttons.pack(pady= 20, padx= 20, anchor=CENTER, side=TOP)   
create_frame_buttons()

def update_entries_stats(enable:bool):
    newstat = "normal" if enable == True else "disabled"
    for entry in entries:
        entry.config(state=f'{newstat}')
        try:
            entry.config(background=colors["b1"])
        except Exception:
            pass

# Timer Logic
def Timer_Ended(frame_StartedTime):
    window.lift()
    window.attributes('-topmost', True)
    update_entries_stats(False)
    print("Timer ended")
    def clearing():
        update_entries_stats(True)
        for entry in entries:
            try:
                entry.delete(0, END)
            except Exception:
                try: 
                    entry.delete("1.0", "end")
                except Exception:
                    pass
                
        clearbutton.destroy()
        frame_buttons.destroy()
        frame_StartedTime.destroy()
        window.attributes('-topmost', False)
        
    
    clearbutton = Button(frame_StartedTime, text="Clear ALL", relief=RAISED, command= clearing)
    clearbutton.pack(side=BOTTOM, padx=10, pady=10)

def currentlyOnTimer(Time):
    frame_StartedTime = Frame(frame_Main, bg=colors["bg2"])
    frame_StartedTime.pack(pady= 20, padx= 20)

    c1 = ["Timer started at: ", datetime.now().strftime("%H:%M:%S")]
    c2 = ["Timer ends at: ", Time]

    split_StartedTime = c1[1].split(":")
    split_EndTime = c2[1].split(":")




    def get_diff():
        dict_diffs = {
        "h" : {"diff" : False, "index" : 0},
        "m" : {"diff" : False, "index" : 0},
        "s" : {"diff" : False, "index" : 0}
        }
        def get_key_from_index(index):
            vs = ["h", "m", "s"]
            return vs[index]
    
        for index, (e1, e2) in enumerate(zip(split_StartedTime,split_EndTime)):
            print("============")
            print(e1,e2)
            if e1 != e2:
                dict_diffs[get_key_from_index(index)]["diff"] = True
        return dict_diffs

    print("diffs:", get_diff())



    label_StartedTime = Text(frame_StartedTime, height=1,width=len(c1[0])+len(c1[1]))
    label_StartedTime.insert("end","".join(c1))

    label_StartedTime.pack(padx = 10, pady= 10, side=LEFT)
    label_StartedTime.configure(state="disabled")

    
    label_EndTime = Text(frame_StartedTime, height=1,width=len(c2[0])+len(c2[1]))
    label_EndTime.insert("end", "".join(c2))
    label_EndTime.tag_configure("default", foreground="black")
    label_EndTime.tag_add("default", "1.0", f"1.{len(c2[0])}")
    label_EndTime.tag_configure("changed", foreground="red")


    for k_times, v_times in get_diff().items():
        if v_times["diff"] == True:
            label_EndTime.tag_add("changed", f"1.{v_times["index"]}", f"1.{v_times["index"]+2}")


    label_EndTime.pack(padx = 10, pady= 10, side=LEFT)
    label_EndTime.configure(state="disabled")

    return frame_StartedTime

def new_Timer(delay_data:str,is_spinbox:bool,Title:str,Message:str):
    print(f"Timer: {delay_data} \n {is_spinbox} \n Title: {Title} \n Message: {Message}")
    update_entries_stats(False)

    def delay_to_wait_seconds__hh_mm_ss(delay_data:str):
        delay_data = delay_data.split(":")
        h = int(delay_data[0])
        m = int(delay_data[1])
        s = int(delay_data[2])

        print(h,m,s)
        return (h*3600*1000 + m*60*1000 + s*1000), [h,m,s]

    def delay_to_wait_seconds__hh_mm(delay_data:str):
        delay_data = delay_data.split(":")
        h = int(delay_data[0])
        m = int(delay_data[1])
        print(h,m)
        return (h*3600*1000 + m*60*1000), [h, m, 0]

    if is_spinbox == False:
        delay_to_wait_seconds = delay_to_wait_seconds__hh_mm_ss(delay_data)
    else:
        delay_to_wait_seconds = delay_to_wait_seconds__hh_mm(delay_data)
    print(delay_to_wait_seconds)

    def currentTime_addDelay(delay_to_wait_seconds):
        delay_to_wait_seconds = delay_to_wait_seconds[1]
        currentTime = (datetime.now().strftime("%H:%M:%S")).split(":")
        h = int(currentTime[0])
        m = int(currentTime[1])
        s = int(currentTime[2])
        dh = delay_to_wait_seconds[0]
        dm = delay_to_wait_seconds[1]
        ds = delay_to_wait_seconds[2]

        return f"{h+dh}:{m+dm}:{s+ds}"
    
    dt2 = datetime.strptime((f"{delay_data}:00" if is_spinbox else delay_data), "%H:%M:%S")
    TimeResult = (datetime.now() + timedelta(hours=dt2.hour, minutes=dt2.minute, seconds=dt2.second)).strftime("%H:%M:%S")

    frame_StartedTime = currentlyOnTimer(TimeResult)
    
    window.after(delay_to_wait_seconds[0], lambda: Timer_Ended(frame_StartedTime))

def update_RealTime():
    heure_actuelle = datetime.now().strftime("%H:%M:%S")
    label_RealTime.config(text=heure_actuelle)
    window.after(1000, update_RealTime)

heure_actuelle = datetime.now().strftime("%H:%M:%S")
label_RealTime = Label(window, text=heure_actuelle, fg=colors["b0"], bg=colors["b1"],font=(Gfont,20,"bold"))

label_RealTime.pack()
window.after(1000, update_RealTime)


# Title
frame_Title = Frame(frame_Main, bg=colors["bg2"])
frame_Title.pack(pady= 20, padx= 20)

label_Title = Label(frame_Title , text = "Titre:",font=(Gfont,11), relief=SUNKEN, bg=colors["b3"])
label_Title.pack(padx = 10, pady= 10, side = LEFT)


def callback_input_Title():
    spawn_jobbutton()

content_input_Title = StringVar()
content_input_Title.trace("w", lambda  name, index, mode : callback_input_Title())

input_Title = Entry(frame_Title, width=50, fg = 'red',bg=colors["b1"], textvariable=content_input_Title)
input_Title.pack(padx = 10, pady= 10)
entries.append(input_Title)

# Description
frame_Description = Frame(frame_Main, bg=colors["bg2"])
frame_Description.pack(pady= 10, padx= 10,fill=BOTH,expand=True)

label_Description = Label(frame_Description , text = "Description:",font=(Gfont,11), relief=SUNKEN, bg=colors["b3"])
label_Description.pack(padx = 10, pady= 10)

input_Description = Text(frame_Description, height=5,fg = 'black',bg=colors["b1"])
input_Description.pack(fill=BOTH,expand=True,padx = 10, pady= 10)
entries.append(input_Description)

# Time
frame_Time = Frame(frame_Main, bg=colors["bg3"])
frame_Time.pack(pady= 20, padx= 20, anchor=CENTER)

label_Time = Label(frame_Time , text = "Durée:",font=(Gfont,11), bg=colors["b3"], relief=SUNKEN)
label_Time.pack(padx = 10, pady= 10, side = LEFT)

def callback_input_Time(data):
    flen = len((data.get()).replace(":",""))
    if flen > 6:
        input_Time.delete(len(data.get())-1)
    if flen < 6:
        if flen == 2 or flen == 4:
            input_Time.insert("end", ":")

content_input_Time = StringVar()
content_input_Time.trace("w", lambda  name, index, mode, content_input_Time=content_input_Time: callback_input_Time(content_input_Time))

input_Time = Entry(frame_Time, textvariable=content_input_Time)
input_Time.config(fg = 'blue')
input_Time.pack(padx = 10, pady= 10)
entries.append(input_Time)

spinbox_Time = Spinbox(frame_Time, values=([f"{hour:02d}:00" for hour in range(0,25,2)]))
spinbox_Time.pack(side = RIGHT,padx = 10, pady= 10)
entries.append(spinbox_Time)

jobbutton = Button(frame_buttons,text="Ajouter",relief=RAISED, bg=colors["b2"] ,
        command= lambda: 
        new_Timer(
    input_Time.get() if input_Time.get() != "" else spinbox_Time.get(),
    False if input_Time.get() != "" else True,
    input_Title.get(),
    input_Description.get("1.0",'end-1c').replace("\n", " "))
    )
def spawn_jobbutton():
    jobbutton.pack(side=LEFT, padx=10,pady=10)
entries.append(jobbutton)


window.mainloop()