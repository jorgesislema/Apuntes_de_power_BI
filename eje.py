import simpy
import random

class Banco:
    def __init__(self, env, num_cajeros):
        self.env = env
        self.cajero = simpy.Resource(env, num_cajeros)
    
    def atender_cliente(self, cliente):
        # Tiempo de servicio realista (5-15 minutos)
        tiempo_servicio = random.uniform(5, 15)
        yield self.env.timeout(tiempo_servicio)

def cliente(env, nombre, banco, datos):
    llegada = env.now
    with banco.cajero.request() as solicitud:
        yield solicitud
        tiempo_espera = env.now - llegada
        yield env.process(banco.atender_cliente(nombre))
        
    # Guardamos datos sintéticos del comportamiento del cliente
    datos.append({
        'cliente': nombre,
        'tiempo_llegada': llegada,
        'tiempo_espera': tiempo_espera,
        'satisfaccion': calcular_satisfaccion(tiempo_espera)
    })
