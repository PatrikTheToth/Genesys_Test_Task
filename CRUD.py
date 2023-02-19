from flask import Flask, jsonify, request, make_response
import sqlite3
import datetime

app = Flask(__name__)

# Database connection
global_conn = sqlite3.connect('user.db')
global_cursor = global_conn.cursor()

# Create users table
global_cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL,
                 password TEXT NOT NULL,
                 last_login DATE NOT NULL)''')
global_conn.commit()


# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    # Get the data from the HTTP request
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    # last login time is set as the creation timestamp
    last_login = datetime.datetime.now()

    # Check if the user already exists in the database
    create_conn = sqlite3.connect('user.db')
    create_cursor = create_conn.cursor()
    create_cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = create_cursor.fetchone()
    if user:
        # Return an error response if the email already exists
        return make_response(jsonify({'message': 'User with this email already exists'}), 409)

    # Insert the new user record if the email does not exist
    create_cursor.execute("INSERT INTO users (name, email, password, last_login) VALUES (?, ?, ?, ?)",
                          (name, email, password, last_login))
    create_conn.commit()

    # Close the database connection when the request is complete
    create_cursor.close()
    create_conn.close()

    return jsonify({'message': 'User created successfully!'})


# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Get the data from the HTTP request
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    # treating update as a login here, just like with create
    last_login = datetime.datetime.now()

    update_conn = sqlite3.connect('user.db')
    update_cursor = update_conn.cursor()

    update_cursor.execute("UPDATE users SET name=?, email=?, password=?, last_login=? WHERE id=?",
                          (name, email, password, last_login, user_id))
    update_conn.commit()

    update_cursor.close()
    update_conn.close()

    return jsonify({'message': 'User updated successfully!'})


# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_conn = sqlite3.connect('user.db')
    delete_cursor = delete_conn.cursor()

    delete_cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    delete_conn.commit()

    delete_cursor.close()
    delete_conn.close()

    return jsonify({'message': 'User deleted successfully!'})


# List all users
@app.route('/users', methods=['GET'])
def list_users():
    list_conn = sqlite3.connect('user.db')
    list_cursor = list_conn.cursor()

    list_cursor.execute("SELECT * FROM users")
    rows = list_cursor.fetchall()
    users = []
    for row in rows:
        user = {'id': row[0], 'name': row[1], 'email': row[2], 'password': row[3], 'last_login': row[4]}
        users.append(user)

    list_cursor.close()
    list_conn.close()
    return jsonify(users)


# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    login_conn = sqlite3.connect('user.db')
    login_cursor = login_conn.cursor()

    # Check if a user exists in the database with the same email and password
    login_cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = login_cursor.fetchone()

    if user:
        # if we get a hit update the login time, as simulating a login scenario
        now = datetime.datetime.now()
        login_cursor.execute("UPDATE users SET last_login = ? WHERE email = ?", (now, email))
        login_conn.commit()

        login_cursor.close()
        login_conn.close()
        return jsonify({'message': 'Login successful!'})
    else:
        # if the user data provided does not produce a match in the DB, give an error.
        login_cursor.close()
        login_conn.close()
        return make_response(jsonify({'message': 'Invalid email or password'}), 401)


if __name__ == '__main__':
    app.run(debug=True)
