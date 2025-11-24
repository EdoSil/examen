from flask import Flask, render_template, request

# Crear la aplicación
app = Flask(__name__)


# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")  # Carga la plantilla


# Ruta para Ejercicio 1
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
# mayor o igual a 18 y menos de 30, 15% descuento
# entre mayor de 30, 25% de descuento
# menos de 18, sin descuento

    nombre = ""
    edad = None
    cantidad_tarros = None
    total_sin_descuento = 0
    descuento = 0
    total_con_descuento = 0
    mensaje_error = None

    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            edad = float(request.form["edad"])
            cantidad_tarros = float(request.form["tarros"])


            if edad >= 18 and edad <= 30:
                total_sin_descuento = cantidad_tarros * 9000
                descuento =  (total_sin_descuento * 0.15)
                total_con_descuento = total_sin_descuento - descuento

            elif edad > 30:
                total_sin_descuento = cantidad_tarros * 9000
                descuento = (total_sin_descuento * 0.25)
                total_con_descuento = total_sin_descuento - descuento

            else :
                total_sin_descuento = cantidad_tarros * 9000
                descuento = (total_sin_descuento * 0)
                total_con_descuento = total_sin_descuento - descuento

            return render_template("ejercicio1.html",
                               nombre = nombre,
                               edad = edad,
                               total_sin_descuento = total_sin_descuento,
                               descuento = descuento,
                               total_con_descuento = total_con_descuento,
                               error = mensaje_error )


        except Exception:
            mensaje_error = "Ingrese valores numéricos válidos para edad y cantidad de tarros."
            return render_template("ejercicio1.html", error=mensaje_error)

    # GET → página recién cargada sin cálculos
    return render_template("ejercicio1.html")

# Ruta para Ejercicio 2
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    usuario = None
    contrasena = None

    if request.method == "POST":
       usuario = request.form["nombre_usuario"]
       contrasena = request.form["contrasena"]

       if usuario == "juan" and contrasena == "admin":
          mensaje = f"Bienvenido administrador {usuario}"
       elif usuario == "pepe" and contrasena == "user":
          mensaje = f"Bienvenido administrador {usuario}"
       elif usuario == "juan" and contrasena != "admin":
          mensaje = f"{usuario} contraseña incorrecta"
       elif usuario == "pepe" and contrasena != "user":
          mensaje = f"{usuario} contraseña incorrecta"
       else:
          mensaje = "Usuario y contraseña incorrectos"

       return render_template("ejercicio2.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


# Punto de entrada principal para ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)