def calcular_proporcao_cn(cn_a, cn_b, cn_desejado, fluxo_total):


    # Definição da equação
    # (C_A * X_A + C_B * X_B) / (N_A * X_A + N_B * X_B) = C/N_desejado
    # Sendo que: C_A/N_A = cn_a e C_B/N_B = cn_b

    # Equação derivada:
    # (cn_a - cn_desejado) * X_A = (cn_desejado - cn_b) * X_B
    # e X_A + X_B = fluxo_total

    # Verificação se os CNs são válidos
    if cn_a == cn_b:
        raise ValueError("A relações C/N dos dois resíduos não pode ser igual.")

    # Cálculo da proporção entre X_A e X_B
    proporcao = (cn_desejado - cn_b) / (cn_a - cn_desejado)

    if proporcao < 0:
        raise ValueError("C/N desejado deve estar entre os C/N dos resíduos.")

    # Calcular massas dos dois resíduos
    massa_b = fluxo_total / (1 + proporcao)
    massa_a = fluxo_total - massa_b

    return massa_a, massa_b


# Dados de entrada
cn_residuo_a = 44
cn_residuo_b = 5.8
cn_desejado = 25      # C/N alvo
fluxo_total = 1000    # kg/h

# Cálculo
massa_a, massa_b = calcular_proporcao_cn(cn_residuo_a, cn_residuo_b, cn_desejado, fluxo_total)

# Resultado
print(f"Para um fluxo total de {fluxo_total} kg/h e C/N = {cn_desejado}:")
print(f" - Resíduo A (C/N={cn_residuo_a}): {massa_a:.2f} kg/h")
print(f" - Resíduo B (C/N={cn_residuo_b}): {massa_b:.2f} kg/h")
