# =====================================================================
# PROGRAMA: Calculadora de Índice de Masa Corporal (IMC)
# =====================================================================

print("--- BIENVENIDO A LA CALCULADORA DE IMC ---")

try:
    # 1. SOLICITUD DE DATOS
    # Solicitamos el peso en kilogramos y lo convertimos a decimal (float)
    peso = float(input("Por favor, ingresa tu peso en kg (ej. 70.5): "))
    
    # Solicitamos la estatura en metros y la convertimos a decimal (float)
    estatura = float(input("Por favor, ingresa tu estatura en metros (ej. 1.75): "))

    # 2. CÁLCULO DEL IMC
    # La fórmula matemática es: IMC = peso / (estatura^2)
    imc = peso / (estatura ** 2)

    # 3. MOSTRAR RESULTADO GENERAL
    # Mostramos el IMC redondeado a 2 decimales usando la función round()
    print(f"\nTu Índice de Masa Corporal es: {round(imc, 2)}")

    # 4. CLASIFICACIÓN DEL RESULTADO (Según la OMS)
    # Evaluamos el valor del IMC mediante estructuras condicionales (if-elif-else)
    print("Clasificación actual: ", end="")
    
    if imc < 18.5:
        print("Bajo peso")
        print("💡 Consejo: Sería bueno consultar con un nutricionista para un plan de alimentación saludable.")
        
    elif 18.5 <= imc < 25:
        print("Peso normal (Saludable)")
        print("🎉 ¡Excelente! Te encuentras en un rango óptimo. Mantén tus buenos hábitos.")
        
    elif 25 <= imc < 30:
        print("Sobrepeso")
        print("⚠️ Atención: Estás un poco por encima del rango ideal. Considera revisar tu dieta y hacer ejercicio.")
        
    else:
        print("Obesidad")
        print("🚨 Alerta: Tu salud podría estar en riesgo. Te recomendamos acudir a un profesional médico.")

except ZeroDivisionError:
    # Manejo de error por si el usuario introduce 0 en la estatura
    print("\n❌ Error: La estatura no puede ser 0 metros.")
    
except ValueError:
    # Manejo de error por si el usuario introduce texto en lugar de números
    print("\n❌ Error: Por favor, introduce solo valores numéricos válidos (usa el punto '.' para los decimales).")

print("\n--- Gracias por usar la calculadora ---")