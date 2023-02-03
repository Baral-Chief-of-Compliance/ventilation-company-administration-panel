from app import app, jsonify, request
from app.stored_procedure import call_stored_procedure


'''BRIGADES'''


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


'''EMPLOYESS'''


@app.route('/admin_panel/api/v1.0/all_employess', methods=['GET'])
def all_employess():
    if request.method == 'GET':
        json_employess= []
        employess = call_stored_procedure('all_employess', commit=False, fetchall=True)

        for emp in employess:
            json_employess.append(
                {
                    'id': emp[0],
                    'surname': emp[1],
                    'name': emp[2],
                    'patronymic': emp[3],
                    'position': emp[4],
                    'phone': emp[5],
                    'br_id': emp[6]
                }
            )

        return jsonify(json_employess)


@app.route('/admin_panel/api/v1.0/add_employee', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        surname = request.args['surname']
        name = request.args['name']
        patronymic = request.args['patronymic']
        position = request.args['position']
        phone = request.args['phone']
        br_id = request.args['br_id']

        call_stored_procedure('add_employee', [surname, name, patronymic, position, phone, br_id], commit=True, fetchall=False)

        return jsonify(f'employee {surname} {name} {patronymic} is add')


@app.route('/admin_panel/api/v1.0/inf_about_employee', methods=['GET'])
def inf_about_employee():
    if request.method == 'GET':
        id = request.args['id']
        inf = call_stored_procedure('inf_about_employee', [id], commit=False, fetchall=False)
        return jsonify(
                        {
                            'surname': inf[0],
                            'name': inf[1],
                            'patronymic': inf[2],
                            'position': inf[3],
                            'phone': inf[4],
                            'br_id': inf[5]
                        }
        )


@app.route('/admin_panel/api/v1.0/delete_employee', methods=['POST'])
def delete_employee():
    if request.method == 'POST':
        id = request.args['id']
        call_stored_procedure('delete_employee', [id], commit=True, fetchall=False)
        return jsonify(f'employee id = {id} is delete')


'''OPERATOR'''


@app.route('/admin_panel/api/v1.0/all_operators', methods=['GET'])
def all_operators():
    if request.method == 'GET':
        json_operators = []
        operators = call_stored_procedure('all_operators', commit=False, fetchall=True)

        for op in operators:
            json_operators.append({
                                    'id': op[0],
                                    'surname': op[1],
                                    'name': op[2],
                                    'patronymic': op[3],
                                    'login': op[4],
                                    'password_hash': op[5],
                                    'phone': op[6]
                                }
            )

        return jsonify(json_operators)


def index():
    return 'Пошел нахуй'