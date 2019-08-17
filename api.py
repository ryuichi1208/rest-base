from flask import Blueprint, request, abort, jsonify

from models import db, User

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/users', methods=['GET'])
def list_user():
    q_limit = request.args.get('limit', default=-1, type=int)
    q_offset = request.args.get('offset', default=0, type=int)

    if q_limit == -1:
        users = User.query.all()
    else:
        users = User.query.offset(q_offset).limit(q_limit)

    return jsonify({'users': [user.to_dict() for user in users]})


@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id=None):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user.to_dict())


@api.route('/users', methods=['POST'])
def post_user():
    payload = request.json
    name = payload.get('name')
    age = payload.get('age')

    user = User(name, age)
    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.headers['Location'] = '/api/users/%d' % user.id
    return response, 201


@api.route('/users/<user_id>', methods=['PUT'])
def put_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'user not found'})

    payload = request.json
    user.name = payload.get('name')
    user.age = payload.get('age')
    db.session.commit()

    return jsonify(user.to_dict())


@api.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'user not found'})

    db.session.delete(user)
    db.session.commit()

    return jsonify(None), 204


@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
