from flask import Blueprint, render_template, request
from bson import ObjectId

def uses_bp(mongo):
    users_bp = Blueprint('users_bp', __name__, url_prefix='/uses')


    @users_bp.route('/profile/<string:id>', methods=['GET', 'POST'])
    def users_profile(id):
        if request.method == 'GET':
            cursor = mongo.db.usuarios.find_one({'_id':ObjectId(id)})
            return render_template('users/profile.html', user=cursor), 200
        



    return users_bp