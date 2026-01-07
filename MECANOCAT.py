import tkinter as tk
import tkinter.font as font
from pynput.keyboard import Key, Controller as KeyboardController
from time import time
import sys
import GettingDictionary as Gd
import Stats

keyboard = KeyboardController()

# Inicialitzant la finestra en pantalla completa.
root = tk.Tk()
root.attributes("-fullscreen", True)
width = root.winfo_screenwidth()

# Inicialitzant constants i globals
mylst = []
this_index = 0
errs = 0
mode = tk.StringVar()  # No el faig servir però es podria implementar fàcilment.
max_diff = 2000
MyDICT = []
diff = 500
temps = 0
text = Gd.selectphrase(Gd.gettingmydict(), diff)

# Introduint el nom de l'usuari.
current_perfil = input('Profile: ')

# Inicialitzant el document en el que les dades seran introduides.
try:
    f = open(f"Stats{current_perfil}.txt", "x", encoding='utf8')
    f.close()
except FileExistsError:
    pass

# Incicialitzant tots els Labels relacionats amb números.
vel_mitj_dia = Stats.getvelmitjdia(current_perfil)
err_mitj_dia = Stats.geterrmitjdia(current_perfil)
num_lin_dia = Stats.getlindia(current_perfil)

err_ante = Stats.getanteerr(current_perfil)
vel_ante = Stats.getantevel(current_perfil)

vel_mitj_tot = Stats.getvelmitjtot(current_perfil)
err_mitj_tot = Stats.geterrmitjtot(current_perfil)
num_lin_tot = Stats.getlintot(current_perfil)


# Tots els tipus de lletres utilitzants.
titolfont = font.Font(family='Courier', size=round((width * 25) / 1920), weight='bold')
normal = font.Font(family='Courier', size=round((width * 21) / 1920))
bold = font.Font(family='Courier', size=round((width * 21) / 1920), weight='bold')
butfont = font.Font(family='Courier', size=round((width * 15) / 1920))
medfont = font.Font(family='Courier', size=round((width * 15) / 1920), weight='bold')
smallfont = font.Font(family='Courier', size=round((width * 11) / 1920))

# Totes les lletres i caràcters que seràn acceptats.
abecedari = ["='a'", "='b'", "='c'", "='d'", "='e'", "='f'", "='g'", "='h'", "='i'", "='j'", "='k'", "='l'", "='m'",
             "='n'", "='o'", "='p'", "='q'", "='r'", "='s'", "='t'", "='u'", "='v'", "='w'", "='x'", "='y'", "='z'",
             "='ç'", "='ñ'", "='á'", "='à'", "='é'", "='è'", "='í'", "='ï'", "='ì'", "='ó'", "='ò'", "='ú'", "='ü'",
             "='ù'", "='A'", "='B'", "='C'", "='D'", "='E'", "='F'", "='G'", "='H'", "='I'", "='J'", "='K'", "='L'",
             "='M'", "='N'", "='O'", "='P'", "='Q'", "='R'", "='S'", "='T'", "='U'", "='V'", "='W'", "='X'", "='Y'",
             "='Z'", "='Ç'", "='Ñ'", "='Á'", "='À'", "='É'", "='È'", "='Í'", "='Ï'", "='Ì'", "='Ó'", "='Ò'", "='Ú'",
             "='Ü'", "='Ù'"]


def reset():
    """
    Fa un reset desprès d'haver acabat una línia, actualitza tots els Labels relacionats amb números i finalment guarda
    la informacó en el document adient
    """
    global this_index, errs, text, vel_mitj_dia

    this_time = time() - temps
    if this_index == len(text):
        Stats.grabarstats(current_perfil, len(text), this_time, errs, diff)

        Lbl_vel_mitj_dia.config(text='Velociat: ' + str(Stats.getvelmitjdia(current_perfil)))
        Lbl_err_mitj_dia.config(text='Errors: ' + str(Stats.geterrmitjdia(current_perfil)))
        Lbl_num_dia.config(text='Línies: ' + str(Stats.getlindia(current_perfil)))

        Lbl_vel_ante.config(text='Velocitat: ' + str(Stats.velcalc(len(text), this_time)))
        Lbl_err_ante.config(text='Errors: ' + str(errs))

        Lbl_vel_mitj_tot.config(text='Velocitat: ' + str(Stats.getvelmitjtot(current_perfil)))
        Lbl_err_mitj_tot.config(text='Errors: ' + str(Stats.geterrmitjtot(current_perfil)))
        Lbl_num_tot.config(text='Línies: ' + str(Stats.getlintot(current_perfil)))

    txt1.delete(0, len(txt1.get()) + 1)
    ref_bold.config(text='')

    text = '  ' + Gd.selectphrase(Gd.gettingmydict(), diff)
    ref.config(text=text)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

    errs = 0
    this_index = 2


