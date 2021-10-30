from flask import Flask, request, url_for, redirect, abort
from flask.templating import render_template
app = Flask(__name__)
import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Univalle",
    database="prueba"
)

cursor = midb.cursor(dictionary=True)



@app.route('/')
def index():
    return 'Hola mundo'
#GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_usuario_id>', methods=['GET', 'POST'])
def lala(post_usuario_id):
    if request.method == 'GET':
        return 'el id del post es: {}'.format(post_usuario_id)
    else:
        return 'este es otro metodo'


@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print(usuarios)
    # abort(403)
    # return redirect(url_for('lala', post_usuario_id=1))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    # return render_template('lele.html')
    # return {'username': 'chanchito feliz', 'email': 'chanchito@feliz.com'}
    return render_template('lele.html', usuarios=usuarios)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje="Hola mundo")


@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'GET':
        return render_template('crear.html')
    else:
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sql = "INSERT INTO usuarios (nombre, apellido) VALUES (%s, %s)"
        valores = (nombre, apellidos)
        cursor.execute(sql,valores)
        midb.commit()
        return redirect(url_for('lele'))