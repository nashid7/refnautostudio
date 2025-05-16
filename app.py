from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/pricing')
def pricing():
    """Render the pricing/packages page."""
    return render_template('pricing.html')

@app.route('/about')
def about():
    """Render the about us page."""
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    """Render the gallery page."""
    return render_template('gallery.html')

@app.route('/sitemap.xml')
def sitemap():
    """Serve the sitemap.xml file at the root URL for SEO."""
    return send_from_directory('static', 'sitemap.xml', mimetype='application/xml')

@app.route('/favicon.ico')
def favicon():
    """Serve favicon.ico from the static directory at the root URL."""
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
