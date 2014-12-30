import datetime
import json
from flask import Flask, render_template
import config
from storage import Storage

app = Flask(__name__)

boards_collection = Storage(host=config.db_host).get_collection(db='boards_register',
                                                                collection_name='registered_boards')

@app.route('/')
def home():
    registed_boards_num = boards_collection.find({}).count()
    return render_template('index.html', counter=registed_boards_num)

@app.route('/register/<guid>')
def register(guid):

    boards_collection.find_and_modify({'_id': str(guid)},
                                      {'$set': {'registered_on': datetime.datetime.utcnow()}},
                                      upsert=True)

    return json.dumps({'id': str(guid)})



if __name__ == '__main__':
    app.run()
