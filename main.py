
import re


# 1. Napisati program koji određuje težinu predmeta. Informacije o predmetima su date u nepoznatnom broju linija i razdvojene su blanko znakom u okviru jednog reda. Svaki red sadrži šifru predmeta, broj studenata upisanih na tom predmetu i težinu jedne grupe studenata. Jedan predmet se može držati na više odseka i u tom slučaju postoji više šifara za taj predmeta (jedna po odseku). Svaka šifra se sastoji od sledećeg: dve cifre koje predstavljaju godinu akreditacije, slovo koje predstavlja odsek, dve cifre koje predstavljaju katedru koja drži taj predmet, cifru koja predstavlja godinu studija na kojoj se drži taj predmet i akronim predmeta. Program treba da za svaki predmet odredi broj koji predstavlja težinu datog predmeta. Težina se računa tako što se najpre nađe težinska suma proizvoda koji se dobijaju tako što se broj grupa na nekom odseku pomnoži sa težinom grupe na datom odseku, a potom se ta suma podeli sa ukupnim brojem grupa na svim odsecima. Broj grupa se određuje na osnovu broj studenata na odseku i to tako da jednu grupu čini maksimalno 60 studenata. Program treba najpre da pročita sve informacije, a potom da za svaki predmet odredi njegovu težinu. Na kraju program treba da ispiše akronime predmeta i njihove težine sortirane leksikografski po akronimu predmeta. Određivanje težine predmeta izdvojiti u zasebnu funkciju koja treba da komuniciraju sa glavnim programom isključivo putem argumenata i povratnih vrednosti. Smatrati da su svi podaci korektno zadati. Sve realne brojeve ispisivati na dve decimale.
# Program treba da:
# 1) Pozove funkciju koja će učitati sve informacije o predmetima. 
# 2) Pozove funkciju koja za svaki predmeta pronalazi njegovu težinu.
# 3) Ispiše dobijeni rezultat u navedenom poretku

def read(filename):
    lines = []
    with open(filename, 'r') as file: 
        for line in file:
            lines.append(line.strip())

    return lines    

#Svaka šifra se sastoji od sledećeg: 
# dve cifre koje predstavljaju godinu akreditacije, 
# slovo koje predstavlja odsek, 
# dve cifre koje predstavljaju katedru koja drži taj predmet, 
# cifru koja predstavlja godinu studija na kojoj se drži taj predmet i akronim predmeta.
def determineSubjectRegex(subjectCode): 
    pattern = r'\d{2}[A-Za-z]\d{2}\d(\w*)'
    matches = re.findall(pattern, subjectCode)
    return matches[0]

def determineSubjectNotRegex(subjectCode):
    return subjectCode[6:]

def determineGroupNumber(studentsCount):
    divOperation = studentsCount // 60
    if ( studentsCount % 60 == 0):
        return divOperation
    else:
        return divOperation + 1


def determineGroupsWeight(subject):
    numberOfGroups = determineGroupNumber(float(subject[1]))
    return numberOfGroups * float(subject[2])



if __name__ == '__main__':
    lines = read('input.txt')
    # print(lines)
    lines = map(lambda x : x.split(" ") , lines)
    listOfSubjectsList = list(lines)
    #print(listOfSubjectsList)


    subjects = {} #  subjects[subjectAcro] = [numberOfGroups, weightNumbe]
    for subject in listOfSubjectsList:
        
        subjectAcro = determineSubjectRegex(subject[0])
        numberOfGroups = determineGroupNumber(float(subject[1]))
        groupsWeight = determineGroupsWeight(subject)
        
        if (subjectAcro in subjects):
            subjects[subjectAcro] = [subjects[subjectAcro][0] + numberOfGroups  , subjects[subjectAcro][1] + groupsWeight]
        else :
            subjects[subjectAcro] = [numberOfGroups  , groupsWeight]

    print(subjects.values())

    result = subjects = {key: value for key, value in zip(subjects.keys(), map(lambda x: round(x[1]/x[0],2), subjects.values()))} 
    print(dict(sorted(subjects.items())))

