# Semantic Search peste documente text

[![Python](https://img.shields.io/badge/Python-3.14.0-blue?logo=python&logoColor=white)](#)
[![Oracle](https://img.shields.io/badge/Oracle-Database_23ai/26ai-red?logo=oracle&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-4.49.0-2496ED?logo=docker&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-FF4B4B?logo=streamlit&logoColor=white)](#)

Acest proiect are ca scop implementarea **căutării semantice** peste un set de documente text folosind `Oracle AI Vector Search`. 

---

## Arhitectura soluției

Procesul de căutare semantică funcționează astfel:

1. **Chunking:** Documentele (în format Markdown) sunt inițial împărțite în *chunks* (fragmente de text de dimensiuni relativ mici) pentru a putea fi prelucrate de modelul de embedding. Strategia de chunking a fost adaptată astfel încât fiecare fișier este împărțit pe secțiuni delimitate de headere.
2. **Generare Embeddings:** Modelul generează câte un embedding pentru fiecare chunk și le stochează într-un tabel cu două coloane de tipul `VARCHAR` și `VECTOR`.
   
![embeddings](https://github.com/rob3rtu/TSBD/blob/main/images/embeddings.png)

> **Un embedding** este un vector numeric ce reprezintă un echivalent al sensului semantic pentru un text. Două texte diferite, dar cu sens asemănător, vor genera vectori apropiați în spațiul multidimensional.

3. **Procesul de Căutare:** Textul pentru care se dorește a se face căutarea este, la rândul său, transformat într-un embedding. Acesta este apoi folosit pentru a căuta chunk-urile similare din baza de date. 
4. **Calculul Distanței:** Funcția `vector_distance()` folosește `COSINE SIMILARITY` pentru a calcula distanța dintre cei doi vectori și a returna cele mai relevante rezultate.

---

## Tehnologii și Versiuni

- **Limbaj:** Python 3.14.0
- **Bază de date:** Oracle AI Database 26ai Free Release 23.26.1.0.0 + `ALL_MINILM_L12_V2`
- **Driver Bază de date:** oracledb 3.4.2 (Interfața Python pentru Oracle Database)
- **Containerizare:** Docker 4.49.0
- **Frontend / UI:** Streamlit 1.45.1

---

## Rularea proiectului

### 1. Crearea unui container Docker pentru baza de date

Comanda de mai jos creează un container și îl pornește. Acesta folosește cea mai recentă imagine de Oracle (care la momentul actual este 26ai/23ai). Ulterior, containerul poate fi oprit și pornit direct din interfața Docker.
```bash
docker run -d  -p 1521:1521  -e ORACLE_PWD=YourSecurePassword123 --name oracle-db container-registry.oracle.com/database/free:latest
```

### 2. Descărcarea modelului de embedding

Modelul folosit în acest proiect poate fi descărcat din [documentația oficială Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/import-pretrained-models-onnx-format-vector-generation-database.html). 

După dezarhivare, se obține modelul cu extensia `.onnx`. Pentru a fi vizibil în baza de date, trebuie să îl importăm în container. În acest proiect, am ales să îl adăugăm la locația `/home/oracle/models`:

![ss-docker](https://github.com/rob3rtu/TSBD/blob/main/images/ss-docker.png)

### 3. Adăugarea modelului în baza de date

Odată descărcat și încărcat în Docker, modelul trebuie integrat în baza de date, prin rularea următoarelor instrucțiuni:

```sql
create or replace directory dm_dump as '/home/oracle/models';

grant read,write on directory dm_dump to sys;

begin
   dbms_vector.load_onnx_model(
      directory  => 'DM_DUMP',
      file_name  => 'all_MiniLM_L12_v2.onnx',
      model_name => 'ALL_MINILM_L12_V2'
   );
end;
/
```

Se poate verifica dacă modelul a fost încărcat cu succes și este vizibil în baza de date prin comanda următoare:

```sql
select model_name,
       algorithm,
       mining_function
  from user_mining_models
 where model_name = 'ALL_MINILM_L12_V2';
```

![check model](https://github.com/rob3rtu/TSBD/blob/main/images/model-check.png)

### 4. Pornirea aplicației

Aplicația poate fi pornită folosind următoarea comandă:
```bash
streamlit run ui.py
```

Aceasta va porni un server local, iar aplicația va fi disponibilă pe `http://localhost:8501/`.

![demo-start](https://github.com/rob3rtu/TSBD/blob/main/images/demo-start.png)

Acum se pot căuta orice informații direct în fișierele Markdown deja indexate:

![demo1](https://github.com/rob3rtu/TSBD/blob/main/images/demo-search1.png)

![demo2](https://github.com/rob3rtu/TSBD/blob/main/images/demo-search2.png)

---

## Prezentare

**[Prezentarea Proiectului](https://onedrive.live.com/:p:/g/personal/3fa7202e406714ae/IQBBc3iGf5wWR7VAqDki67KlAVQwWIczbJOyEKWMJR0t_08?rtime=uiY0Jrmj3kg&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy8zZmE3MjAyZTQwNjcxNGFlL0lRQkJjM2lHZjV3V1I3VkFxRGtpNjdLbEFWUXdXSWN6YkpPeUVLV01KUjB0XzA4P2U9NkhFZjdH)**

---

## Bibliografie

- Sherry LaMonica, *[Now Available! Pre-built Embedding Generation model for Oracle Database 26ai](https://blogs.oracle.com/machinelearning/use-our-prebuilt-onnx-model-now-available-for-embedding-generation-in-oracle-database-23ai)*
- *[Vector Search in Oracle Database 23ai: Demo](https://www.youtube.com/watch?v=eyCnDd8b7xc)* (YouTube)
