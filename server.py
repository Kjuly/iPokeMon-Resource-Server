from bottle import Bottle, run
from bottle import static_file

app = Bottle()

@app.route('/')
def index():
    return 'Resource is Running'

@app.get('/Thumbnails/<filename:re:.*\.png>')
def get_thumbnail(filename):
    return static_file(filename, root='Thumbnails')

@app.get('/Bundles/<filename:re:.*\.zip>')
def get_package(filename):
    return static_file(filename, root='Bundles')

@app.get('/<filename:re:.*\.json>')
def get_sources(filename):
    return static_file(filename, root='')

#
# Start a server instance
#
run(
        app,                    # Run |app| Bottle() instance
        host     = 'localhost',
        port     = 8888,
        reloader = True,        # restarts the server every time edit a module file
        debug    = True         # Comment out it before deploy
        )
