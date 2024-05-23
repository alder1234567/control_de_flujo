class GrassSintetico:
    def _init_(self):
        self.horarios_disponibles = ["9:00 AM", "11:00 AM", "3:00 PM", "5:00 PM"]
        self.reservas = []

    def ver_horarios_disponibles(self):
        print("Horarios Disponibles:")
        for horario in self.horarios_disponibles:
            print(horario)

    def reservar_horario(self, horario):
        if horario in self.horarios_disponibles:
            self.reservas.append(horario)
            print(f"¡Reserva realizada para el horario {horario}!")
        else:
            print("Horario no válido. Inténtalo de nuevo.")

    def pagar_alquiler(self):
        costo_alquiler = 50  # Costo del alquiler
        print(f"Pago del alquiler por ${costo_alquiler} realizado con éxito.")

    def verificar_alquileres(self):
        print("Reservas realizadas:")
        for reserva in self.reservas:
            print(f"Fecha y Hora: {reserva}, Costo: $50")  # Costo fijo en este ejemplo

# Crear instancia del sistema de control de grass sintético
sistema_grass = GrassSintetico()

# Ejemplo de uso
sistema_grass.ver_horarios_disponibles()
sistema_grass.reservar_horario("11:00 AM")
sistema_grass.pagar_alquiler()
sistema_grass.verificar_alquileres(