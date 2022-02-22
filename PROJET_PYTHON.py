import csv
from datetime import date
with open("/home/abdou/PYTHON/Note_eleve.csv", 'r') as Note:
    myReader = csv.reader(Note)

    liste =[]
    listeinv =[]
    p=0

    def check_date(Date):
        chaine = ",;:' '._-"
        for i in chaine:
                Date = Date.replace(i,"/")
                Date = Date.strip()
        return Date


#################################################################
    def mois(x):
        x =x.lower()
        if x in "janvier":
            return "01"
        elif x in ["fev","fèv","février"]:
            return "02"
        elif x in "mars":
            return "03"
        elif x in "avril":
            return "04"
        elif x in "mai":
            return "05"
        elif x in "juin":
            return "06"
        elif x in "juillet":
            return "07"
        elif x in ["aout","août"]:
            return "08"
        elif x in "septembre":
            return "09"
        elif x in "octobre":
            return "10"
        elif x in "novembre":
            return "11"
        elif x in "decembre":
            return "12"
        else:
            return None
#################################################################
    def verify_date(j, m, a):
        try:
            d = date(a, m, j)
            return True
        except ValueError:
            return False
   #print(verify_date(22, 12, 2020))

##################################################################
    def transformdate(datees):
        try:
            datees=check_date((datees))
            datees=datees.split("/")
            x=len(datees)
            i=0
            while i<x:
                if datees[i]=="":
                    del datees[i]
                    x=x-1
                    i=i-1
                i=i+1
            if len(datees) == 3:
                j=datees[0]
                m=datees[1]
                a=datees[2]
                if m.isalpha():
                    m=mois(m)
                    if(m!=None):
                        m=int(m)
                        if j.isdigit() and a.isdigit():
                            j = int(j)
                            a = int(a)
                            dateval = verify_date(j,m,a)
                        else:
                            dateval = False
                    else:
                        dateval = False
                elif m.isdigit() and j.isdigit() and a.isdigit():
                    m=int(m)
                    j = int(j)
                    a = int(a)
                    dateval = verify_date(j, m, a)
                else:
                    dateval = False
            else:
                dateval = False
            if dateval == True:
                    j = str(j)
                    m = str(m)
                    a = str(a)
                    dateval = j + "/" + m + "/" + a
        except ValueError:
            dateval = False
        return  dateval

###################################################################

####################DEME DIALLO##################################
    tableaumoy = []
    def separe_note_function(notes):
        valide = True
        composition = 0
        moyenne_general = 0
        if notes.startswith('#'):
            notes = notes[1:]

        note_recuperer = notes.split('#')

        for k in note_recuperer:
            k = k.replace(',',';')
            cpt = 0
            note_recup = k.replace(']', '')
            # note_separer = note_recup.split('[')  #====>['matiere','notes']
            matiere = note_recup.split('[')[0]
            # print(matiere)
            # print(note_recup)
            for l in note_recup:      ### Pour gèrer les notes qui ont plus d'une composition
                if l == ':':
                    cpt = cpt + 1
            if cpt != 1:
                valide = False
            else:
                # valeur_note = note_separer[1]
                separer_comp_devoir = note_recup.split('[')[1].split(':')
                if separer_comp_devoir[1] == "":  ###Pour enlever les notes qui ont un vide
                    valide = False
                else:
                    # print(separer_comp_devoir)
                    devoirs = separer_comp_devoir[0]
                    composition = separer_comp_devoir[1]
                    if int(composition) < 0 or int(composition) > 20:
                        valide = False
                    else:
                        devoir = devoirs.split(';')
                        for z in range(len(devoir)-1):
                            if int(devoir[z]) < 0 or int(devoir[z]) > 20:
                                valide = False
                        if valide == True:
                            # print(matiere, devoir, composition)

                            somme = 0

                            for val in devoir:
                                somme = somme + int(val)
                            # print(somme)
                            moyenne_devoir = somme / len(devoir)
                            # print(moyenne_devoir)
                            # tableaumoy.append(moyenne_devoir)

                            # moyenne_general = calcul_moyenne(tableaumoy, composition)
                            # print(moyenne_general)
                            moyenne_matiere = (moyenne_devoir + (2 * int(composition))) / 3
                            moyenne_general = moyenne_general + moyenne_matiere

        moyenne_general = round(moyenne_general / len(note_recuperer), 2)
        info: any
        if valide == True:
            info = moyenne_general
        else:
            info = valide
        return info


#####################################################################

    #di = "30:Fev;98"
    #print(transformdate(di))
    for row in myReader:
        code=row[1]
        nom=row[2]
        prenom=row[3]
        Date=row[4]
        classe=row[5]
        matiere=row[6]
        if (code!='' and nom!='' and prenom!='' and Date!='' and classe!='' and matiere!='' ) and \
                (len(code)==7 and code.isupper() and code.isalnum() and len(nom)>=2 and nom[0].isalpha() and len(prenom)>=3 and prenom.isalpha()) \
                and (classe.endswith('A') or classe.endswith('B')) and transformdate(Date) != False:
                        moyenne = separe_note_function(matiere)

                        liste.append([code,nom,prenom,transformdate(Date),classe,matiere,moyenne])
                        p = p + 1

        else :
            listeinv.append([code,nom,prenom,date,classe,matiere])




for li in range(len(liste)):
    print(liste[li])
