from app import mysql 
def selectAll():
    cursor = mysql.connection.cursor()

    #execute: ejecutar la consulta
    cursor.execute("SELECT * from tb_alumnos WHERE state=1")
    #fechall: obtener los valores
    consulta = cursor.fetchall()
    #close: cerrar consulta
    cursor.close()
    return consulta

#funcion insertar
def insertEstudiante(nombre, carrera):
    cursor= mysql.connection.cursor()
    # se usa %s por ser screen
    cursor.execute("INSERT INTO tb_alumnos(nombre,carrera) VALUES (%s,%s)",(nombre,carrera))
    mysql.connection.commit()
    #close: cerrar consulta
    cursor.close()        

# funcion eliminar (softdelete)
def softDeleteEstudiante(id):
    cursor= mysql.connection.cursor()
    cursor.execute("UPDATE tb_alumnos SET state =0 WHERE id=%s",(id))
    mysql.connection.commit()
    #close: cerrar consulta
    cursor.close()           

# funcion actualizar
def actualizarEstudiante(nombre,carrera,id):
    cursor= mysql.connection.cursor()
    cursor.execute("UPDATE tb_alumnos SET nombre=%s, carrera=%s WHERE id=%s",(nombre,carrera,id))
    mysql.connection.commit()
    #close: cerrar consulta
    cursor.close()           