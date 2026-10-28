from transporte import EnvioNacional, EnvioInternacional, EnvioUrgente
from viajes import Camping, Hotel

'''en = EnvioNacional('00X3/33-00403', 'Córdoba', 9.9, 25, 47)
print(en)
print(en.get_coste_total())

ei = EnvioInternacional('HolaSoyUnCodigo', 'Helsinki', 18.18, 49, 67, 'Finlandia')
print(ei)
print(ei.get_coste_total())

eu = EnvioUrgente('AdiosNoSoyUnCodigo', 'Varsovia', 25.25, 59, 55)
print(eu)
print(eu.get_coste_total())'''

hotel = Hotel('CEI', 200, 'Buenos Aires', 3, False)
print(hotel)
print(hotel.calcular_precio(2))

camping = Camping('La Torrecilla', 25, 'El Bosque', 18, 23, True)
print(camping)
print(camping.calcular_precio(11))
print(camping.get_capacidad_restante())