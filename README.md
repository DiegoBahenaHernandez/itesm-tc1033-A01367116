TC1033 - T1 - A01367116.zip

En el diagrama dejé sólo la información escencial que se relaciona en el archivo "solucio_t3". Se pueden ver los conceptos que interactúan para generar el archivo "statistics".

Conteo del aereopuerto.
Es el objetivo final de toda la interacción de los distintos conceptos.

Rastreo de pasajeros.
Rastrea la posición de los pasajeros dentro del Areopuerto.
Es una herencia del conteo de aereopuerto. Tiene una relación fuerte con los pasajeros y los filtros, ya que a los pasajeros son a los que cuentan y los filtros son los lugares en donde se cuentan a los primeros. Las tripulaciones son rastreadas de la misma forma que a los pasajeros.
Tiene una relación débil con los estados de vuelo, ya que para llegar a ciertos estados de vuelo, es necesario que todos los pasajeros abordo hayan pasado por ciertos filtros.

Pasajeros
Tienen una relación débil con los filtros, ya que dependiendo del tipo de equipaje puede saltarce ciertos filtros.

Tripulación.
Tienen una relación débil con los filtros, ya que dependiendo del tipo de equipaje puede saltarce ciertos filtros.

Estados de vuelo.
Es la instancia en la que se encuentra el vuelo.
Son una herencia del conteo del aereopuerto. Tienen una relación fuerte con el estado de pista y puerta, ya que son en estas donde ciertos estados de vuelo toman lugar.

Estados de pista y puerta
Es herencia del conteo del aereopuerto. Tiene una relación fuerte con los vuelos que han llegado y salido, ya que estos salieron de o llegarán a pistas y puertas específicas.

Vuelos que han llegado y salido.
Es herencia del conteo del aereopuerto, ya que el conteo cuenta todos los aviones que se encuentran en el aereopuerto.