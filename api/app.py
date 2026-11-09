from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def conectar_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            hora INT NOT NULL,
            categoria VARCHAR(100) NOT NULL,
            ingreso_total DECIMAL(18,2) NOT NULL,
            UNIQUE KEY unica_hora_categoria (hora, categoria)
        )
    """)

    conexion.commit()
    cursor.close()
    conexion.close()

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API DataMart funcionando",
        "matricula": "125053108",
        "estado": "Activo"
    })

@app.route("/conexion")
def verificar_conexion():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE()")
        nombre_db = cursor.fetchone()[0]
        cursor.close()
        conexion.close()

        return jsonify({
            "estado": "Conectado correctamente",
            "base_de_datos": nombre_db
        })

    except mysql.connector.Error as error:
        return jsonify({
            "estado": "Error de conexion",
            "detalle": str(error)
        }), 500


@app.route("/resultados", methods=["GET"])
def obtener_resultados():
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, hora, categoria, ingreso_total
        FROM resultados
        ORDER BY hora, categoria
    """)

    resultados = cursor.fetchall()

    for resultado in resultados:
        resultado["ingreso_total"] = float(
            resultado["ingreso_total"]
        )

    cursor.close()
    conexion.close()

    return jsonify(resultados)


@app.route("/resultados/<categoria>", methods=["GET"])
def filtrar_resultados(categoria):
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, hora, categoria, ingreso_total
        FROM resultados
        WHERE categoria = %s
        ORDER BY hora
    """, (categoria,))

    resultados = cursor.fetchall()

    for resultado in resultados:
        resultado["ingreso_total"] = float(
            resultado["ingreso_total"]
        )

    cursor.close()
    conexion.close()

    return jsonify(resultados)


@app.route("/resultados", methods=["POST"])
def guardar_resultado():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "Envia un JSON valido"}), 400

    try:
        hora = int(datos["hora"])
        categoria = str(datos["categoria"]).strip()
        ingreso = float(datos["ingreso_total"])

        if not 0 <= hora <= 23 or not categoria or ingreso < 0:
            return jsonify({"error": "Datos invalidos"}), 400

    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Faltan datos o son incorrectos"}), 400

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO resultados (hora, categoria, ingreso_total)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE ingreso_total = VALUES(ingreso_total)
    """, (hora, categoria, ingreso))

    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Resultado guardado correctamente"}), 201


if __name__ == "__main__":
    crear_tabla()
    app.run(host="0.0.0.0", port=5000)
