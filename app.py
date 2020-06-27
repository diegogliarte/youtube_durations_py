from flask import Flask, render_template, request
from youtube import youtube_duration
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if (request.method == 'POST'):
        url = request.form['url']
        duration, total_videos = youtube_duration(url)
        print(duration)

        return render_template('main.html', name='youtube', duration=duration, url=url, total_videos=total_videos)

    return render_template('main.html', name='youtube')


app.run(host='localhost', port=6060, debug=True)
