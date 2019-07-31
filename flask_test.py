from flask import Flask
#improving template
from flask import render_template


app = Flask(__name__)


def factors(num):
	return [x for x in range (1, num+1) if ( num %x  == 0)]

@app.route('/factors/<int:num>')
def factors_route(num):
	return "The factors of {} are {}".format(num, factors(num))


@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/test')
def test():
	return 'test'

@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello ' + name.capitalize() + '!'


@app.route('/factors_raw/<int:n>')
def factors_display_rawHmtl(n):
	factors_list = factors(int(n))
	html = "<h1> The factors of "+ str(n) + " are</h1> \n" + "<ul>"

	for f in factors_list:
		html += "<li>"+ str(f) + "</li> \n"

	html += "</ul> </body>"
	return html

@app.route('/factors_D/<int:n>')
def factors_display(n):
	return render_template(
			"factors.html", #name of render_template
			number=n, #value for the number variable in render_template
			factors = factors(n) # value for factors in template
	)


if __name__ == '__main__':
	app.run(host='0.0.0.0')
