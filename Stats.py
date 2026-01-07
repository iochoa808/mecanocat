import matplotlib.pyplot as plt
import datetime


def velcalc(chars, t):
    """
    Calcula la velocitat mitjana.
    :param chars: Número de caràcters.
    :param t: Segons que ha trigat en escriure tots els caràcters.
    :return: Retorna la velocitat mitjana.
    """
    try:
        return round(chars / (t / 60))
    except ZeroDivisionError:
        return 0


def grabarstats(pers, char, t, err, diff):
    """
    Graba les estadístiques al document adient.
    :param pers: El perfil al qual se li afegiran totes les dades.
    :param char: Número de caràcters.
    :param t: Segons que ha trigat en escriure tots els caràcters.
    :param err: Els errors que ha fet en aquest període de temps.
    :param diff: La dificultat.
    :return: No retorna res, però graba totes aquestes dades al document amb el nom adient.
    """
    stats = open(f"Stats{pers}.txt", "a", encoding='utf8')
    dia = str(datetime.datetime.now()).split(' ')[0]
    defstr = str([pers, char, round(t, 2), err, diff, str(dia)])
    stats.write(defstr + '\n')
    stats.close()


def getstats(pers):
    """
    Aconsegueix una llista amb totes les dades anteriors del perfil adient.
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna un diccionari amb cada dada etiquetada amb el seu títol adient. Si el document està buit retornarà
    None
    """
    stats = open(f"Stats{pers}.txt", "r", encoding='utf8')
    inputs = stats.read().split('\n')
    stats.close()
    if len(inputs) >= 1:
        mylst = ['Pers', 'char', 't', 'err', 'diff', 'dia']
        deflst = []
        for datapoint in inputs:
            if len(datapoint) > 1:
                this_lst = datapoint.strip('][').split(', ')
                deflst.append(dict(zip(mylst, this_lst)))
        return deflst
    else:
        return None


def getante(pers):
    """
    Agafa les dades anteriors i així poder-les mostrar
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna les últimes dades guradades. Si el document està buit retorna un string 'n/a' que vol dir que no hi
    ha dades.
    """
    try:
        return getstats(pers)[-1]
    except IndexError:
        return 'n/a'


def getantevel(pers):
    """
    Calcula la darrera velociat grabada.
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna la darrera velocitat. Si el document està buit retorna un string 'n/a' que vol dir que no hi
    ha dades.
    """
    try:
        return str(velcalc(int(getante(pers).get('char')), float(getante(pers).get('t'))))
    except AttributeError:
        return 'n/a'


def getanteerr(pers):
    """
    Agafa els derrers errors grabats.
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna un string amb els errors anteriars. Si el document està buit retorna un string 'n/a' que vol dir
    que no hi ha dades.
    """
    try:
        return str(getante(pers).get('err'))
    except AttributeError:
        return 'n/a'


def getvelmitjdia(pers):
    """
    Calcula la velocitat mitjana en tota la història del perfil.
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna la velocitat mitjana. Si el document està buit retorna un string 'n/a' que vol dir que no hi
    ha dades.
    """
    sumchar = 0
    sumtemp = 0
    for elem in getstats(pers):
        if elem.get('dia') == "'" + str(datetime.datetime.now()).split(' ')[0] + "'":
            sumchar += int(elem.get('char'))
            sumtemp += float(elem.get('t'))
        else:
            pass
    try:
        return str(round(sumchar / round(sumtemp / 60, 4), 2))
    except ZeroDivisionError:
        return 'n/a'


def geterrmitjdia(pers):
    """
    Calcula els errors mitjans de tota la història del perfil.
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna els errors mitjans. Si el document està buit retorna un string 'n/a' que vol dir que no hi
    ha dades.
    """
    sumerr = 0
    lst = getstats(pers)
    for elem in lst:
        if elem.get('dia') == "'" + str(datetime.datetime.now()).split(' ')[0] + "'":
            sumerr += int(elem.get('err'))
        else:
            pass
    try:
        return str(round(sumerr / len(lst), 2))
    except ZeroDivisionError:
        return 'n/a'


def getlindia(pers):
    """
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna el nombre de linies que ha fet el perfil seleccionat el mateix dia.
    """
    n = 0
    lst = getstats(pers)
    for linia in lst:
        if linia.get('dia') == "'" + str(datetime.datetime.now()).split(' ')[0] + "'":
            n += 1
    return str(n)


def getvelmitjtot(pers):
    """
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna la mitjana de la velociata del perfil seleccionat.
    """
    stats = getstats(pers)
    sumchar = sumtemp = 0
    for linia in stats:
        sumchar += int(linia.get('char'))
        sumtemp += float(linia.get('t'))
    try:
        return str(round(sumchar / round(sumtemp / 60, 4), 2))
    except ZeroDivisionError:
        return 'n/a'


def geterrmitjtot(pers):
    """
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna la mitjana total del nombre d'errors que ha fet el perfil seleccionat.
    """
    stats = getstats(pers)
    sumerr = 0
    for linia in stats:
        sumerr += int(linia.get('err'))
    try:
        return str(round(sumerr / len(stats), 2))
    except ZeroDivisionError:
        return 'n/a'


def getlintot(pers):
    """
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna el nombre total de linies que s'han fet mai en el perfil seleccionat.
    """
    return str(len(getstats(pers)))


def getdata(pers):
    """
    Aconsegueix les dades de manera que es puguin fer servir per la gràfica.
    :param pers: Perfil al qual se li agafen les dades.
    :return: Retorna, en un format utilitzable per la funció per fer gràfics: el número de repeticions que s'han fet en
    aquest perfil i la velocitat i els errors junts.
    """
    vel = []
    errs = []
    reps = [n for n in range(1, len(getstats(pers)) + 1)]

    for elem in getstats(pers):
        vel.append(round(velcalc(int(elem['char']), float(elem['t']))))
        errs.append(int(elem['err']) * 20)
    return reps, [vel, errs]


def graphic(pers):
    """
    Crea una finestra amb un gràfic representant la progressió de la persona.
    :param pers: Perfil al qual se li agafen les dades.
    :return: No retorna res però crea uan finestra amb el gràfic.
    """
    eixos = getdata(pers)

    plt.figure("Progressió al llarg del temps")
    plt.plot(eixos[0], eixos[1][0], label='Velociat', color='#2EBD55')
    plt.plot(eixos[0], eixos[1][1], label='Errors', color='#F43131')

    plt.xlabel('Línies')
    plt.ylabel('Velocitat  i els Errors(x20)')
    plt.title('Progressió')

    plt.legend()
    plt.tight_layout()
    plt.show()
