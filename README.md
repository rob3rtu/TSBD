# TSBD

Proiect - Topici Speciale in Baze de Date

## Comands

docker pull container-registry.oracle.com/database/free:latest

docker run -d \
 -p 1521:1521 \
 -e ORACLE_PWD=YourSecurePassword123 \
 --name oracle-db \
 container-registry.oracle.com/database/free:latest
