import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()

cursor.execute('''
    SELECT * FROM estudantes
''')

estudantes = cursor.fetchall()

for estudante in estudantes:
    print(estudante)

cursor.execute('''
    SELECT * FROM disciplinas
''')

disciplinas = cursor.fetchall()

for disciplina in disciplinas:
    print(disciplina)

    conn.close()