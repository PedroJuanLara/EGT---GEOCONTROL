"""
EGT GeoControl

DDR Test Parser

Primera prueba de extracción de datos
desde un Daily Drilling Report.
"""

from parser import DDRData


def test_ddr():

    ddr = DDRData()

    ddr.reporte = 1

    ddr.fecha = "2026-05-14"

    ddr.dia_campania = 1

    ddr.md = 66.0

    ddr.tvd = 66.0

    ddr.hole_made = 66.0

    ddr.rop = 0.0

    ddr.coste_acumulado = 1633394

    ddr.afe_pct = 14.09

    ddr.npt = 0

    return ddr


if __name__ == "__main__":

    resultado = test_ddr()

    print("===== DDR TEST =====")

    print(
        f"Reporte: {resultado.reporte}"
    )

    print(
        f"Fecha: {resultado.fecha}"
    )

    print(
        f"Día Campaña: {resultado.dia_campania}"
    )

    print(
        f"MD: {resultado.md}"
    )

    print(
        f"Coste Acumulado: {resultado.coste_acumulado}"
    )

    print(
        f"AFE %: {resultado.afe_pct}"
    )
