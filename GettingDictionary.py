import random


def buscar_paraules():
    """
    Script per traspassar les paraules desde un .txt amb paraules en ranking
    (primeres-2000-paraules.txt) a un altre .txt amb el format necessari per
    poder ser usable per el programa(MyDict.txt).
    """
    with open("primeres-2000-paraules.txt", "r", encoding='utf8') as f:
        inputs = f.read().split('\n')
    f.close()

    n = 0

    this_lst = []
    defstr = ''

    for paraula in inputs:
        try:
            this_lst.append(paraula.split(' ')[1])
        except IndexError:
            pass

    for paraula in this_lst:
        if n % 100 == 0:
            defstr += '\n'
        defstr += '|' + paraula
        n += 1
    defstr += '|'

    fw = open("MyDict.txt", "w", encoding='utf8')
    fw.write(defstr[1:])
    fw.close()


def gettingmydict():
    """
    Llegeix el diccionari i les posa en una llista que és usable per el programa.
    :return: Retorna una llista amb les 2000 paraules més usades del català.
    """
    mydict = []
    with open("MyDict.txt", "r", encoding='utf8') as f:
        inputs = f.read().split('\n')
    f.close()
    for nivell in inputs:
        mydict.append(nivell.split('|')[1:])
    return mydict


def selectphrase(usablelst, diff):
    """
    Selecciona la frase final per escruire.
    :param usablelst: Les 2000 paraules més comunes del català.
    :param diff: Dificultat que limitarà quines paraules poden ser seleccionades
    :return: Retorna la frase final de com a mínim 55 caràcters
    """
    this_phrase = ''
    while len(this_phrase) <= 55:  # la frase seleccionada tindrà com a mínim 55 caràcters
        this_rand = random.random()
        if 0 <= this_rand < .3:
            if diff == 500:
                this_phrase += usablelst[0][random.randint(0, 99)] + ' '
            elif diff == 1000:
                this_phrase += usablelst[random.randint(0, 1)][random.randint(0, 99)] + ' '
            elif diff == 1500:
                this_phrase += usablelst[random.randint(0, 2)][random.randint(0, 99)] + ' '
            elif diff == 2000:
                this_phrase += usablelst[random.randint(0, 3)][random.randint(0, 99)] + ' '
        elif .3 <= this_rand < .55:
            if diff == 500:
                this_phrase += usablelst[1][random.randint(0, 99)] + ' '
            elif diff == 1000:
                this_phrase += usablelst[random.randint(2, 3)][random.randint(0, 99)] + ' '
            elif diff == 1500:
                this_phrase += usablelst[random.randint(3, 5)][random.randint(0, 99)] + ' '
            elif diff == 2000:
                this_phrase += usablelst[random.randint(4, 7)][random.randint(0, 99)] + ' '
        elif .55 <= this_rand < .75:
            if diff == 500:
                this_phrase += usablelst[2][random.randint(0, 99)] + ' '
            elif diff == 1000:
                this_phrase += usablelst[random.randint(4, 5)][random.randint(0, 99)] + ' '
            elif diff == 1500:
                this_phrase += usablelst[random.randint(6, 8)][random.randint(0, 99)] + ' '
            elif diff == 2000:
                this_phrase += usablelst[random.randint(8, 11)][random.randint(0, 99)] + ' '
        elif .75 <= this_rand < .9:
            if diff == 500:
                this_phrase += usablelst[3][random.randint(0, 99)] + ' '
            elif diff == 1000:
                this_phrase += usablelst[random.randint(6, 7)][random.randint(0, 99)] + ' '
            elif diff == 1500:
                this_phrase += usablelst[random.randint(9, 11)][random.randint(0, 99)] + ' '
            elif diff == 2000:
                this_phrase += usablelst[random.randint(12, 15)][random.randint(0, 99)] + ' '
        elif .9 <= this_rand <= 1:
            if diff == 500:
                this_phrase += usablelst[4][random.randint(0, 99)] + ' '
            elif diff == 1000:
                this_phrase += usablelst[random.randint(8, 9)][random.randint(0, 99)] + ' '
            elif diff == 1500:
                this_phrase += usablelst[random.randint(12, 14)][random.randint(0, 99)] + ' '
            elif diff == 2000:
                this_phrase += usablelst[random.randint(16, 19)][random.randint(0, 99)] + ' '
        else:
            raise Exception("Error en el grau de dificultat")
    return this_phrase[:-1]
