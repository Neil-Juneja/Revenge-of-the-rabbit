import tkinter as tk
from tkinter import messagebox as mb
import sys,pygame,os,pickle
import tkinter.font as tkfont
from tkinter import ttk as ttk
import traceback
pygame.init()

# opinions for font,music,sound effects, backgrounds
def button(win,x,y,text,color,command,width=8,height=4):
    but=tk.Button(win,text=text,bg=color,command=command)
    but.place(x=x,y=y)
def exit_():
    global second_window
    second_window.destroy()


    
def levels():
    levelwid=second_window_width-375
    levelhi=second_window_height-150
    insidew=2900
    levelcan=tk.Canvas(second_window,width=levelwid,height=levelhi)
    levelframe=tk.Frame(levelcan,bg='black',width=insidew,height=levelhi)
    levelscroll=tk.Scrollbar(levelframe,bg='black',troughcolor='white')
    levelcan.config(xscrollcommand=levelscroll.set,highlightthickness=0,scrollregion=levelcan.bbox('all'))
    levelscroll.config(orient='horizontal',command=levelcan.xview)
    levelcan.place(x=350,y=75)
    levelframe.place(x=0,y=0)
    levelscroll.place(x=0,y=levelhi-15,width=insidew)
    '''def on_mouse_wheel(event)a:
        if event.num == 4:
            levelcan.yview_scroll(-1, "units")  # Scroll up
        elif event.num == 5:
            levelcan.yview_scroll(1, "units")  # Scroll down'''
    def on_mouse_wheel(event):
        levelcan.yview_scroll(-1 * int(event.delta / 120), "units")
    # Bind mouse wheel event to Canvas for scrolling
    levelcan.create_window((0,0),window=levelframe,anchor='nw',tags=levelframe)
    
    def levframe(x,levnum):
        frame=tk.Frame(levelframe,width=300,height=levelhi-40,bg='firebrick')
        frame.place(x=x,y=20)
        namelab=tk.Label(frame,bg='grey',text='Level'+levnum,font=tkfont.Font(size=50,weight=tkfont.BOLD,family='courier new'))
        namelab.place(x=25,y=30)
        levnumreal='level'+levnum
        fox=open('datasheet.dat','rb')
        try:
            data_=pickle.load(fox)
        except EOFError:
            pass
        ##########################################333
        fox.seek(0)
        fox.close()
        for i in data_:
            if i ==levnumreal: 
                btime=str(data_[i][0])
                if btime=='0':
                    statlab=tk.Label(frame,bg='firebrick',text="Best time:No time",font=tkfont.Font(size=20,weight=tkfont.BOLD,family='courier new'))
                else:
                    statlab=tk.Label(frame,bg='firebrick',text="Best time:"+btime+'s',font=tkfont.Font(size=20,weight=tkfont.BOLD,family='courier new'))
                if len(data_[i])>1:
                    fullhealth=tk.Label(frame,bg='firebrick',text='ACHEIVEMENT\nDid not lose any health')
                    fullhealth.place(x=25,y=400)
        statlab.place(x=15,y=300)
        
        def level1():
            levnumreal='level'+levnum
            fox=open('control_config.dat','rb')
            try:
                data__=pickle.load(fox)
            except EOFError:
                pass
            ##################################################
            fox.seek(0)
            fox.close()
            data__['level']=levnumreal
            fox=open('control_config.dat','wb')
            pickle.dump(data__,fox)
            fox.close()
            try:
                exit_()
                sys.path.append('monkey2.py')
                import monkey2
                exit()
            except tk.TclError:
                traceback.print_exc()
        playbutton=tk.Button(frame,text='Play',bg='orangered',width=25,height=2,command=level1)
        playbutton.place(x=60,y=200)


    def updatescroll():
        levelcan.update_idletasks()
        levelcan.config(scrollregion=levelcan.bbox('all'))
        #levelcan.create_window(0,0,window=levelframe,anchor=tk.NW)
    levelcan.focus_set()
    levelcan.bind("<MouseWheel>", on_mouse_wheel)
    levframe(20,'1')
    levframe(340,'2')
    levframe(660,'3')
    levframe(980,'4')
    levframe(1300,'5')
    levframe(1620,'6')
    levframe(1940,'7')
    levframe(2260,'8')
    levframe(2580,'9')

    updatescroll()
    levelframe.mainloop()

