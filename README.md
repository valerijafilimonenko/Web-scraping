# Web-scraping
Projekta mērķis ir izstrādāt pilnvērtīgu programmu, kas automatizēs kādu manu ikdienas uzdevumu. Savam projektam esmu izvēlējusies tīmekļa skrapingu, kas ļauj iegūt vajadzīgo informāciju no visām tīmekļa resursu lapām. Projekta uzdevums veikt platformas skrapingu, kurā ir publiski pieejami nekustamā īpašuma sludinājumi, pēc tam šos datus saglabāt CSV failā, izvēlējos šo formātu, jo tas ir vienkāršs tabulveida datu glabāšanas formāts, kas ir viegli lasāms un apstrādājams. Pēc projekta uzdevuma noskaidrošanas, ir jāsaprot, ko vēlamies no tā iegūt, manā gadījumā ir jāsaņem īsa informācija par katru dzīvokli, tā cenu, cik tajā ir istabu, kurā stāvā atrodas, tā atrašanās vietu (ielu). Tāpat, izmantojot algoritmu, tika pievienotas saites ātrai pāriešanai no CSV faila uz ieinteresēto sludinājumu. Pēc mājas lapas izvēles un konkrētu parametru noteikšanas vajadzīgā nekustamā īpašuma atrašanai, jāuzzina kuros mājas lapas elementos tiek glabāti nepieciešamie dati, bija jāizdomā skrapinga loģika, kas ļaus mums iegūt visu vajadzīgo informāciju no katra sludinājuma un saglabāt to CSV failā. 
### Tāpēc man bija jāatbild uz šādiem jautājumiem:
**1.** Kā iegūt vajadzīgo informāciju no viena sludinājuma? (piemēram, šī varētu būt cena)

**2.** Kā iegūt šo informāciju, bet jau no visiem sludinājumiem lapā?

**3.** Tā kā pēc mana pieprasījuma mājas lapā bija vairākas lapas, radās jautājums, kā iegūt šo pašu informāciju, bet jau no visām lapām?

**4.** Kā saglabāt visu CSV failā esošo informāciju, lai viss tiktu ierakstīts rindiņā, ar vajadzīgajiem virsrakstiem, lai viegli pārskatītu failu?
## Mana projekta pamatuzdevumi:
* Nekustamā īpašuma tirgus monitorings, aktuālas informācijas saņemšanai par pieejamajiem sludinājumiem, manā gadījumā, par nekustamā īpašuma izīrē Rīgas centrā, konkrētajā rajonā.
* Sekojot izmaiņām sludinājumos, programma ļauj izsekot, piemēram, cenu izmaiņām, jaunu dzīvokļu piedāvājumu parādīšanos utt.
* Nekustamā īpašuma cenu un raksturojumu analīze, ietver datu apkopošanu par cenām, ēku stāvu skaitu, kurā pilsētā/rajonā atrodas vajadzīgais nekustamais īpašums.
* Nekustamā īpašuma datu bāzes izveide, kas ietver tās veidošanu ar vajadzīgo informāciju un var tikt izmantota tālākai analīzei vai informācijas sniegšanai lietotājiem.
* Automatizēt noteiktu sludinājumu tipu meklēšanu, piemēram, programmā var mainīt sev vai citam jebkuram cilvēkam vajadzīgos datus par konkrēti interesējošiem sludinājumu parametriem.
* Apkopot datus ērtā formātā turpmākai lietošanai un ērtai lasīšanai un uztverei.
## Kādas Python bibliotēkas tiek izmantotas projekta izstrādes laikā?
Iedvesmojoties no iepriekšējā praktiskā darba par datu iegūšanu ar **Selenium** bibliotēkas palīdzību, tā arī kļuva par pamatbibliotēku manā programmā. Protams, mājas lapas parsingam varēja izmantot tādas ne mazāk pazīstamas bibliotēkas kā BeautifulSoup un requests, tās izpilda statisko skrapingu, bet man labāk patika dinamiskais skrapings, ko tieši veic Selenium bibliotēka.
Tā ir nepieciešama, lai automatizētu tīmekļa pārlūkprogrammu. Manā projektā to lieto, lai vadītu Chrome tīmekļa pārlūkprogrammu, aizpildītu veidlapas, naviģētu pa lapām un izgūtu datus no tīmekļa lapas. Selenium bibliotēka ir spēcīgs rīks tīmekļa skrāpēšanai un darbību automatizēšanai tīmekļa lapās, kas noder, ja API nav pieejams vai nepiešķir nepieciešamo funkcionalitāti.

Otrā **Time** bibliotēka, kuru izmanto, lai skripta izpildei pievienotu aizkaves. Proti, piemēram, lai pārietu uz vēlamo vietni, nepieciešams laiks, lai lapa varētu pilnībā ielādēt datus un nebūtu nekādu kļūmju vai problēmu, tā ir ļoti noderīga un turklāt aizkavēšanās laiku izvēlas pats lietotājs.

