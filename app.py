from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
# Aqui vamos aconfigurar la conexion.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistemaejemplo'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/success' , methods=['GET', 'POST'])
def success():
    return render_template('succes.html')

@app.route('/consulta' , methods=['GET', 'POST'])
def consulta(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        contrasena = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)', (nombre, email, contrasena))
        mysql.connection.commit()
        return render_template('succes.html')



if __name__ == '__main__':
    app.run(port = 5000, debug = True) 