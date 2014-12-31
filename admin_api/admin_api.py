import json
import config
from flask import Blueprint
from storage import Storage

__author__ = 'carlozamagni'

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')

boards_collection = Storage(host=config.db_host).get_collection(db='boards_register',
                                                                collection_name='registered_boards')

@admin.route('/reset')
def reset():
    res = boards_collection.remove({})
    return json.dumps({'removed': res.get('n')})