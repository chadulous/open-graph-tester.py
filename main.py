import flask
import opgparse

app = flask.Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
@app.route('/')
def home():
    return flask.render_template('form.html')
@app.route('/opg')
def opg():
    url = flask.request.args['url']
    parsed = opgparse.OpenGraph(url)
    return flask.render_template('opg.html', og=opgparse.htmlify(parsed))
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, True)