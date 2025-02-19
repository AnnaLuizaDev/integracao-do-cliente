import sqlite3

conn = sqlite3.connect('squad.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS squad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tempo_empresa INTEGER NOT NULL,
    squad TEXT NOT NULL,
    funcao TEXT NOT NULL
)
''')

conn.commit()
conn.close()

import sqlite3


def conectar():
    return sqlite3.connect('squad.db')


def cadastrar_integrante(nome, tempo_empresa, squad, funcao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO squad (nome, tempo_empresa, squad, funcao)
    VALUES (?, ?, ?, ?)
    ''', (nome, tempo_empresa, squad, funcao))
    conn.commit()
    conn.close()


def listar_integrantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM squad')
    registros = cursor.fetchall()
    conn.close()
    return registros


def atualizar_integrante(id, nome, tempo_empresa, squad, funcao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE squad
    SET nome = ?, tempo_empresa = ?, squad = ?, funcao = ?
    WHERE id = ?
    ''', (nome, tempo_empresa, squad, funcao, id))
    conn.commit()
    conn.close()


def deletar_integrante(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM squad WHERE id = ?', (id))
    conn.commit()
    conn.close()


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Integrante")
        print("2. Listar Integrantes")
        print("3. Atualizar Integrante")
        print("4. Deletar Integrante")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            tempo_empresa = int(input("Tempo de Empresa (em anos): "))
            squad = input("Squad: ")
            funcao = input("Função: ")
            cadastrar_integrante(nome, tempo_empresa, squad, funcao)
        elif opcao == '2':
            integrantes = listar_integrantes()
            for integrante in integrantes:
                print(integrante)
        elif opcao == '3':
            id = int(input("ID do Integrante: "))
            nome = input("Nome: ")
            tempo_empresa = int(input("Tempo de Empresa (em anos): "))
            squad = input("Squad: ")
            funcao = input("Função: ")
            atualizar_integrante(id, nome, tempo_empresa, squad, funcao)
        elif opcao == '4':
            id = int(input("ID do Integrante: "))
            deletar_integrante(id)
        elif opcao == '5':
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