def ajuda():
    """
    Obra el frame de la ajuda.
    """
    ajudaframe = tk.Frame(root, bg="#e6e6e6")
    ajudaframe.place(relwidth=0.94, relheight=0.94, relx=0.03, rely=0.03)
    sortir_ajuda = tk.Button(ajudaframe, text="tornar a\nl'inici", padx=10, pady=5, fg="black", bg="white",
                             command=lambda: ajudaframe.place_forget())
    sortir_ajuda.place(relx=0.5, rely=0.8)

    lbl_tit_aj = tk.Label(ajudaframe, text='AJUDA', fg='black', bg='#e6e6e6', font=titolfont)
    lbl_tit_aj.place(relx=0.45, rely=0.01)
    lbl_tit_expl = tk.Label(ajudaframe, text='Com es fa servir?', fg='black', bg='#e6e6e6', font=medfont)
    lbl_tit_expl.place(relx=0.05, rely=0.1)
    readme = open("README.txt", "r", encoding='utf8')
    inputs = readme.read()
    readme.close()
    lbl_expl = tk.Label(ajudaframe, text=inputs, fg='black', bg='#e6e6e6', font=butfont, justify='left')
    lbl_expl.place(relx=0.05, rely=0.15)


def diff_high():
    """
    Puja la dificultat.
    """
    global diff
    if diff != 2000:
        diff += 500
        diff_lbl.config(text="Dificultat\n\n\n" + str((diff/2000)*100))
        diff_explain.config(text=("Les " + str(diff) + ' paraules\nmés usades del català'))


def diff_low():
    """
    Baixa la dificultat.
    """
    global diff
    if diff != 500:
        diff -= 500
        diff_lbl.config(text="Dificultat\n\n\n" + str((diff/2000)*100))
        diff_explain.config(text=("Les " + str(diff) + ' paraules\nmés usades del català'))


def determinar_mode():
    """
    Funció que hauria funcionat com a selector de mode entre pràctica i showdown(un escriure el màxim de paraules amb 1
    minut). Al final no s'ha fet servir. En un futur no seria gaire difícil implementar-ho.
    """
    if mode.get() == 'PRÀCTICA':
        print('PRÀCTICA')
    else:
        print('SHOWDOWN')


def obrir_estadistica():
    """
    Obra la gràfica de matplotlib desde Stats.py
    """
    Stats.graphic(current_perfil)


def corregir(key):
    """
    Corregeix si la tecla és correcte/incorrecte segons la frase de referència.
    :param key: Tecla refinada a través de la funció listener
    """
    global this_index, errs, temps
    if len(txt1.get()) == 0:
        temps = time()
    try:
        if key == ' ':
            pass
        if key == text[this_index]:
            this_index += 1
            ref_bold.config(text=txt1.get() + key)
        else:
            ref.config(text=txt1.get() + key + text.partition(text[this_index:])[1])
            ref_bold.config(text=txt1.get() + key)
            errs += 1
        print('err: ', errs, key)
        print(len((txt1.get() + key)), len(text))
    except IndexError:
        reset()


def listener(key):
    """
    Detecta cada tecla premuda i la classifica.
    :param key: Input de cada tecla premuda al entry txt1
    :return: No retorna però envia cada tecla a la funció corregir
    """
    global this_index
    properties = str(key).split(' ')
    if properties[-3][4:] in abecedari:
        corregir(properties[-3][-2])

    elif properties[-3][4:] in abecedari:
        corregir(properties[-3][-2])

    elif properties[-5] == "keysym=BackSpace":
        try:
            ref_bold.config(text=txt1.get()[:-1])
            ref.config(text=txt1.get()[:-1] + text.partition(text[this_index:])[1])
        except ValueError:
            pass

    elif properties[-6] == "keysym=space":
        corregir(" ")

    elif properties[-5] == "keysym=quoteright":
        corregir("'")

    elif properties[-5] == "keysym=period":
        corregir(".")

    elif properties[-5] == "keysym=minus":
        corregir("-")

    elif properties[-5] == "keysym=periodcentered":
        corregir("·")

    elif properties[-5] == "keysym=Escape":
        reset()
    else:
        raise Exception(f"Caràcter introduit desconegut: {properties}")


def tancar():
    """
    Tanca l'aplicació
    """
    sys.exit()


# GUI
# MAIN GUI
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.94, relheight=0.94, relx=0.03, rely=0.03)

buttancar = tk.Button(root, text="✖", padx=10, pady=5, fg="black", bg="red", command=tancar)
buttancar.place(relx=0.98, rely=0)

titol = tk.Label(frame, text="MECANOCAT", font=titolfont, fg="black", bg="white")
titol.place(relx=0.4, rely=0.01)

But_ajud = tk.Button(frame, text="Ajuda", padx=10, pady=5, fg="black", bg="#e6e6e6", command=ajuda)
But_ajud.place(relx=0.01, rely=0.01)

