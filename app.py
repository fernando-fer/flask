from flask import Flask, request, render_template, jsonify

# Creamos una instancia de Flask
app = Flask(__name__)

# Lista para almacenar las notas
notes = []

# Ruta principal para mostrar la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para agregar una nueva nota
@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    print("Nota recibida desde el formulario:", note)  # Debugging
    if note:
        notes.append(note)
        print("Nota agregada correctamente:", note)  # Debugging
        return f"Nota agregada: {note}"
    else:
        print("Error: No se recibió ninguna nota.")  # Debugging
        return "Por favor, envía una nota."

# Ruta para obtener la lista de notas
@app.route('/notes', methods=['GET'])
def list_notes():
    print("Lista de notas:", notes)  # Debugging
    return jsonify(notes)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
