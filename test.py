from main import calculadora

def test_suma_numeros():
    calc = calculadora()
    resultado = calc.suma(2, 3)
    assert resultado == 5, f"Se esperaba pero se obtuvio {resultado}"