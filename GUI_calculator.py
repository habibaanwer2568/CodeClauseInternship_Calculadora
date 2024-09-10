import tkinter as tk
import pygame
from PIL import Image , ImageTk, ImageSequence
import itertools


calc = ""
root = tk.Tk()
root.geometry("324x538")
root.configure(bg="#ffffff")
root.title("Calculadora")

result_box = tk.Text(root , height=2 , width=17 , font=("Arial" , 24) )
result_box.grid(columnspan=5)

def add_to_calc(char) :
    play_btn_sound()
    global calc
    calc += str(char)
    result_box.delete(1.0 , "end")
    result_box.insert(1.0 , calc)

def eval_calc() :
    result_soundd()
    global calc
    try :
        calc= str(eval(calc))
        result_box.delete(1.0 , "end")
        result_box.insert(1.0, calc)
    except:
        clear_field()
        result_box.insert(1.0 , "Error")


def del_last() :
    play_btn_sound()
    current_txt = result_box.get(1.0 , tk.END).strip()
    result_box.delete(1.0 , tk.END)
    result_box.insert(1.0, current_txt[:-1])

def clear_field() :
    play_btn_sound()
    global calc
    calc = ""
    result_box.delete(1.0, "end")

pygame.mixer.init()
click_sound = pygame.mixer.Sound("mixkit-modern-technology-select-3124.wav")
result_sound = pygame.mixer.Sound("mixkit-space-coin-win-notification-271.wav")
def play_btn_sound() :
    click_sound.play()

def result_soundd():
    result_sound.play()

gif_path = "1047355246-preview.gif"
image = Image.open(gif_path)

frames = [ ImageTk.PhotoImage(frame.resize((75,55), Image.LANCZOS )) for frame in  ImageSequence.Iterator(image) ]

def animate_gif(frame_idx = 0) :
    gif_label.config(image=frames[frame_idx])
    frame_idx = (frame_idx+1) % len(frames)
    root.after(100, animate_gif, frame_idx)

gif_label = tk.Label(root ,width=80, height=60)
gif_label.grid(row=1 , column= 2 )

animate_gif()



btn_1 = tk.Button(root , text="1" , command= lambda : add_to_calc(1), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff") 
btn_1.grid(row=2 , column= 1 , padx=5, pady=5)

btn_2 = tk.Button(root , text="2" , command= lambda : add_to_calc(2),width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_2.grid(row=2 , column= 2, padx=5, pady=5)

btn_3 = tk.Button(root , text="3" , command= lambda : add_to_calc(3), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_3.grid(row=2 , column= 3, padx=5, pady=5)

btn_4 = tk.Button(root , text="4" , command= lambda : add_to_calc(4), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_4.grid(row=3 , column= 1 , padx=5, pady=5)

btn_5 = tk.Button(root , text="5" , command= lambda : add_to_calc(5), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_5.grid(row=3 , column= 2, padx=5, pady=5)

btn_6 = tk.Button(root , text="6" , command= lambda : add_to_calc(6), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_6.grid(row=3 , column= 3, padx=5, pady=5)

btn_7 = tk.Button(root , text="7" , command= lambda : add_to_calc(7), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_7.grid(row=4 , column= 1, padx=5, pady=5)

btn_8 = tk.Button(root , text="8" , command= lambda : add_to_calc(8), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_8.grid(row=4 , column= 2, padx=5, pady=5)

btn_9 = tk.Button(root , text="9" , command= lambda : add_to_calc(9), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_9.grid(row=4 , column= 3, padx=5, pady=5)

btn_0 = tk.Button(root , text="0" , command= lambda : add_to_calc(0), width=5, height=2, font=("Arial" , 16), background="#8EACCD", fg="#ffffff")
btn_0.grid(row=5 , column= 2 , padx=5, pady=5)

btn_ = tk.Button(root , text="." , command= lambda : add_to_calc("."), width=5, height=2, font=("Arial" , 16), background="#ffffff", fg="#8EACCD")
btn_.grid(row=5 , column= 1, padx=5, pady=5)

btn_del = tk.Button(root , text="⌫" , command= del_last, width=5, height=2, font=("Arial" , 16), background="#ffffff", fg="#8EACCD")
btn_del.grid(row=5 , column= 3, padx=5, pady=5)

btn_c = tk.Button(root , text="C" , command= clear_field, width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_c.grid(row=1 , column= 1, padx=5, pady=5)
btn_mud = tk.Button(root , text="%" , command= lambda : add_to_calc("%"), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_mud.grid(row=1 , column= 3, padx=5, pady=5)
btn_div = tk.Button(root , text="÷" , command= lambda : add_to_calc("/"), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_div.grid(row=1 , column= 4, padx=5, pady=5)
btn_multi = tk.Button(root , text="x" , command= lambda : add_to_calc("*"), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_multi.grid(row=2 , column= 4, padx=5, pady=5)
btn_min = tk.Button(root , text="-" , command= lambda : add_to_calc("-"), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_min.grid(row=3 , column= 4, padx=5, pady=5)
btn_add = tk.Button(root , text="+" , command= lambda :  add_to_calc("+"), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_add.grid(row=4 , column= 4, padx=5, pady=5)

btn_open = tk.Button(root , text="(" , command= lambda : add_to_calc("("), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_open.grid(row=5 , column= 4, padx=5, pady=5)
btn_close = tk.Button(root , text="(" , command= lambda : add_to_calc(")"), width=5, height=2, font=("Arial" , 16), background="#D2E0FB", fg="#8EACCD")
btn_close.grid(row=6 , column= 4, padx=5, pady=5)

btn_equal = tk.Button(root , text="=" , command= eval_calc, width=18, height=2, font=("Arial" , 16), background="#E6A4B4", fg="#ffffff")
btn_equal.grid(row=6,column=1,columnspan=3, padx=5, pady=5)


root.mainloop()