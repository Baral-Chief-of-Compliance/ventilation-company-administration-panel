from app import app
from app.stored_procedure import call_stored_procedure


@app.route('/')
@app.route('/index')
def index():
    return 'Пошел нахуй'