import os
from flask import Flask, render_template

app = Flask(__name__)

# Mock url_for to return relative paths
@app.context_processor
def override_url_for():
    def mocked_url_for(endpoint, **values):
        if endpoint == 'static':
            return f"static/{values['filename']}"
        elif endpoint == 'index':
            return 'index.html'
        elif endpoint == 'about':
            return 'about.html'
        elif endpoint == 'services':
            return 'services.html'
        elif endpoint == 'gallery':
            return 'gallery.html'
        elif endpoint == 'contact':
            return 'contact.html'
        else:
            return f"{endpoint}.html"
    return dict(url_for=mocked_url_for)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    build_dir = os.path.join(os.path.dirname(__file__), 'dist')
    os.makedirs(build_dir, exist_ok=True)

    with app.test_request_context():
        pages = {
            'index.html': index(),
            'about.html': about(),
            'services.html': services(),
            'gallery.html': gallery(),
            'contact.html': contact(),
        }

        for filename, content in pages.items():
            filepath = os.path.join(build_dir, filename)
            with open(filepath, 'w') as f:
                f.write(content)

    print(f"Static site built in {build_dir}")
