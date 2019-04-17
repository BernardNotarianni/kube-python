from bottle import route, run, template

@route('/')
def index():
    return '<html><b>We are devops rockstars!!</b></html>'

run(host='0.0.0.0', port=8000)

