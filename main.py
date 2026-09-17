from flask import Flask, render_template, request, redirect, url_for
from datetime import date, datetime

app = Flask(__name__)
solicitudes = []

def validar_fecha(fecha_str: str) -> bool:
    """Convertimos la cadena a date y verificamos que no sea anterior a hoy."""
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        return fecha >= date.today()
    except ValueError:
        return False

def validar_telefono(telefono: str) -> bool:
    """Verificamos que sean exactamente 9 dígitos enteros."""
    return telefono.isdigit() and len(telefono) == 9

def formatear_datos(tipo: str, motivo: str, correo: str, telefono: str, fecha: str) -> dict:
    """Limpiamos las cadenas y devolvemos cada campo por separado."""
    return {
        'tipo': tipo.strip().title(),
        'motivo': motivo.strip(),
        'correo': correo.strip(),
        'telefono': telefono.strip(),
        'fecha_entrega': fecha.strip()
    }

def guardar_solicitud(solicitud: dict):
    """Agregamos la solicitud a la lista de solicitudes."""
    solicitudes.append(solicitud)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        tipo     = request.form['tipo']
        motivo   = request.form['motivo']
        correo   = request.form['correo']
        telefono = request.form['telefono']
        fecha    = request.form['fecha_entrega']

        if not validar_telefono(telefono):
            error = "Teléfono inválido. Por favor, ingresa exactamente 9 dígitos numéricos."
        elif not validar_fecha(fecha):
            error = "La fecha debe ser hoy o posterior."
        else:
            datos = formatear_datos(tipo, motivo, correo, telefono, fecha)
            guardar_solicitud(datos)
            return redirect(url_for('reporte'))

    return render_template('formulario.html', error=error)

@app.route('/reporte')
def reporte():
    return render_template('reporte.html', solicitudes=solicitudes)

if __name__ == '__main__':
    app.run(debug=True, port=5019)
