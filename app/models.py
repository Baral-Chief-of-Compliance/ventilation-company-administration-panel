from app import db


class Operator(db.Model):
    __tablename__ = 'operator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    patronymic = db.Column(db.String(64), nullable=True)
    phone = db.Column(db.String(12), nullable=False, index=True, unique=True)
    login = db.Column(db.String(64), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'operator: {}'.format(self.login)


class Brigade(db.Model):
    __tablename__ = 'brigade'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    employee = db.relationship('employee', backref='Brigade')

    def __repr__(self):
        return 'brigade: {}'.format(self.name)


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    patronymic = db.Column(db.String(64), nullable=True)
    role = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(12), nullable=False, index=True, unique=True)
    brigade_id = db.Column(db.Integer, db.ForeignKey('brigade.id', ondelete='CASCADE', onupdate='CASCADE'))

    def __repr__(self):
        return 'employee: {}'.format(self.name, self.surname, self.role)


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(64), nullable=False)
    house = db.Column(db.Integer, nullable=False)
    frame = db.Column(db.Integer, nullable=True)
    latitude = db.Column(db.String(20), nullable=False, index=True)
    longitude = db.Column(db.String(20), nullable=False, index=True)
    phys = db.relationship('Phys', back_populates='address')

    def __repr__(self):
        return 'address: {}'.format(self.street, self.house, self.latitude, self.longitude)


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    patronymic = db.Column(db.String(64), nullable=True)
    phone = db.Column(db.String(12), nullable=False, index=True, unique=True)
    phys = db.relationship('Phys', back_populates='client')
    entity = db.relationship('Entity', back_populates='client')


class Phys(db.Model):
    __tablename__ = 'phys'

    client_id = db.Column(db.Integer, db.ForeignKey('client.id',  ondelete='CASCADE', onupdate='CASCADE'),  primary_key=True)
    client = db.relationship('Client', back_populates='phys')
    address_id = db.Column(db.Integer, db.ForeignKey('address.id', ondelete='CASCADE', onupdate='CASCADE'))
    address = db.relationship('Address', back_populates='phys')

    def __repr__(self):
        return 'phys: {}'.format(self.client_id, self.address_id)


class Entity(db.Model):
    __tablename__ = 'entity'

    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE', onupdate='CASCADE'),  primary_key=True)
    client = db.relationship('Client', back_populates='entity')
    name_of_company = db.Column(db.String(64), nullable=False)
    inn = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return 'entity: {}'.format(self.name_of_company, self.inn)