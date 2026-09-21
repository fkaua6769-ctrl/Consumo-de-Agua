Imóvel = input ("Informe o tipo de imóvel (casa, apartamento, comercial): ")
Consumo_agua = float (input ("Informe o consumo de água em metros cúbicos (m³): "))
if (Imóvel == "comercial"):
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif Imóvel == "apartamento" and Consumo_agua < 10:
    print("Consumo econômico – excelente controle de água!")
elif (Imóvel == "apartamento" or Imóvel == "casa") and Consumo_agua <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    