# request para peticion y jsonify para respuestas
from flask import Blueprint,request, jsonify

# importar las funciones del archivo modelEstudiante de la carpeta Models
from Models.modelEstudiante import *

#Primer objeto controlador con constructor "name", sirve para aplicar y utilizar las rutas
controladorAlumnoBP = Blueprint('controladorAlumno', __name__)

#Cambiamos la ruta de app para agregar el controlador como objeto de las rutasx
@controladorAlumnoBP.route('/')
def inicio():
    return "Hola soy el backend de Alumno"

#Ruta para insert
@controladorAlumnoBP.route('/guardarAlumno', methods=['POST'])
def guardar():
    nombreReq = request.form.get('txtNombre').strip()
    carreraReq = request.form.get('txtCarrera').strip()

    try:
        insertEstudiante(nombreReq,carreraReq)
        return jsonify({"Completado":"estudiante guardado"}),200
    except Exception as e:
        return jsonify({"Error": str(e)}),500


#Ruta para consulta
@controladorAlumnoBP.route('/consultatodo')
def consultatodo():
    try:
        datos = selectAll()
        return jsonify({"Consultado":datos}),200
    except Exception as e:
            return jsonify({"Error": str(e)}),500
#Ruta para actualizar
@controladorAlumnoBP.route('/actualizarAlumno', methods=['PUT'])
def actualizar():
    try:
        idReq = request.form.get('txtId').strip()
        nombreReq = request.form.get('txtNombre').strip()
        carreraReq = request.form.get('txtCarrera').strip()
        actualizarEstudiante(nombreReq,carreraReq,idReq)
        return jsonify({"Actualizar":"Se actualizó correctamente"}),200
    except Exception as e:
        return jsonify ({"Exception": str(e)}),500

#Ruta para eliminar
@controladorAlumnoBP.route('/eliminarAlumno', methods=['DELETE'])
def eliminar():
    idReq = request.form.get('txtId').strip()
    try:
        softDeleteEstudiante(idReq)
        return jsonify({"Eliminado":" Eliminado exitosamente"}),200
    except Exception as e:
        return jsonify({"Error": str(e)}),500
    
#Ruta para consultar uno
@controladorAlumnoBP.route('/consultarUno')
def consultarUno():
    try:
        idReq = request.form.get('txtId').strip()
        datos = consultarUnEstudiante(idReq)
        return jsonify({"Consultado":datos}),200
    except Exception as e:
            return jsonify({"Error": str(e)}),500
