""" Módulo que contiene la función crear_blueprint. """
from flask import Blueprint

def crear_blueprint(identificador: str, prefijo_url: str):
    """ Crea un blueprint con un prefijo de URL. """
    return Blueprint(identificador, __name__, url_prefix=prefijo_url)