Lbl_vel_ante = tk.Label(frame, text='Velocitat: ' + vel_ante, font=butfont, fg="black", bg="white")
Lbl_vel_ante.place(relx=0.38, rely=0.27)

Lbl_err_ante = tk.Label(frame, text='Errors: ' + err_ante, font=butfont, fg="black", bg="white")
Lbl_err_ante.place(relx=0.52, rely=0.27)

ref = tk.Label(frame, text=text, fg="black", bg="white", font=normal)
ref.place(relx=0.205, rely=0.35)

ref_bold = tk.Label(frame, text='', fg="black", bg="white", font=bold)
ref_bold.place(relx=0.205, rely=0.35)

txt1 = tk.Entry(frame, fg="black", font=bold)
txt1.place(relwidth=0.7, relheight=0.04, relx=0.205, rely=0.42)
txt1.bind("<Key>", listener)


# FRAME ESQUERRA
op_frame = tk.Frame(frame, bg="#e6e6e6", bd=5)
op_frame.place(relwidth=0.12, relheight=0.65, relx=0, rely=0.15)

# toggle que al final no va ser usat per canviar entre mode showdown i pràctica.
mode_toggle = tk.Checkbutton(op_frame, onvalue="SHOWDOWN", offvalue="PRÀCTICA", width=40, height=5, indicatoron=False,
                             variable=mode, textvariable=mode, background="white", command=determinar_mode,
                             font=butfont)
# mode.set("PRÀCTICA")
# mode_toggle.pack()

diff_lbl = tk.Label(op_frame, text="Dificultat\n\n\n" + str((diff/2000)*100), fg="black", font=butfont, bg='#e6e6e6')
diff_lbl.place(relx=.2, rely=0.42)

diff_minus = tk.Button(op_frame, text="-", padx=10, pady=5, fg="black", bg="white", font=butfont, command=diff_low)
diff_minus.place(relx=0, rely=0.5)

diff_plus = tk.Button(op_frame, text="+", padx=10, pady=5, fg="black", bg="white", font=butfont, command=diff_high)
diff_plus.place(relx=.75, rely=.5)

diff_explain = tk.Label(op_frame, text=("Les " + str(diff) + ' paraules\nmés usades del català'), bg='#e6e6e6',
                        font=smallfont)
diff_explain.place(relx=.01, rely=.6)


# FRAME DRETA
prof_frame = tk.Frame(frame, bg="#e6e6e6", bd=5)
prof_frame.place(relwidth=0.12, relheight=0.65, relx=0.88, rely=0.15)

perf_nom = tk.Label(prof_frame, text=current_perfil, font=bold, bg='#e6e6e6')
perf_nom.pack()

# Estadístiques diàries
Lbl_titol_diari = tk.Label(prof_frame, text='Estadísitques\ndiàries', font=medfont, bg='#e6e6e6')
Lbl_titol_diari.place(relx=.1, rely=.15)

Lbl_vel_mitj_dia = tk.Label(prof_frame, text='Velociat: ' + vel_mitj_dia, font=butfont, bg='#e6e6e6')
Lbl_vel_mitj_dia.place(relx=.01, rely=.25)

Lbl_err_mitj_dia = tk.Label(prof_frame, text='Errors: ' + err_mitj_dia, font=butfont, bg='#e6e6e6')
Lbl_err_mitj_dia.place(relx=.01, rely=.3)

Lbl_num_dia = tk.Label(prof_frame, text='Línies: ' + num_lin_dia, font=butfont, bg='#e6e6e6')
Lbl_num_dia.place(relx=.01, rely=.35)

# Estadístiques globals
Lbl_titol_tot = tk.Label(prof_frame, text='Estadístiques\nglobals', font=medfont, bg='#e6e6e6')
Lbl_titol_tot.place(relx=.1, rely=.45)

Lbl_vel_mitj_tot = tk.Label(prof_frame, text='Velocitat: ' + vel_mitj_tot, font=butfont, bg='#e6e6e6')
Lbl_vel_mitj_tot.place(relx=.01, rely=.55)

Lbl_err_mitj_tot = tk.Label(prof_frame, text='Errors: ' + err_mitj_tot, font=butfont, bg='#e6e6e6')
Lbl_err_mitj_tot.place(relx=.01, rely=.6)

Lbl_num_tot = tk.Label(prof_frame, text='Línies: ' + num_lin_tot, font=butfont, bg='#e6e6e6')
Lbl_num_tot.place(relx=.01, rely=.65)

# Botó per veure la gràfica del progrés
but_estadis = tk.Button(prof_frame, text="Gràfica del\n progrés", fg="black",
                        bg='#d0d3d4', font=smallfont, command=obrir_estadistica)
but_estadis.place(relx=0.1, rely=0.8, relwidth=.8, relheight=0.15)

root.mainloop()
