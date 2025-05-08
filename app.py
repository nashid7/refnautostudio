from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)