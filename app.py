from flask import Flask, request, render_template, redirect
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='app/templates')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'speedtestuser'
app.config['MYSQL_PASSWORD'] = 'wifi123!'
app.config['MYSQL_DB'] = 'speedtest'
mysql =  MySQL(app)

@app.route('/')
def index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from speedtest where TimeStamp >= CURDATE();")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', speedtests = data)

if __name__ == '__main__':
    app.run(debug=True,host= '192.168.0.120')
