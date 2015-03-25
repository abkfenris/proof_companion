from proof_companion.core import db
from .common import CommonColumns


class Contact(CommonColumns):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(120))
    fullname = db.column_property(firstname + ' ' + lastname)
