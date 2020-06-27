<<<<<<< HEAD
# Visualizzazione Dati COVID-19 Regioni

Questo progetto è un fork del repository ufficiale del [Dipartimento della Protezione Civile](https://github.com/pcm-dpc/COVID-19/).
Il principale obiettivo è offrire una visualizzazione analitica dei dati ufficiali, su base regionale.

<<<<<<< HEAD
## Estensioni

<<<<<<< HEAD
<<<<<<< HEAD
Le personalizzazioni apportate sono di due tipologie:

* Codice python per elaborazione dei dati, nella folder [custom](https://github.com/nicogiangregorio/COVID-19/tree/master/custom)
* Codice HTML/JS per visualizzazione degli output, nella folder [docs](https://github.com/nicogiangregorio/COVID-19/tree/master/docs)
=======
## README e Wiki in aggiornamento (nuova versione - 01/04/2020 @ 08:00)
## README and Wiki under update (new version - 01/04/2020 @ 08:00)

## Stiamo lavorando per fornire nuovi dataset e dashboard e perfezionamento di quelli esistenti.
## We are working to provide new datasets and dashboard and refinement of existing ones.

## Aggiornamenti dataset 
## Dataset update
=======
## Aggiornamento effettuato!
>>>>>>> upstream/master

## Aggiornamenti schema dataset 30/03/2020 @ 12:00 (Ora italiana)
## Dataset schema update 30/03/2020 @ 12:00 (Italian hour)

### Dataset:
- dati_regioni (csv / json)
- dati_andamento_nazionale (csv / json)
- dati_province (csv / json) - (solo modifica nome/only change name "Emilia-Romagna" in "Emilia-Romagna")

### IT
- Modifica: "totale_attualmente_positivi" rinominato in "totale_positivi" (ricoverati_con_sintomi + terapia_intensiva + isolamento domiciliare) in "dati_regioni" e "dati_andamento_nazionale"
- Modifica: "nuovi_attualmente_positivi" rinominato in "variazione_totale_positivi" (totale_attualmente positivi giorno corrente - totale_attualmente positivi giorno precedente) in "dati_regioni" e "dati_andamento_nazionale"
- Aggiunta: "nuovi_positivi" (totale_casi giorno corrente - totale_casi giorno precedente) in "dati_regioni" e "dati_andamento_nazionale"
- Modifica: Regione "Emilia Romagna" rinominato in "Emilia-Romagna" in "dati-regioni" e "dati-province" ("denominazione_regione")

### EN
- Change: "totale_attualmente_positivi" renamed to "totale_positivi" (ricoverati_con_sintomi + terapia_intensiva + isolamento domiciliare) in "dati_regioni" and "dati_andamento_nazionale"
- Change: "nuovi_attualmente_positivi" renamed to "variazione_totale_positivi" (totale_attualmente positivi giorno corrente - totale_attualmente positivi giorno precedente) in "dati_regioni" and "dati_andamento_nazionale"
- Add: "nuovi_positivi" (totale_casi giorno corrente - totale_casi giorno precedente) in "dati_regioni" and "dati_andamento_nazionale"
- Change: Regione "Emilia Romagna" renamed to "Emilia-Romagna" in "dati-regioni" and "dati-province" ("denominazione_regione")
=======
=======
<img src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" alt="COVID-19" data-canonical-src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" width="400" />

[Italiano](README.md) - [English](README_EN.md)<br><br>

# Dati COVID-19 Italia

<<<<<<< HEAD
>>>>>>> upstream/master
=======
>>>>>>> upstream/master
[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
[![GitHub commit](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)](https://github.com/pcm-dpc/COVID-19/commits/master)

**Nuove modifiche ai dataset da lunedì 29/06 - [Avviso](https://github.com/pcm-dpc/COVID-19/issues/747)**<br>
**New changes to datasets from Monday 29/06 - [Notice](https://github.com/pcm-dpc/COVID-19/issues/747)**<br>

[Sito del Dipartimento della Protezione Civile - Emergenza Coronavirus: la risposta nazionale](http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus)
<<<<<<< HEAD
>>>>>>> upstream/master
=======
>>>>>>> upstream/master

Il 31 gennaio 2020, il Consiglio dei Ministri dichiara lo stato di emergenza, per la durata di sei mesi, in conseguenza del rischio sanitario connesso all'infezione da Coronavirus.
Al Capo del Dipartimento della Protezione Civile, Angelo Borrelli, è affidato il coordinamento degli interventi necessari a fronteggiare l'emergenza sul territorio nazionale.  
Le principali azioni coordinate dal Capo del Dipartimento sono volte al soccorso e all'assistenza della popolazione eventualmente interessata dal contagio, al potenziamento dei controlli nelle aree aeroportuali e portuali, in continuità con le misure urgenti già adottate dal Ministero della salute, al rientro in Italia dei cittadini che si trovano nei Paesi a rischio e al rimpatrio dei cittadini stranieri nei Paesi di origine esposti al rischio.

Per informare i cittadini e mettere a disposizione i dati raccolti, utili ai soli fini comunicativi e di informazione, il Dipartimento della Protezione Civile ha elaborato un cruscotto geografico interattivo raggiungibile agli indirizzi  [http://arcg.is/C1unv](http://arcg.is/C1unv) (versione desktop) e [http://arcg.is/081a51](http://arcg.is/081a51) (versione mobile) e mette a disposizione, con licenza CC-BY-4.0, le seguenti informazioni aggiornate quotidianamente alle 18:30 (successivamente la conferenza stampa del Capo Dipartimento):

- Dati Andamento nazionale
- Dati json
- Dati regioni
- Dati province
- Schede riepilogative
- Aree
- Note
- Dati contratti DPC forniture
- Metriche

## Avvisi

[Avvisi sui dati andamento COVID-19 Italia](avvisi.md)<br>

## Struttura del repository
```
COVID-19/
│
├── aree/
│   ├── geojson
│   │   ├── dpc-covid-19-ita-aree-comuni.geojson
│   │   ├── dpc-covid19-ita-aree.geojson
│   ├── shp
│   │   ├── dpc-covid19-ita-aree-comuni.dbf
│   │   ├── dpc-covid19-ita-aree-comuni.prj
│   │   ├── dpc-covid19-ita-aree-comuni.shp
│   │   ├── dpc-covid19-ita-aree-comuni.shx
│   │   ├── dpc-covid19-ita-aree.dbf
│   │   ├── dpc-covid19-ita-aree.prj
│   │   ├── dpc-covid19-ita-aree.shp
│   │   ├── dpc-covid19-ita-aree.shx
├── dati-andamento-nazionale/
│   ├── dpc-covid19-ita-andamento-nazionale-*.csv
│   ├── dpc-covid19-ita-andamento-nazionale-latest.csv
│   ├── dpc-covid19-ita-andamento-nazionale.csv
├── dati-contratti-dpc-forniture/
│   ├── dpc-covid19-dati-contratti-dpc-forniture.csv
│   ├── dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv
│   ├── dati-json
│   │   ├── dpc-covid19-dati-contratti-dpc-forniture.csv
│   │   ├── dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv
│   ├── file-atti-negoziali
│   │   ├── dpc-contratto-covid19-*.pdf
├── dati-json/
│   ├── dpc-covid19-ita-andamento-nazionale-latest.json
│   ├── dpc-covid19-ita-andamento-nazionale.json
│   ├── dpc-covid19-ita-note-en.json
│   ├── dpc-covid19-ita-note-it.json
│   ├── dpc-covid19-ita-province-latest.json
│   ├── dpc-covid19-ita-province.json
│   ├── dpc-covid19-ita-regioni-latest.json
│   ├── dpc-covid19-ita-regioni.json
├── dati-province/
│   ├── dpc-covid19-ita-province-*.csv
│   ├── dpc-covid19-ita-province-latest.csv
│   ├── dpc-covid19-ita-province.csv
├── dati-regioni/
│   ├── dpc-covid19-ita-regioni-*.csv
│   ├── dpc-covid19-ita-regioni-latest.csv
│   ├── dpc-covid19-ita-regioni.csv
├── metriche
│   ├── dpc-covid19-ita-metriche-dashboard-desktop.csv
│   ├── dpc-covid19-ita-metriche-dashboard-desktop.json
│   ├── dpc-covid19-ita-metriche-dashboard-mobile.csv
│   ├── dpc-covid19-ita-metriche-dashboard-mobile.json
├── note/
│   ├── dpc-covid19-ita-note-en.csv
│   ├── dpc-covid19-ita-note-it.csv
├── schede-riepilogative/
│   ├── province
│   │   ├── dpc-covid19-ita-scheda-province-*.pdf
│   ├── regioni
│   │   ├── dpc-covid19-ita-scheda-regioni-*.pdf
```

## Aggiornamento dei dati
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> upstream/master

- Dati andamento COVID-19 Italia: ogni giorno alle 18:00<br>
- Dati contratti DPC COVID-19 di fornitura: continua (ogni volta che vengono effettuate operazioni sui contratti)

## Formato dei dati

<<<<<<< HEAD
<<<<<<< HEAD
### Dati per Regione

**Directory:**  dati-regioni<br>
**Struttura file giornaliero:** dpc-covid19-ita-regioni-yyyymmdd.csv (dpc-covid19-ita-regioni-20200224.csv)<br>
**File complessivo:** dpc-covid19-ita-regioni.csv<br>
**File ultimi dati (latest):** dpc-covid19-ita-regioni-latest.csv

| Nome campo                  | Descrizione                       | Description                            | Formato                       | Esempio             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell'informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**              | Codice della Regione (ISTAT 2019) | Code of the Region (ISTAT 2019)        | Numero                        | 13                  |
| **denominazione_regione**       | Denominazione della Regione       | Name of the Region                     | Testo                         | Abruzzo             |
| **lat**                         | Latitudine                        | Latitude                               | WGS84                         | 42.6589177          |
| **long**                        | Longitudine                       | Longitude                              | WGS84                         | 13.70439971         |
| **ricoverati_con_sintomi**      | Ricoverati con sintomi            | Hospitalised patients with symptoms    | Numero                        | 3                   |
| **terapia_intensiva**           | Ricoverati in terapia intensiva   | Intensive Care                         | Numero                        | 3                   |
| **totale_ospedalizzati**        | Totale ospedalizzati              | Total hospitalised patients            | Numero                        | 3                   |
| **isolamento_domiciliare**      | Persone in isolamento domiciliare | Home confinement                       | Numero                        | 3                   |
| **totale_positivi** | Totale attualmente positivi (ospedalizzati + isolamento domiciliare)      | Total amount of current positive cases (Hospitalised patients + Home confinement)  | Numero                        | 3                   |
| **variazione_totale_positivi**  | Variazione del totale positivi (totale_positivi giorno corrente - totale_positivi giorno precedente)       | News amount of current positive cases (totale_positivi current day - totale_positivi previous day)  | Numero                        | 3                   |
| **nuovi_positivi**  | Nuovi attualmente positivi (totale_casi giorno corrente - totale_casi giorno precedente)       | News amount of current positive cases (totale_casi current day - totale_casi previous day)  | Numero                        | 3                   |
| **dimessi_guariti**             | Persone dimesse guarite           | Recovered                              | Numero                        | 3                   |
| **deceduti**                    | Persone decedute                  | Death                                  | Numero                        | 3                   |
| **totale_casi**                 | Totale casi positivi              | Total amount of positive cases         | Numero                        | 3                   |
| **tamponi**                     | Totale tamponi                    | Tests performed                        | Numero                        | 3                   |
| **casi_testati**                     | Totale dei soggetti sottoposti al test                    | Total number of people tested                        | Numero                        | 3                   |
| **note_it**                     | Note in lingua italiana (separate da ;)                   | Notes in italian language (separated by ;)                       | Testo                        | pd-IT-000                   |
| **note_en**                     | Note in lingua inglese (separate da ;)                    | Notes in english language (separated by ;)                       | Testo                        | pd-EN-000                   |


*Le Province autonome di Trento e Bolzano sono indicate in "denominazione regione" e con il codice 04 del Trentino Alto Adige.*<br>
*Viene messo a disposizione un file JSON complessivo di tutte le date nella cartella "dati-json": dpc-covid19-ita-regioni.json* e rispettivo file ultimi dati (latest) dpc-covid19-ita-regioni-latest.json

### Dati per Provincia

**Directory:**  dati-province<br>
**Struttura file giornaliero:** dpc-covid19-ita-province-yyyymmdd.csv (dpc-covid19-ita-province-20200224.csv)<br>
**File complessivo:** dpc-covid19-ita-province.csv<br>
**File ultimi dati (latest):** dpc-covid19-ita-province-latest.csv

| Nome campo              | Descrizione                         | Description                     | Formato            | Esempio              |
|-------------------------|-------------------------------------|---------------------------------|--------------------|----------------------|
| **data**                    | Data dell'informazione              | Date of notification            | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana           | 2020-03-05 12:15:45 |                   |
| **stato**                   | Stato di riferimento                | Country of reference            | ISO 3166-1 alpha-3 | ITA                  |
| **codice_regione**          | Codice della Regione (ISTAT 2019)   | Code of the Region (ISTAT 2019) | Numero             | 13                   |
| **denominazione_regione**   | Denominazione della Regione         | Name of the Region              | Testo              | Abruzzo              |
| **codice_provincia**        | Codice della Provincia (ISTAT 2019) | Code of the Province            | Numero             | 067                  |
| **denominazione_provincia** | Denominazione della provincia       | Name of the Province            | Testo              | Teramo               |
| **sigla_provincia**         | Sigla della Provincia               | Province abbreviation           | Testo              | TE                   |
| **lat**                     | Latitudine                          | Latitude                        | WGS84              | 42.6589177           |
| **long**                    | Longitudine                         | Longitude                       | WGS84              | 13.70439971          |
| **totale_casi**             | Totale casi positivi                | Total amount of positive cases  | Numero             | 3                    |
| **note_it**                     | Note in lingua italiana (separate da ;)                   | Notes in italian language (separated by ;)                       | Testo                        | pd-IT-000                   |
| **note_en**                     | Note in lingua inglese (separate da ;)                    | Notes in english language (separated by ;)                       | Testo                        | pd-EN-000                   |

*Le Province autonome di Trento e Bolzano sono indicate in "denominazione regione" e con il codice 04 del Trentino Alto Adige.*<br>
*Ogni Regione ha una Provincia denominata "In fase di definizione/aggiornamento" con il codice provincia da 979 a 999, utile ad indicare i dati ancora non assegnati alle Province.*<br>
*Viene messo a disposizione un file JSON complessivo di tutte le date nella cartella "dati-json": dpc-covid19-ita-province.json* e rispettivo file ultimi dati (latest) dpc-covid19-ita-province-latest.json

### Andamento nazionale

**Directory:**  dati-andamento-nazionale<br>
**Struttura file giornaliero:** dpc-covid19-ita-andamento-nazionale-yyyymmdd.csv (dpc-covid19-ita-andamento-nazionale-20200224.csv)<br>
**File complessivo:** dpc-covid19-ita-andamento-nazionale.csv<br>
**File ultimi dati (latest):** dpc-covid19-ita-regioni-latest.csv


| Nome campo                  | Descrizione                       | Description                            | Formato                       | Esempio             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell'informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **ricoverati_con_sintomi**      | Ricoverati con sintomi            | Hospitalised patients with symptoms    | Numero                        | 3                   |
| **terapia_intensiva**           | Ricoverati in terapia intensiva   | Intensive Care                         | Numero                        | 3                   |
| **totale_ospedalizzati**        | Totale ospedalizzati              | Total hospitalised patients            | Numero                        | 3                   |
| **isolamento_domiciliare**      | Persone in isolamento domiciliare | Home confinement                       | Numero                        | 3                   |
| **totale_positivi** | Totale attualmente positivi (ospedalizzati + isolamento domiciliare)      | Total amount of current positive cases (Hospitalised patients + Home confinement)  | Numero                        | 3                   |
| **variazione_totale_positivi**  | Variazione del totale positivi (totale_positivi giorno corrente - totale_positivi giorno precedente)       | News amount of current positive cases (totale_positivi current day - totale_positivi previous day)  | Numero                        | 3                   |
| **nuovi_positivi**  | Nuovi attualmente positivi (totale_casi giorno corrente - totale_casi giorno precedente)       | News amount of current positive cases (totale_casi current day - totale_casi previous day)  | Numero                        | 3                   |
| **dimessi_guariti**             | Persone dimesse guarite           | Recovered                              | Numero                        | 3                   |
| **deceduti**                    | Persone decedute                  | Death                                  | Numero                        | 3                   |
| **totale_casi**                 | Totale casi positivi              | Total amount of positive cases         | Numero                        | 3                   |
| **tamponi**                     | Totale tamponi                    | Tests performed                        | Numero                        | 3                   |
| **casi_testati**                     | Totale dei soggetti sottoposti al test                    | Total number of people tested                        | Numero                        | 3                   |
| **note_it**                     | Note in lingua italiana (separate da ;)                   | Notes in italian language (separated by ;)                       | Testo                        | pd-IT-000                   |
| **note_en**                     | Note in lingua inglese (separate da ;)                    | Notes in english language (separated by ;)                       | Testo                        | pd-EN-000                   |


*Viene messo a disposizione un file JSON complessivo di tutte le date nella cartella "dati-json": dpc-covid19-ita-andamento-nazionale.json* e rispettivo file ultimi dati (latest) dpc-covid19-ita-andamento-nazionale-latest.json

### Note

**Directory:**  note<br>
**Struttura file:** dpc-covid19-ita-note-*<br>

| Nome campo                  | Descrizione                       | Description                            | Formato                       | Esempio             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **codice**                       | Codice nota (nd - nodata / pd - partialdata / dc datacorrection)             | Note code (nd - nodata / pd - partialdata / datacorrection)                   | Testo      | nd-EN-0006                 |
| **data**                        | Data dell'informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **dataset**                       | Dataset di riferimento              | Reference dataset                   | Testo      | andamento-nazionale                 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**          | Codice della Regione (ISTAT 2019)   | Code of the Region (ISTAT 2019) | Numero             | 13                   |
| **denominazione_regione**   | Denominazione della Regione         | Name of the Region              | Testo              | Abruzzo              |
| **codice_provincia**        | Codice della Provincia (ISTAT 2019) | Code of the Province            | Numero             | 067                  |
| **denominazione_provincia** | Denominazione della provincia       | Name of the Province            | Testo              | Teramo               |
| **tipologia_avviso** | Tipologia avviso (dati parziali / nessun dato / correzione dato) | Notice type (partial data / no data / data correction)            | Testo              | dati parziali               |
| **avviso** | Testo di avviso       | Notice text            | Testo              | dati parziali               |
| **note** | Altre informazioni       | Other informations            | Testo              | dato tamponi non aggiornato               |
<br><br><br>
<<<<<<< HEAD
**Editore/Autore del dataset:** Dipartimento della Protezione Civile<br>
**Temi del dataset:** [Salute umana e sicurezza - Human health and safety](http://inspire.ec.europa.eu/theme/hh) (Inspire)<br>
**Categoria ISO 19115:** Salute<br>
*Dati forniti dal Ministero della Salute*<br>
*Elaborazione e gestione dati a cura del Dipartimento della Protezione Civile*
>>>>>>> upstream/master
=======

**Licenza:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.it) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)<br>
Scheda metadati RNDT: [dati](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM%3ACOVID-19%3A05032020%3A093000) - [aree](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM%3A000086%3A20200306%3A110700)<br>
Temi del dataset: [Salute umana e sicurezza](http://inspire.ec.europa.eu/theme/hh) - [Human health and safety (Inspire)](http://inspire.ec.europa.eu/theme/hh)<br>
Categoria ISO 19115: Salute<br>
Dati forniti dal Ministero della Salute<br>
Elaborazione e gestione dati a cura del Dipartimento della Protezione Civile<br><br>

**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en) - [View license](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)<br>
RNDT metadata: [data](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM%3ACOVID-19%3A05032020%3A093000) - [areas](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM%3A000086%3A20200306%3A110700)<br>
Dataset themes: [Human health and safety](http://inspire.ec.europa.eu/theme/hh) - [Human health and safety (Inspire)](http://inspire.ec.europa.eu/theme/hh)<br>
ISO Category 19115: Human healt<br>
Data provided by the Ministry of Health <br>
Processing and data management by the Department of Civil Protection
>>>>>>> upstream/master
=======
- [Dati andamento COVID-19 Italia](dati-andamento-covid19-italia.md)<br>
- [Dati contratti DPC COVID-19 di fornitura](dati-contratti-dpc-covid19-fornitura.md)
- [Dati aree misure restrittive COVID19](dati_aree-nazionali-subregionali-misure-restrittive-covid19.md)

## Licenza

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.it) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
>>>>>>> upstream/master
=======

- Dati andamento COVID-19 Italia: ogni giorno alle 18:00<br>
- Dati contratti DPC COVID-19 di fornitura: continua (ogni volta che vengono effettuate operazioni sui contratti)

## Formato dei dati

=======
>>>>>>> upstream/master
- [Dati andamento COVID-19 Italia](dati-andamento-covid19-italia.md)<br>
- [Dati contratti DPC COVID-19 di fornitura](dati-contratti-dpc-covid19-fornitura.md)
- [Dati aree misure restrittive COVID19](dati-aree-covid19.md)
- [Metriche](metriche.md)

## Licenza

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.it) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
<<<<<<< HEAD
>>>>>>> upstream/master
=======
>>>>>>> upstream/master
