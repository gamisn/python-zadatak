Napisati program koji određuje težinu predmeta. Informacije o predmetima su date u nepoznatnom broju linija i razdvojene su blanko znakom u okviru jednog reda. Svaki red sadrži šifru predmeta, broj studenata upisanih na tom predmetu i težinu jedne grupe studenata. Jedan predmet se može držati na više odseka i u tom slučaju postoji više šifara za taj predmeta (jedna po odseku). Svaka šifra se sastoji od sledećeg: dve cifre koje predstavljaju godinu akreditacije, slovo koje predstavlja odsek, dve cifre koje predstavljaju katedru koja drži taj predmet, cifru koja predstavlja godinu studija na kojoj se drži taj predmet i akronim predmeta. Program treba da za svaki predmet odredi broj koji predstavlja težinu datog predmeta. Težina se računa tako što se najpre nađe težinska suma proizvoda koji se dobijaju tako što se broj grupa na nekom odseku pomnoži sa težinom grupe na datom odseku, a potom se ta suma podeli sa ukupnim brojem grupa na svim odsecima. Broj grupa se određuje na osnovu broj studenata na odseku i to tako da jednu grupu čini maksimalno 60 studenata. Program treba najpre da pročita sve informacije, a potom da za svaki predmet odredi njegovu težinu. Na kraju program treba da ispiše akronime predmeta i njihove težine sortirane leksikografski po akronimu predmeta. Određivanje težine predmeta izdvojiti u zasebnu funkciju koja treba da komuniciraju sa glavnim programom isključivo putem argumenata i povratnih vrednosti. Smatrati da su svi podaci korektno zadati. Sve realne brojeve ispisivati na dve decimale.
Program treba da:
1) Pozove funkciju koja će učitati sve informacije o predmetima.
2) Pozove funkciju koja za svaki predmeta pronalazi njegovu težinu.
3) Ispiše dobijeni rezultat u navedenom poretku