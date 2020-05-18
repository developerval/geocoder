from flask import Flask, render_template, request, send_file
from geocoder import output_gen
from geopy.exc import GeocoderTimedOut
import pandas


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        global file
        file = request.files['file']
        try:
            table, output = output_gen(file)
            if table:
                return render_template('index.html', btn='download.html', table=table)
            else:
                return render_template('index.html', table='Please upload a file with an "Address" or "address" column')
        except pandas.errors.EmptyDataError:
            return render_template('index.html', table='Looks like you forgot to upload a file!')
        except GeocoderTimedOut:
            return render_template('index.html', table='Looks like the geo service timed out, please wait before trying again!')


@app.route('/download')
def download():
    return send_file('output.csv', attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
