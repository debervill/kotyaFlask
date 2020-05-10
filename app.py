from flask import Flask, render_template
import app_config
from serviceFunc import getDays

app = Flask(__name__)
app.config.from_object(app_config)


@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')


@app.route('/yespage.html', methods=['GET', 'POST'])
def yespressed():
	return render_template('yespage.html', days=getDays())


@app.route('/nopage.html', methods=['GET', 'POST'])
def nopressed():
	return render_template('nopage.html')

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(debug=True, host='0.0.0.0')	