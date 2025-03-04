"""Módulo de utilidades"""
import os
import time


def time_millis():
    """ Obtiene el tiempo en milisegundos """
    return int(time.time() * 1000)


def broker_host():
    """Obtiene el host del broker"""
    return os.getenv('BROKER_HOST', default="localhost")
