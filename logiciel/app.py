from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configurer la connexion à la base de données
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3307",  # Utilisez le port 3307
            user="root",
            password="123456",
            database='school'
        )
        print("Connexion à MySQL réussie")
    except Error as e:
        print(f"Erreur '{e}' lors de la connexion à MySQL")
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/etudiant')
def get_students():
    connection = create_connection()
    if connection is None:
        return "Erreur de connexion à la base de données", 500  # Retourne une erreur 500 si la connexion échoue
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('etudiant.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
