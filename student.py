import json
import sys

def raport(listaStudentow):
    print 'Liczba studentow: ' + str(len(listaStudentow['students']))
    listaStudentowSorted = dict(listaStudentow)
    listaStudentowSorted['students'] = sorted(listaStudentow['students'], key=lambda x: x['surname'], reverse=False)
    for i in range(0, len(listaStudentowSorted['students'])-1, 1):
        index = str(listaStudentowSorted['students'][i]['nr_indeksu'])
        imie = str(listaStudentowSorted['students'][i]['name'])
        nazwisko = str(listaStudentowSorted['students'][i]['surname'])
        minOcena = min(listaStudentowSorted['students'][i]['oceny'])
        maxOcena = max(listaStudentowSorted['students'][i]['oceny'])
        srOcena = sum(listaStudentowSorted['students'][i]['oceny'])/len(listaStudentowSorted['students'][i]['oceny'])
        print index+' Sr:'+str(srOcena)+' Max:'+str(maxOcena)+' Min:'+str(minOcena)+'\t'+nazwisko, imie





with open(sys.argv[1]) as json_data:
    students = json.load(json_data)

raport(students)

