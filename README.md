# Semantic Search peste documente text

Acest proiect are ca scop implementarea cautarii semantice peste un set de documente text folosind `Oracle AI Vector Search`.

## Arhitectura solutiei

Documentele sunt prima data impartite in chunks (fragmente de text de dimensiuni relativ mici) pentru a putea fi prelucrate de modelul de embedding. Documentele sunt in format Markdown astfel ca strategia de chunking a fost adaptata astfel incat fiecare fisier este impartit pe sectiuni delimitate de un header. Acest model genereaza cate un embedding pentru fiecare chunk si le stocheaza intr un tabel cu 2 coloane de tipul VARCHAR si VECTOR.

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

![]()

## Comands

docker pull container-registry.oracle.com/database/free:latest

## PPT

[link](https://onedrive.live.com/:p:/g/personal/3fa7202e406714ae/IQBBc3iGf5wWR7VAqDki67KlAVQwWIczbJOyEKWMJR0t_08?rtime=uiY0Jrmj3kg&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy8zZmE3MjAyZTQwNjcxNGFlL0lRQkJjM2lHZjV3V1I3VkFxRGtpNjdLbEFWUXdXSWN6YkpPeUVLV01KUjB0XzA4P2U9NkhFZjdH)

## Bibliografie

- Sherry LaMonica, [Now Available! Pre-built Embedding Generation model for Oracle Database 26ai](https://blogs.oracle.com/machinelearning/use-our-prebuilt-onnx-model-now-available-for-embedding-generation-in-oracle-database-23ai)
- [Vector Search in Oracle Database 23ai: Demo](https://www.youtube.com/watch?v=eyCnDd8b7xc)
