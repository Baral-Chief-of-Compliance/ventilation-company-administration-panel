from app import app, jsonify, request
from app.stored_procedure import call_stored_procedure
from app.hash import hash_password
from app.geo import get_longitude, get_latitude


'''BRIGADES'''


@app.route('/admin_panel/api/v1.0/brigades', methods=['GET'])
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
        name = request.json['name']
        call_stored_procedure('add_brigade', [name], commit=True, fetchall=False)
        return jsonify(f'brigade {name} is add')


@app.route('/admin_panel/api/v1.0/brigades/<int:id>', methods=['GET', 'DELETE'])
def inf_about_brigade(id):
    if request.method == 'GET':
        json_employess = []
        name = call_stored_procedure('inf_about_brigade', [id], commit=False, fetchall=False)
        emp_inf = call_stored_procedure('show_all_employess_in_brigade', [id], commit=False, fetchall=True)

        for emp in emp_inf:
            json_employess.append({
                'id': emp[0],
                'surname': emp[1],
                'name': emp[2],
                'patronymic': emp[3],
                'position': emp[4],
                'phone': emp[5]
            })

        return jsonify({'name': name[0], 'employees': json_employess})

    elif request.method == 'DELETE':
        call_stored_procedure('delete_brigade', [id], commit=True, fetchall=False)
        return jsonify(f'brigade id = {id} is delete')


'''EMPLOYEES'''


