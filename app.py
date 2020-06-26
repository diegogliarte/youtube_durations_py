from flask import Flask, render_template, request
from youtube import youtube_duration

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if (request.method == 'POST'):
        url = request.form['url']
        duration = youtube_duration(url)
        print(duration)

        return render_template('main.html', name='yikes', duration=duration, url=url)

    return render_template('main.html', name='yikes')


