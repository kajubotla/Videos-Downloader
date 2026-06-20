import os
from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_data = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                # yt-dlp کی سیٹنگز
                ydl_opts = {'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_data = {
                        'title': info.get('title'),
                        'formats': info.get('formats', [])
                    }
            except Exception as e:
                video_data = {'error': str(e)}
    
    return render_template('index.html', video=video_data)

if __name__ == '__main__':
    # Railway کے لیے پورٹ اور ہوسٹ کی سیٹنگ
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
