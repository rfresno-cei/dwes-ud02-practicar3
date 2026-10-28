class Envio:
    def __init__(self, codigo, destino, peso, coste_base):
        self.codigo = codigo
        self.destino = destino
        self.peso = peso
        self.coste_base = coste_base

    def get_coste_total(self):
        return self.coste_base

    def es_pesado(self):
        return self.peso > 10

    def __str__(self):
        return f'Envío {self.codigo} con destino {self.destino}'

class EnvioNacional(Envio):
    def __init__(self, codigo, destino, peso, coste_base, iva):
        super().__init__(codigo, destino, peso, coste_base)
        self.iva = iva

    def get_coste_total(self):
        # return self.coste_base + self.coste_base * self.iva / 100
        return self.coste_base * (1 + self.iva / 100)

    def __str__(self):
        return f'Envío nacional {self.codigo} con destino {self.destino}'

class EnvioInternacional(Envio):
    def __init__(self, codigo, destino, peso, coste_base, tasa_aduanas, pais_destino):
        super().__init__(codigo, destino, peso, coste_base)
        self.tasa_aduanas = tasa_aduanas
        self.pais_destino = pais_destino

    def get_coste_total(self):
        return self.coste_base * (1 + self.tasa_aduanas / 100)

    def __str__(self):
        return f'Envío internacional {self.codigo} con destino {self.destino} ({self.pais_destino})'

class EnvioUrgente(Envio):
    def __init__(self, codigo, destino, peso, coste_base, recargo):
        super().__init__(codigo, destino, peso, coste_base)
        self.recargo = recargo

    def get_coste_total(self):
        return self.coste_base + self.recargo

    def __str__(self):
        return f'Envío urgente {self.codigo} con destino {self.destino}'