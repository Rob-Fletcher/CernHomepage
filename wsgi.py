import flask

application = flask.Flask(__name__)

@application.route('/')
def homepage():
    return flask.render_template('index.html')

if __name__=='__main__':
    application.run()
