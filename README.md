Proyecto Evaluación 3 – Aplicación Web con Flask

Este proyecto corresponde a la Evaluación 3 del taller de Programación Web. Consiste en una aplicación desarrollada con Python y Flask, utilizando plantillas HTML + Jinja2, validación de formularios y lógica básica en el servidor.



Ejercicio 1 – Venta de tarros de pintura

Permite ingresar:

Nombre del cliente
Edad
Cantidad de tarros

El sistema calcula: Total sin descuento

Descuento aplicable, según la edad:

18 a 30 años → 15%
Más de 30 años → 25%
Menores de 18 → 0%

Total final a pagar

Incluye validación para evitar errores por datos inválidos.



Ejercicio 2 – Inicio de Sesión

El usuario ingresa nombre y contraseña, y el sistema valida contra dos usuarios registrados:

juan / admin → Bienvenido administrador
pepe / user → Bienvenido usuario

Si los datos no coinciden, se muestra un mensaje de error.

Objetivo del proyecto

Practicar el uso de:
Rutas Flask con métodos GET/POST
Manejo de formularios HTML
Validación de datos ingresados

Interacción básica usuario–servidor