Trešā **CSV** bibliotēka, tā tiek izmantota datu ierakstīšanai CSV failā, tabulveida datu glabāšanai, tā ir praktiska, viegli lietojama. Konkrēti mans projekts tajā glabā datus par nekustamo īpašumu.
### Tāpat tika pievienoti moduļi un klases.
Klase **Select** no moduļa **selenium.webdriver.support.ui** tiek izmantota, lai mijiedarbotos ar izkritušajiem sarakstiem, piemēram, izkritušajām izvēlnēm. Manā projektā tas tiek izmantots, lai atlasītu opciju izkritušā sarakstā tīmekļa lapā, iestatot meklēšanas opcijas.

Izņēmums **NoSuchElementException** tiek izmantots, lai apstrādātu situācijas, kad vienums tīmekļa lapā nav atrasts. Tas palīdz padarīt kodu noturīgāku pret izmaiņām tīmekļa lapā un novērst iespējamās kļūmes. Tāpat palīdz uztaisīt programmu bez bezgalīga cikla, lai pēc visu datu apstrādes, programma pati aizvērtu tīmekļa lapu. 

**Service from selenium.webdriver.chrome.service** modulis pārstāv **Service** klasi, kuru var izmantot, lai pārvaldītu pārlūkprogrammas pakalpojumu, piemēram, ChromeDriver, startējot to. Izmantojiet šo klasi, lai pārvaldītu un konfigurētu pārlūkprogrammu, startējot to, izmantojot WebDriver. By from modulis selenium.webdriver.common.by pārstāv By klasi, kas nodrošina dažādas metodes, kā tīmekļa lapā identificēt elementus. Manā projektā to izmanto, lai tīmekļa vietnē atrastu vajadzīgos objektus, izmantojot identifikatorus, piemēram, ID, XPATH un citus.
##  Par programmatūras izmantošanas metodem.
Lai aprakstītu programmatūras izmantošanas metodes, ir jāsaprot, kā lietotājs to var izmantot, tūlīt tiks aprakstītas galvenās darbības, kas var būt nepieciešamas, lietojot programmatūru, un ko var veikt lietotājs.
* Sākšanas un pielāgošanas konfigurācija - lai sāktu lietot programmu, lietotājam var būt jāinstalē dažādi iestatījumi, programmas vai konfigurācijas faili. Pēc instalēšanas lietotājs palaiž programmu, iekļaujot izpildāmo skriptu vai izpildot atbilstošu komandu.
* Ievadot meklēšanas kritēriju, tiek ietverts, ka, pirmo reizi startējot, lietotājs var pielāgot iestatījumus, ja nepieciešams, piemēram, dzīvokļu cenu diapazonu, istabu skaitu, atrašanās vietu un citus parametrus, kas palīdzēs precizēt meklēšanas rezultātus.
* Automātiski izgūt datus no vietnes tikai pēc tam, kad lietotājs ir ievadījis meklēšanas kritērijus, programma izmanto Selenium, lai automatizētu darbības galvenajā lapā. Tas var ietvert lappušu navigāciju, ievadīto kritēriju ievadīšanu meklēšanas veidlapā un datu iegūšanu no iegūtajiem rezultātiem.
* Datu bāzes vai failu atjaunināšana, tas ir, ja programma tiek lietota ilgāku laiku, iespējams, būs regulāri jāatjaunina vai jāsaglabā informācija. Tas var notikt, saglabājot datus datu bāzē vai failā.
* Datu apstrāde un uzglabāšana, kur lietotājam var būt nepieciešams saglabāt vai eksportēt datus uz kādu no programmas piedāvātajiem formātiem, manā gadījumā, tas notiek CSV formātā.
* Aizveriet un saglabājiet konfigurāciju, lai lietotājs varētu saglabāt vai aizvērt programmu, saglabājot tās konfigurācijas iestatījumus, lai nākamajā reizē varētu viegli atsākt darbu no tā paša punkta.

Tas varētu būt viens piemērs, kā lietotājs var izmantot šo programmatūru, balstoties uz manu izstrādāto kodu. Protams, iespējams, būs jāpievieno vai jāpielāgo funkcionālās iespējas atkarībā no maniem konkrētajiem mērķiem un prasībām. Tāpat atkarībā no lietotāja apstākļiem un vēlmēm, piemēram, varētu pievienot paziņojumus par jauniem rezultātiem, ja lietotājam tas būtu vajadzīgs, proti, programma varētu piedāvāt iespēju paziņot lietotājam par jaunatrastajiem paziņojumiem. Izstrādātais kods ir labi automatizēts un man ir labi piemērots ikdienas uzdevuma veikšanai.

#### Projekta autore - Valērija Fiļimoņenko
