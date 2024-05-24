from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
grades = {}

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    id = data.get('id')
    if id in students:
        return jsonify({"message": "Student already exists"}), 400
    students[id] = {"id": id, "grades": []}
    return jsonify({"message": "Student created successfully"}), 201

@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    student = students.get(id)
    if student:
        return jsonify(student), 200
    return jsonify({"message": "Student not found"}), 404

@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    if id not in students:
        return jsonify({"message": "Student not found"}), 404
    students[id].update(data)
    return jsonify({"message": "Student updated successfully"}), 200

@app.route('/students/<id>', methods=['DELETE'])
def delete_student(id):
    if id in students:
        del students[id]
        return jsonify({"message": "Student deleted successfully"}), 200
    return jsonify({"message": "Student not found"}), 404

@app.route('/grades', methods=['POST'])
def create_grade():
    data = request.get_json()
    student_id = data.get('student_id')
    grade_id = data.get('grade_id')
    grade = data.get('grade')
    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404
    for g in students[student_id]['grades']:
        if g['grade_id'] == grade_id:
            return jsonify({"message": "Grade ID already exists for this student"}), 400
    students[student_id]['grades'].append({"grade_id": grade_id, "grade": grade})
    return jsonify({"message": "Grade created successfully"}), 201

@app.route('/grades/<student_id>/<grade_id>', methods=['GET'])
def get_grade(student_id, grade_id):
    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404
    for g in students[student_id]['grades']:
        if g['grade_id'] == grade_id:
            return jsonify(g), 200
    return jsonify({"message": "Grade not found for this student"}), 404

@app.route('/grades/<student_id>/<grade_id>', methods=['PUT'])
def update_grade(student_id, grade_id):
    data = request.get_json()
    grade = data.get('grade')
    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404
    for g in students[student_id]['grades']:
        if g['grade_id'] == grade_id:
            g['grade'] = grade
            return jsonify({"message": "Grade updated successfully"}), 200
    return jsonify({"message": "Grade not found for this student"}), 404

@app.route('/grades/<student_id>/<grade_id>', methods=['DELETE'])
def delete_grade(student_id, grade_id):
    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404
    for g in students[student_id]['grades']:
        if g['grade_id'] == grade_id:
            students[student_id]['grades'].remove(g)
            return jsonify({"message": "Grade deleted successfully"}), 200
    return jsonify({"message": "Grade not found for this student"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
