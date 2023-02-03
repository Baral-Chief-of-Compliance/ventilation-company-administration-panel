from app import app, jsonify, request
from app.stored_procedure import call_stored_procedure


@app.route('/admin_panel/api/v1.0/all_brigades', methods=['GET'])
def all_brigades():
    if request.method == 'GET':
        json_brigades = []
        brigades = call_stored_procedure('all_brigades', commit=False, fetchall=True)

        for br in brigades:
            json_brigades.append({'id': br[0], 'name': br[1]})

        return jsonify(json_brigades)


@app.route('/admin_panel/api/v1.0/create_brigades', methods=['POST'])
def create_brigades():
    if request.method == 'POST':
        name = request.args['name']
        call_stored_procedure('add_brigade', [name], commit=True, fetchall=False)
        return jsonify(f'brigade {name} is add')


@app.route('/admin_panel/api/v1.0/inf_about_brigade', methods=['GET'])
def inf_about_brigade():
    if request.method == 'GET':
        id = request.args['id']
        inf = call_stored_procedure('inf_about_brigade', [id], commit=False, fetchall=False)
        return jsonify({'name': inf[0]})


@app.route('/admin_panel/api/v1.0/delete_brigade', methods=['POST'])
def delete_brigade():
    if request.method == 'POST':
        id = request.args['id']
        call_stored_procedure('delete_brigade', [id], commit=True, fetchall=False)
        return jsonify(f'brigade id = {id} is delete')


@app.route('/index')
def index():
    return 'Пошел нахуй'