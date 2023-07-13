from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect_mysql')
def connect_mysql():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='mysql_host',
            user='prabin',
            password='prabin',
            database='mydatabase'
        )
        conn.close()
        message = "Connected to the MySQL database"
    except mysql.connector.Error as error:
        message = f"Failed to connect to MySQL database: {error}"
    
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
