from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self, tc_id=None):
        data = pd.read_csv('users.csv')

        if tc_id:
            user_data = data[data['tc_id'] == int(tc_id)].to_dict('records')
            if user_data:
                return {'data': user_data[0]}, 200
            else:
                return {'message': f"No entry found with this TC ID: {tc_id}."}, 404

        result = data[['name', 'tc_id', 'university']].to_dict('records')
        return {'data': result}, 200

    def post(self):
        name = request.args['name']
        tc_id = request.args['tc_id']
        university = request.args['university']
        req_data = pd.DataFrame({
            'name': [name],
            'tc_id': [int(tc_id)],
            'university': [university]
        })
        data = pd.read_csv('users.csv')
        data = data.append(req_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'message': 'Record successfully added.'}, 200

class Universities(Resource):
    def get(self):
        data = pd.read_csv('users.csv', usecols=[2])
        universities_data = data.to_dict('records')
        return {'data': universities_data}, 200

api.add_resource(Users, '/users', '/users/<string:tc_id>')
api.add_resource(Universities, '/universities')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    app.run()    
