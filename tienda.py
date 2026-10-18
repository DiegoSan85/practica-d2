"""Calcula el descuento que se aplica a una compra en una tienda.

Si la compra llega a 100 € se descuenta un 10 %, y si llega a 300 €,
un 15 %. Por debajo de 100 € no hay descuento.

Módulo 0485 Programación · UD 2 · Práctica D2
Autor: Diego Sánchez Azorín · Fecha: 18/10/2026
"""

# Constantes
UMBRAL_DESCUENTO_BAJO = 100.0
UMBRAL_DESCUENTO_ALTO = 300.0
DESCUENTO_BAJO = 0.10
DESCUENTO_ALTO = 0.15


def calcular_porcentaje(importe):
    """Devuelve el porcentaje de descuento que corresponde al importe.

    Recibe el importe de la compra en euros y devuelve 0.15, 0.10 o 0.0.
    """
    if importe >= UMBRAL_DESCUENTO_ALTO:
        return DESCUENTO_ALTO
    elif importe >= UMBRAL_DESCUENTO_BAJO:
        return DESCUENTO_BAJO
    else:
        return 0.0


def main():
    """Pide el importe de la compra y muestra el descuento y el total."""
    # Entrada
    importe = float(input("Importe de la compra (€): "))

    # Proceso y salida
    if importe < 0:
        print("Error: el importe no puede ser negativo.")
    else:
        porcentaje = calcular_porcentaje(importe)
        descuento = importe * porcentaje
        total = importe - descuento

        print(f"  Descuento aplicado: {porcentaje * 100:5.0f} %")
        print(f"  Importe:            {importe:8.2f} €")
        print(f"  Descuento:          {descuento:8.2f} €")
        print(f"  Total a pagar:      {total:8.2f} €")


if __name__ == "__main__":
    main()
