# app.py
from flask import Flask, request, jsonify
from sorting_algorithms import merge_sort

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json()
    array = data.get('array')
    
    sorted_array = merge_sort(array)
    
    return jsonify({'sorted_array': sorted_array})

if __name__ == '__main__':
    app.run(debug=True,port=5000,use_reloader=False)
