from flask import Flask, render_template, url_for, request
import sqlite3
from os.path import join
from pandas import DataFrame
from mysql.connector import Error
from crypto_scraper import CryptoScraper
from util import check_directory, get_datetime

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            file_name = get_datetime()
            crypto_scraper = CryptoScraper()
            data, table_heading = crypto_scraper.get_crypto_data()

            check_directory('Crypto Data (csv)')
            DataFrame(data, columns=table_heading).to_csv(
                join('Crypto Data (csv)', file_name + '.csv'), index=False)
            print(f'--> CSV created! (Name): {file_name}')
            print(data)
            return render_template('userlog.html', data=data, table_heading=table_heading)

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
