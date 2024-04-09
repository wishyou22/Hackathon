from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import decimal

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def display_data():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            port=3306,
            password='Vishu@2209',
            database='test1'
        )
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute a query to retrieve data from the table
        cursor.execute("SELECT * FROM transactions")
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Convert the data to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'amount': float(row[2]),  # Convert decimal.Decimal to float
                'time': str(row[1]) if row[1] else None  # Convert to string
            })
        
        # Return JSON response
        return jsonify(data)
            
    except mysql.connector.Error as e:
        return jsonify({'error': f"Error retrieving data from MySQL database: {e}"})
        
    finally:
        # Close the cursor and connection
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)

