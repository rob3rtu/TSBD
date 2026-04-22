# Semantic Search peste documente text

Acest proiect are ca scop implementarea cautarii semantice peste un set de documente text folosind `Oracle AI Vector Search`.

## Arhitectura solutiei

Documentele sunt prima data impartite in chunks (fragmente de text de dimensiuni relativ mici) pentru a putea fi prelucrate de modelul de embedding. Acest model genereaza cate un embedding pentru fiecare chunk si le stocheaza intr un tabel cu 2 coloane de tipul VARCHAR si VECTOR.

Un embedding este un vector numeric ce reprezinta un echivalent al sensului semantic pentru un text. Doua texte diferite dar cu sens asemanator vor avea vectori apropiati.

Textul pentru care se doreste a se face cautarea este la randul sau transormat intr un embedding care este mai apoi folosit pentru cautarea chunkurilor similare. Functia `vector_distance()` foloseste `COSINE SIMILARITY` pentru a calcula distanta dintre doi vectori.

## Versiuni folosite

- Python 3.14.0
- Oracle AI Database 26ai Free Release 23.26.1.0.0 + ALL_MINILM_L12_V2
- oracledb 3.4.2 (Python interface to Oracle Database)
- Docker 4.49.0

## Rularea proiectului

1. Creearea unui container docker pentru baza de date:

```
docker run -d  -p 1521:1521  -e ORACLE_PWD=YourSecurePassword123 --name oracle-db \\n  container-registry.oracle.com/database/free:latest
```

## Comands

docker pull container-registry.oracle.com/database/free:latest

docker run -d \
 -p 1521:1521 \
 -e ORACLE_PWD=YourSecurePassword123 \
 --name oracle-db \
 container-registry.oracle.com/database/free:latest

## Bibliografie

- Sherry LaMonica, [Now Available! Pre-built Embedding Generation model for Oracle Database 26ai](https://blogs.oracle.com/machinelearning/use-our-prebuilt-onnx-model-now-available-for-embedding-generation-in-oracle-database-23ai)
- [Vector Search in Oracle Database 23ai: Demo](https://www.youtube.com/watch?v=eyCnDd8b7xc)
