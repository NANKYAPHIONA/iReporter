"""initialising flask"""
from flask import Flask, request, jsonify


app = Flask(__name__)

red_flag = []


@app.route('/api/v1/red-flags', methods=['POST'])
def create_red_flags():
    req = request.json

    if not req:
        return jsonify({
            'status': 404,
            'error': 'No data'
        }), 404

    red_flag.append(req)
    return jsonify({
        'status': 201,
        'data': red_flag
        }), 201


@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_red_flags():
    return jsonify(
        {
            'status': 200,
            'data': red_flag
        }
    ), 200


@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['GET'])
def get_specific_red_flag(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    return jsonify(
        {
            'status': 200,
            'data': flags
        }
    ), 200


@app.route('/api/v1/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_specific_red_flags(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    flags[0]['location'] = request.json['location']

    if not flags[0]['location']:
        return jsonify(
            {
                'status': 404,
                'error': 'No data'
            }
        ), 404

    return jsonify(
        {
            'status': 204,
            'data': [{
                'id': red_flag_id,
                'message': "updated red-flag record's location"
            }]
        }
    ), 204


@app.route('/api/v1/red-flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_specific_comment(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    flags[0]['comment'] = request.json['comment']
    return jsonify(
        {
            'status': 204,
            'data': [{
                'id': red_flag_id,
                'message': "updated red-flag record's comment"
            }]
        }
    ), 204


@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_specific_red_flag(red_flag_id):
    flags = [flag for flag in red_flag if flag["id"] == red_flag_id]
    red_flag.remove(flags[0])
    return jsonify(
        {
            'status': 202,
            'data': [{
                'id': red_flag_id,
                'message': "red-flag record has been deleted"
            }]
        }
    ), 202


if __name__ == "__main__":
    app.run(debug=True)
