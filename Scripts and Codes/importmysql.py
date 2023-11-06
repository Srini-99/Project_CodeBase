import mysql.connector
import json

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="neo4jtest"
)

cursor = conn.cursor()

# Open the NDJSON file
with open(r"D:\Sem3_Materials\Project\old\log\nodefact.ndjson", "r") as file:
    for line in file:
        data = json.loads(line)
        cursor.execute("INSERT IGNORE INTO nodefact (id, type) VALUES (%s, %s)", (data['id'], data['type']))

conn.commit()

with open(r"D:\Sem3_Materials\Project\old\log\procfact.ndjson", "r") as file:
    for line in file:
        data = json.loads(line)
        cursor.execute("INSERT IGNORE INTO procfact (id, pid, exe, ppid, args) VALUES (%s, %s, %s, %s, %s)", (data['id'], data['pid'], data['exe'], data['ppid'],data['args']))

conn.commit()

with open(r"D:\Sem3_Materials\Project\old\log\socketfact.ndjson", "r") as file:
    for line in file:
        data = json.loads(line)
        cursor.execute("INSERT IGNORE INTO sockfact (id, name) VALUES (%s, %s)", (data['id'], data['name']))

conn.commit()

with open(r"D:\Sem3_Materials\Project\old\log\edgefact_0.ndjson", "r") as file:
    for line in file:
        data = json.loads(line)
        cursor.execute("INSERT IGNORE INTO edgefact (e_id, n1_hash, n2_hash, relation, sequence, session, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)", (data['e_id'], data['n1_hash'], data['n2_hash'], data['relation'],data['sequence'], data['session'],data['timestamp']))

conn.commit()

with open(r"D:\Sem3_Materials\Project\old\log\filefact.ndjson", "r") as file:
    for line in file:
        data = json.loads(line)
        cursor.execute("INSERT IGNORE INTO filefact (id, name, version) VALUES (%s, %s, %s)", (data['id'], data['name'], data['version']))

conn.commit()

conn.close()
