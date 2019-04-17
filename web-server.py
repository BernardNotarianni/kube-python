from bottle import route, run, template

@route('/')
def index():
    return '<html><b>We are devops rockstars!!</b></html>'

run(host='localhost', port=8000)

