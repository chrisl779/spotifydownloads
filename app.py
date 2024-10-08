from flask import Flask, request, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)

def download(url, output):
    if not os.path.exists(output):
        os.makedirs(output)
    try:
        subprocess.run(['spotdl', url, '--output', os.path.join(output, '%(title)s.%(ext)s')], check=True)
    except subprocess.CalledProcessError as e:
        return str(e)
    return f"Downloaded successfully to {output}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output = "C:/Users/Chris_2yelyef/OneDrive/Desktop/spotifytodownloads"
        message = download(url, output)
        return render_template('index.html', message=message)
    return render_template('index.html', message='')

if __name__ == '__main__':
    app.run(debug=True)
