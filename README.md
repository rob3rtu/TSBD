# Semantic Search peste documente text

Acest proiect are ca scop implementarea cautarii semantice peste un set de documente text folosind `Oracle AI Vector Search`.

## Arhitectura solutiei

Documentele sunt prima data impartite in chunks (fragmente de text de dimensiuni relativ mici) pentru a putea fi prelucrate de modelul de embedding. Documentele sunt in format Markdown astfel ca strategia de chunking a fost adaptata si fiecare fisier este impartit pe sectiuni delimitate de un header. Acest model genereaza cate un embedding pentru fiecare chunk si le stocheaza intr un tabel cu 2 coloane de tipul VARCHAR si VECTOR.

![embeddings](https://github.com/rob3rtu/TSBD/blob/main/images/embeddings.png)

Un embedding este un vector numeric ce reprezinta un echivalent al sensului semantic pentru un text. Doua texte diferite dar cu sens asemanator vor avea vectori apropiati.

Textul pentru care se doreste a se face cautarea este la randul sau transormat intr un embedding care este mai apoi folosit pentru cautarea chunkurilor similare. Functia `vector_distance()` foloseste `COSINE SIMILARITY` pentru a calcula distanta dintre doi vectori.

## Versiuni folosite

- Python 3.14.0
- Oracle AI Database 26ai Free Release 23.26.1.0.0 + ALL_MINILM_L12_V2
- oracledb 3.4.2 (Python interface to Oracle Database)
- Docker 4.49.0
- Streamlit 1.45.1

## Rularea proiectului

### 1. Creearea unui container docker pentru baza de date:

```
docker run -d  -p 1521:1521  -e ORACLE_PWD=YourSecurePassword123 --name oracle-db container-registry.oracle.com/database/free:latest
```

Aceasta comanda creeaza un container si il porneste. Ulterior acesta poate fii oprit si pornit din nou din interfata Docker. Comanda foloseste cea mai recenta imagine de Oracle, care la momentul actual este 26ai.

### 2. Descarcarea modelului de embedding

Modelul folosit in acest proiect poate fii descarcat de [aici](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/import-pretrained-models-onnx-format-vector-generation-database.html). Dupa ce dezarhivam arhiva vom vedea modelul intr-un fisier cu extensia `.onnx`. Pentru a putea fii vizibil in baza de date trebuie sa il importam in container. Noi am ales sa il adaugam la locatia `/home/oracle/models`:

![ss-docker](https://github.com/rob3rtu/TSBD/blob/main/images/ss-docker.png)

### 3. Adaugarea modelului in baza de date

Odata descarcat si incarcat in Docker, modelul trebuie adaugat si in baza de date. Pentru asta rulam urmatoarele comenzi:

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

Acum putem verifica daca am incarcam cu succes modelul si acesta este vizibil in baza de date:

```sql
select model_name,
       algorithm,
       mining_function
  from user_mining_models
 where model_name = 'ALL_MINILM_L12_V2';
```

![check model](https://github.com/rob3rtu/TSBD/blob/main/images/model-check.png)

### 4. Pornim aplicatia

Acum putem porni aplicatia folosind urmatoarea comanda:

```
streamlit run ui.py
```

Aceasta va porni un server local disponibil pe `http://localhost:8501/`:

![demo-start](https://github.com/rob3rtu/TSBD/blob/main/images/demo-start.png)

Acum putem cauta orice in fisierele Markdown deja indexate:

![demo1](https://github.com/rob3rtu/TSBD/blob/main/images/demo-search1.png)

![demo2](https://github.com/rob3rtu/TSBD/blob/main/images/demo-search2.png)

## Prezentare

[link](https://onedrive.live.com/:p:/g/personal/3fa7202e406714ae/IQBBc3iGf5wWR7VAqDki67KlAVQwWIczbJOyEKWMJR0t_08?rtime=uiY0Jrmj3kg&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy8zZmE3MjAyZTQwNjcxNGFlL0lRQkJjM2lHZjV3V1I3VkFxRGtpNjdLbEFWUXdXSWN6YkpPeUVLV01KUjB0XzA4P2U9NkhFZjdH)

## Bibliografie

- Sherry LaMonica, [Now Available! Pre-built Embedding Generation model for Oracle Database 26ai](https://blogs.oracle.com/machinelearning/use-our-prebuilt-onnx-model-now-available-for-embedding-generation-in-oracle-database-23ai)
- [Vector Search in Oracle Database 23ai: Demo](https://www.youtube.com/watch?v=eyCnDd8b7xc)