@app.route('/admin_panel/api/v1.0/employees', methods=['GET'])
def all_employees():
    if request.method == 'GET':
        json_employees = []
        employees = call_stored_procedure('all_employess', commit=False, fetchall=True)

        for emp in employees:
            json_employees.append(
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

        return jsonify(json_employees)


@app.route('/admin_panel/api/v1.0/add_employee', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        surname = request.json['surname']
        name = request.json['name']
        patronymic = request.json['patronymic']
        position = request.json['position']
        phone = request.json['phone']
        br_id = request.json['br_id']

        call_stored_procedure('add_employee', [surname, name, patronymic, position, phone, br_id], commit=True, fetchall=False)

        return jsonify(f'employee {surname} {name} {patronymic} is add')


@app.route('/admin_panel/api/v1.0/employees/<int:id>', methods=['GET', 'DELETE'])
def inf_about_employee(id):
    if request.method == 'GET':
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

    elif request.method == 'DELETE':
        call_stored_procedure('delete_employee', [id], commit=True, fetchall=False)
        return jsonify(f'employee id = {id} is delete')


'''OPERATORS'''


@app.route('/admin_panel/api/v1.0/operators', methods=['GET'])
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


@app.route('/admin_panel/api/v1.0/add_operator', methods=['POST'])
def add_operator():
    if request.method == 'POST':
        surname = request.json['surname']
        name = request.json['name']
        patronymic = request.json['patronymic']
        login = request.json['login']
        hash = hash_password(request.json['password'])
        phone = request.json['phone']

        call_stored_procedure('add_operator', [surname, name, patronymic, login, hash, phone], commit=True, fetchall=False)

        return jsonify(f'operator {login} id add')


@app.route('/admin_panel/api/v1.0/operators/<int:id>', methods=['GET', 'DELETE'])
def inf_about_operator(id):
    if request.method == 'GET':
        inf = call_stored_procedure('inf_about_operator', [id], commit=False, fetchall=False)
        return jsonify(
                        {
                            'surname': inf[0],
                            'name': inf[1],
                            'patronymic': inf[2],
                            'login': inf[3],
                            'password_hash': inf[4],
                            'phone': inf[5]
                        }
        )

    elif request.method == 'DELETE':
        call_stored_procedure('delete_operator', [id], commit=True, fetchall=False)
        return jsonify(f'operator id = {id} is delete')


'''PHYS_CLIENTS'''


@app.route('/admin_panel/api/v1.0/clients/phys_clients', methods=['GET'])
def all_phys_clients():
    if request.method == 'GET':
        json_phys_clients = []
        phys_clients = call_stored_procedure('all_phys_clients', commit=False, fetchall=True)

        for cl in phys_clients:
            json_phys_clients.append({
                                    'id': cl[0],
                                    'surname': cl[1],
                                    'name': cl[2],
                                    'patronymic': cl[3],
                                    'phone': cl[4],
                                    'town': cl[5],
                                    'street': cl[6],
                                    'house': cl[7],
                                    'frame': cl[8],
                                    'apartment': cl[9],
                                    'longitude': cl[10],
                                    'latitude': cl[11]
                                }
            )

        return jsonify(json_phys_clients)


@app.route('/admin_panel/api/v1.0/clients/add_phys_client', methods=['POST'])
def add_phys_client():
    if request.method == 'POST':
        surname = request.json['surname']
        name = request.json['name']
        patronymic = request.json['patronymic']
        phone = request.json['phone']
        town = request.json['town']
        street = request.json['street']
        house = request.json['house']
        frame = request.json['frame']
        apartment = request.json['apartment']
        place = f"{street} {house} {frame}, {town}"

        longitude = get_longitude(place)
        latitude = get_latitude(place)

        call_stored_procedure(
            'create_phys_client',
            [
                surname,
                name,
                patronymic,
                phone,
                town,
                street,
                house,
                frame,
                apartment,
                longitude,
                latitude
            ],
            commit=True,
            fetchall=False
        )

        return jsonify(f'phys client {surname} {name} id add')


@app.route('/admin_panel/api/v1.0/clients/phys_clients/<int:id>', methods=['GET', 'DELETE'])
def phys_clients(id):
    if request.method == 'GET':
        inf = call_stored_procedure('inf_about_phys_client', [id], commit=False, fetchall=False)
        return jsonify(
                        {
                            'surname': inf[0],
                            'name': inf[1],
                            'patronymic': inf[2],
                            'phone': inf[3],
                            'town': inf[4],
                            'street': inf[5],
                            'house': inf[6],
                            'frame': inf[7],
                            'apartment': inf[8],
                            'longitude': inf[9],
                            'latitude': inf[10]

                        }
        )

    elif request.method == 'DELETE':
        call_stored_procedure('delete_phys_clients', [id], commit=True, fetchall=False)
        return jsonify(f'phys client id = {id} is delete')


@app.route('/admin_panel/api/v1.0/clients/entity_clients', methods=['GET'])
def all_entity_clients():
    if request.method == 'GET':
        json_entity_clients = []
        entity_clients = call_stored_procedure('all_entity_clients', commit=False, fetchall=True)

        for cl in entity_clients:
            json_entity_clients.append({
                                    'id': cl[0],
                                    'surname': cl[1],
                                    'name': cl[2],
                                    'patronymic': cl[3],
                                    'phone': cl[4],
                                    'name_of_company': cl[5],
                                    'inn': cl[6]
                                }
            )

        return jsonify(json_entity_clients)


@app.route('/admin_panel/api/v1.0/clients/add_entity_client', methods=['POST'])
def add_entity_client():
    if request.method == 'POST':
        surname = request.json['surname']
        name = request.json['name']
        patronymic = request.json['patronymic']
        phone = request.json['phone']
        name_of_company = request.json['name_of_company']
        inn = request.json['inn']

        call_stored_procedure(
            'add_entity_client',
            [
                surname,
                name,
                patronymic,
                phone,
                name_of_company,
                inn
            ],
            commit=True,
            fetchall=False
        )

        return jsonify(f'entity client {surname} {name} is add')


@app.route('/admin_panel/api/v1.0/clients/entity_clients/<int:id>', methods=['GET', 'DELETE'])
def entity_client(id):
    if request.method == 'GET':
        inf = call_stored_procedure('inf_about_entity_client', [id], commit=False, fetchall=False)
        return jsonify(
                        {
                            'surname': inf[0],
                            'name': inf[1],
                            'patronymic': inf[2],
                            'phone': inf[3],
                            'name_of_company': inf[4],
                            'inn': inf[5]
                        }
        )

    elif request.method == 'DELETE':
        call_stored_procedure('delete_entity_clients', [id], commit=True, fetchall=False)
        return jsonify(f'entity client id = {id} is delete')


'''STACKS'''


@app.route('/admin_panel/api/v1.0/stocks', methods=['GET'])
def stocks():
    if request.method == 'GET':
        json_stocks = []
        stocks = call_stored_procedure('all_stocks', commit=False, fetchall=True)

        for st in stocks:
            json_stocks.append({
                                    'id': st[0],
                                    'town': st[1],
                                    'street': st[2],
                                    'house': st[3],
                                    'frame': st[4],
                                    'apartment': st[5],
                                    'longitude': st[6],
                                    'latitude': st[7]
                                }
            )

        return jsonify(json_stocks)


@app.route('/admin_panel/api/v1.0/stocks/add_stock', methods=['POST'])
def add_stock():
    if request.method == 'POST':
        town = request.json['town']
        street = request.json['street']
        house = request.json['house']
        frame = request.json['frame']

        place = f"{street} {house} {frame}, {town}"

        longitude = get_longitude(place)
        latitude = get_latitude(place)

        call_stored_procedure(
            'add_stock',
            [
                town,
                street,
                house,
                frame,
                longitude,
                latitude
            ],
            commit=True,
            fetchall=False
        )

        return jsonify(f'stock on {town} {street} {house} {frame} id add')


@app.route('/admin_panel/api/v1.0/stocks/<int:id>', methods=['GET', 'DELETE'])
def stock(id):
    if request.method == 'GET':
        json_materials = []
        inf = call_stored_procedure('inf_about_stock', [id], commit=False, fetchall=False)
        materials_inf = call_stored_procedure('show_all_materials_in_stock', [id], commit=False, fetchall=True)

        for mat in materials_inf:
            json_materials.append({
                'id': mat[0],
                'name': mat[2],
                'quantity': mat[3]
            })

        return jsonify(
                        {
                            'address': {
                                'town': inf[0],
                                'street': inf[1],
                                'house': inf[2],
                                'frame': inf[3],
                                'apartment': inf[4],
                                'longitude': inf[5],
                                'latitude': inf[6]
                            },
                            'materials': json_materials
                        }
        )

    elif request.method == 'DELETE':
        call_stored_procedure('delete_stock', [id], commit=True, fetchall=False)
        return jsonify(f'stock id = {id} is delete')


'''MATERIALS'''


@app.route('/admin_panel/api/v1.0/materials', methods=['GET'])
def materials():
    if request.method == 'GET':
        json_materials = []
        materials = call_stored_procedure('all_materials', commit=False, fetchall=True)

        for m in materials:
            json_materials.append({
                                    'id': m[0],
                                    'name': m[1],
                                    'quantity': m[2],
                                    'stack_id': m[3],
                                    'town': m[4],
                                    'street': m[5],
                                    'house': m[6],
                                    'frame': m[7],
                                    'apartment': m[8],
                                    'longitude': m[9],
                                    'latitude': m[10]
                                }
            )

        return jsonify(json_materials)


@app.route('/admin_panel/api/v1.0/materials/<int:id>', methods=['GET', 'DELETE'])
def material_info(id):
    if request.method == 'DELETE':
        call_stored_procedure('delete_material', [id], commit=True, fetchall=False)
        return jsonify(f'material id = {id} is delete')


@app.route('/admin_panel/api/v1.0/materials/add_material', methods=['POST'])
def add_material():
    if request.method == 'POST':
        stock_id = request.json['stock_id']
        name_of_material = request.json['name_of_material']
        quantity = request.json['quantity']

        call_stored_procedure(
            'add_material',
            [
                stock_id,
                name_of_material,
                quantity
            ],
            commit=True,
            fetchall=False
        )

        return jsonify(f'material: stock id:{stock_id} {name_of_material} {quantity} is add')


'''applications'''
@app.route('/admin_panel/api/v1.0/applications/all_phys_client_apllication', methods=['GET'])
def all_phys_client_apllication():
    if request.method == 'GET':
        json_phys_clients = []
        phys_clients = call_stored_procedure('all_phys_client_apllication', commit=False, fetchall=True)

        for p in phys_clients:
            json_phys_clients.append(f'{p[1]} {p[2]} {p[3]} {p[4]}')

        return jsonify(json_phys_clients)


@app.route('/admin_panel/api/v1.0/applications/all_entity_client_apllication', methods=['GET'])
def all_entity_client_apllication():
    if request.method == 'GET':
        json_entity_clients = []
        entity_clients = call_stored_procedure('all_entity_client_apllication', commit=False, fetchall=True)

        for e in entity_clients:
            json_entity_clients.append(f'{e[1]} {e[2]} {e[3]} {e[4]} {e[5]}')

        return jsonify(json_entity_clients)

@app.route('/admin_panel/api/v1.0/applications/all_stocks_apllication', methods=['GET'])
def all_stocks_apllication():
    if request.method == 'GET':
        json_stocks = []
        stocks = call_stored_procedure('all_stocks', commit=False, fetchall=True)

        for st in stocks:
            json_stocks.append(f'Склад {st[0]} адрес: г.{st[1]} ул.{st[2]} д.{st[3]} {st[4]}')

        return jsonify(json_stocks)


@app.route('/admin_panel/api/v1.0/applications/add_application', methods=['POST'])
def add_application():
    if request.method == 'POST':
        cl_id = request.json['cl_id']
        op_id = request.json['op_id']
        br_id = request.json['br_id']
        date_of_order = request.json['date_of_order']
        date_of_start_work = request.json['date_of_start_work']
        date_of_end_work = request.json['date_of_end_work']
        date_of_really_end_work = request.json['date_of_really_end_work']
        days_of_delay = request.json['days_of_delay']
        town = request.json['town']
        street = request.json['street']
        house = request.json['house']
        frame = request.json['frame']
        apartment = request.json['apartment']

        place = f"{street} {house} {frame}, {town}"

        longitude = get_longitude(place)
        latitude = get_latitude(place)

        call_stored_procedure(
            'add_application',
            [
                cl_id,
                op_id,
                br_id,
                date_of_order,
                date_of_start_work,
                date_of_end_work,
                date_of_really_end_work,
                days_of_delay,
                town,
                street,
                house,
                frame,
                apartment,
                longitude,
                latitude
            ],
            commit=True,
            fetchall=False
        )

        return jsonify(f'order {date_of_order}  is add')


