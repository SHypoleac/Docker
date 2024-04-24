# Użyj oficjalnego obrazu Ubuntu jako bazy
FROM ubuntu

# Ustaw katalog roboczy w kontenerze na /app
WORKDIR /app

# Skopiuj skrypt bash do obrazu
COPY newserver.bash /app/newserver.bash

RUN apt-get update && apt-get install -y netcat

RUN chmod +x /app/newserver.bash

# Uruchom skrypt bash bezpośrednio z montowanego woluminu
CMD ["/bin/bash", "-c", "./newserver.bash"]