def control():
    def which(action,ymult):
        control_config=open('control_config.dat','rb')
        global data
        while True:
            try:
                data=pickle.load(control_config)
            except EOFError:
                break
        dictword=data[action]
        #################################################3333
        control_config.seek(0)
        control_config.close()
    which('jump',50)


    def key_binding_widget(color, text_size, button_size, label_size, control_dict, key, distance,x,y):
        def update_key_binding(event):
            new_key = event.keysym
            checkdict={'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j','k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't','u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '0': '0', '1': '1', '2': '2', '3': '3','4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'space': 'SPACE', 'backspace': 'BACKSPACE','tab': 'TAB', 'return': 'RETURN', 'escape': 'ESCAPE', 'delete': 'DELETE', 'Shift_L': 'LSHIFT','Shift_R':'RSHIFT', 'Control_L': 'LCTRL','Condtrol_R':'RCTRL','Alt_L': 'LALT','Alt_R':'RALT', 'command': 'LGUI', 'right shift': 'RSHIFT', 'right control': 'RCTRL', 'right alt': 'RALT','right command': 'RGUI', 'caps lock': 'CAPSLOCK', 'home': 'HOME', 'end': 'END', 'insert': 'INSERT','page up': 'PAGEUP', 'page down': 'PAGEDOWN', 'Up': 'UP', 'Down': 'DOWN', 'Left': 'LEFT', 'Right': 'RIGHT','f1': 'F1', 'f2': 'F2', 'f3': 'F3', 'f4': 'F4', 'f5': 'F5', 'f6': 'F6', 'f7': 'F7', 'f8': 'F8', 'f9': 'F9','f10': 'F10', 'f11': 'F11', 'f12': 'F12', 'num lock': 'NUMLOCK', 'scroll lock': 'SCROLLLOCK','semicolon': 'SEMICOLON', 'apostrophe': 'QUOTE', 'comma': 'COMMA', 'period': 'PERIOD', 'slash': 'SLASH','backslash': 'BACKSLASH', 'minus': 'MINUS', 'equal': 'EQUALS', 'bracketleft': 'LEFTBRACKET','bracketright': 'RIGHTBRACKET', 'grave': 'BACKQUOTE', 'print': 'PRINTSCREEN', 'kp0': 'KP_0', 'kp1': 'KP_1','kp2': 'KP_2', 'kp3': 'KP_3', 'kp4': 'KP_4', 'kp5': 'KP_5', 'kp6': 'KP_6', 'kp7': 'KP_7', 'kp8': 'KP_8','kp9': 'KP_9', 'kp divide': 'KP_DIVIDE', 'kp multiply': 'KP_MULTIPLY', 'kp subtract': 'KP_MINUS','kp add': 'KP_PLUS', 'kp enter': 'KP_ENTER', 'kp period': 'KP_PERIOD'}
            #FIXXXXXXXXXXXxx
            for i in checkdict:
                if i==new_key:
                    for j in data:
                        if data[j]==checkdict[i]:
                            new_key=data[key]
                            break
                    else:
                        new_key=checkdict[i]
                        data[key] = new_key
                    break
            else:
                new_key=data[key]
            button.config(text=new_key)
            prompt_label.place_forget()
            levelframe.unbind('<KeyPress>', key_binding_id)
            #
            fox=open('control_config.dat','wb')
            pickle.dump(data,fox)
            fox.close()
        def on_button_click():
            prompt_label.place(x=button.winfo_x(), y=button.winfo_y())
            global key_binding_id
            levelframe.focus_set()
            key_binding_id = levelframe.bind('<KeyPress>', update_key_binding)


        label = tk.Label(levelframe, text=key, bg=color, fg="white", font=("courier new", text_size), width=label_size[0], height=label_size[1])
        label.place(x=x,y=y)
        button = tk.Button(levelframe, text=control_dict[key], bg=color, fg="white", font=("courier new", text_size), width=button_size[0], height=button_size[1], command=on_button_click)
        button.place(x=x+distance,y=y)
        prompt_label = tk.Label(levelframe, text="Enter new key binding", bg=color, fg="white", font=("courier new", text_size))

    def updatescroll():
        levelcan.update_idletasks()
        levelcan.config(scrollregion=levelcan.bbox('all'))
    levelwid=second_window_width-375
    levelhi=second_window_height-150
    insidew=2000
    levelcan=tk.Canvas(second_window,width=levelwid,height=levelhi)
    levelframe=tk.Frame(levelcan,bg='black',width=levelwid,height=insidew)
    levelscroll=tk.Scrollbar(levelframe,bg='maroon',troughcolor='maroon')
    levelcan.config(yscrollcommand=levelscroll.set,highlightthickness=0,scrollregion=levelcan.bbox('all'))
    levelscroll.config(orient='vertical',command=levelcan.yview)
    levelcan.place(x=350,y=75)
    levelframe.place(x=0,y=0)
    levelscroll.place(x=levelwid-15,y=0,height=insidew)
    
    levelcan.create_window((0,0),window=levelframe,anchor='nw',tags=levelframe)
    levelcan.focus_set()
    key_binding_widget(color="green", text_size=20, button_size=(10, 2), label_size=(10, 2), control_dict=data, key="jump",distance=400,x=100,y=100)
    key_binding_widget(color="green", text_size=20, button_size=(10, 2), label_size=(10, 2), control_dict=data, key="left",distance=400,x=100,y=200)
    key_binding_widget(color="green", text_size=20, button_size=(10, 2), label_size=(10, 2), control_dict=data, key="right",distance=400,x=100,y=300)
    key_binding_widget(color="green", text_size=20, button_size=(10, 2), label_size=(10, 2), control_dict=data, key="range",distance=400,x=100,y=400)
    key_binding_widget(color="green", text_size=20, button_size=(10, 2), label_size=(10, 2), control_dict=data, key="melee",distance=400,x=100,y=500)            
    updatescroll()
    levelframe.mainloop()

def introscreen():
    def end():
        global first_window
        first_window.destroy()
        secondscreen()


    global first_window
    first_window=tk.Tk()
    first_window.title("intro_screen")
    first_window_width=first_window.winfo_screenwidth()
    first_window_height=first_window.winfo_screenheight()
    first_window.geometry(str(first_window_width)+'x'+str(first_window_height))
    first_window.attributes('-fullscreen',True)
    first_window.configure(bg='grey')
    #win_.attributes('-topmost',True)
    first_bg=tk.PhotoImage(file='beta_menu_.png')
    first_bg__=pygame.image.load(os.path.join('beta_menu_.png'))
    first_mainframe=tk.Frame(first_window,width=800,height=650)
    first_mainframe.place(y=(first_window_height/2)-first_bg__.get_height()/2,x=first_window_width/2-first_bg__.get_width()/2)
    background=tk.Label(first_mainframe,image=first_bg)
    background.place(x=-2,y=-2)
    button(first_window,200,250,'begin','grey',end)
    button(first_window,200,200,'exit','red',exit_)
    first_window.mainloop()

def secondscreen():
    global second_window,second_window_height,second_window_width,menu_frame
    second_window=tk.Tk()
    second_window.title("main_menu")
    second_window_width=second_window.winfo_screenwidth()
    second_window_height=second_window.winfo_screenheight()
    second_window.geometry(str(str(second_window_width)+'x'+str(second_window_height)))
    second_window.attributes('-fullscreen',True)
    second_window.configure(bg='maroon')

    menu_frame=tk.Frame(second_window,width=300,height=second_window_height-150)
    menu_frame.configure(bg='black')
    menu_frame.place(x=25,y=75)
    introlabel_name1=tk.Label(menu_frame,bg='black',fg='firebrick',text='Revenge',font=tkfont.Font(size=40,weight=tkfont.BOLD,family='courier new'))
    introlabel_name1.place(x=menu_frame.winfo_width()/2+introlabel_name1.winfo_width()/2,y=10)
    introlabel_name2=tk.Label(menu_frame,bg='black',fg='firebrick',text='Of The',font=tkfont.Font(size=15,weight=tkfont.BOLD,family='courier new'))
    introlabel_name2.place(x=menu_frame.winfo_width()/2+introlabel_name1.winfo_width()/2+200,y=80)
    introlabel_name3=tk.Label(menu_frame,bg='black',fg='firebrick',text='Rabbit',font=tkfont.Font(size=60,weight=tkfont.BOLD,family='courier new'))
    introlabel_name3.place(x=menu_frame.winfo_width()/2+introlabel_name1.winfo_width()/2,y=110)    
    
    #playbutton
    playbut=tk.Button(menu_frame,borderwidth=0,activebackground='black',width=12,height=1,fg='tomato',text='Play',bg='black',command=levels,font=tkfont.Font(size=20,weight=tkfont.BOLD,family='courier new'))
    playbut.place(x=60,y=300)
    #control config
    controlbut=tk.Button(menu_frame,borderwidth=0,activebackground='black',width=12,height=1,fg='tomato',text='controls',bg='black',command=control,font=tkfont.Font(size=20,weight=tkfont.BOLD,family='courier new'))
    controlbut.place(x=60,y=400)

    #exitbutton
    exitbut=tk.Button(menu_frame,borderwidth=0,activebackground='black',width=12,height=1,fg='tomato',text='Quit',bg='black',command=exit_,font=tkfont.Font(size=20,weight=tkfont.BOLD,family='courier new'))
    exitbut.place(x=60,y=550)
    second_window.mainloop()
#introscreen()
secondscreen()
