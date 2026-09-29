def simulador_investimentos():
    print("=" * 45)
    print("   SIMULADOR DE INVESTIMENTOS - B3 APRENDIZ   ")
    print("=" * 45)

    try:
        saldo_inicial = float(input("\nInforme o valor do aporte inicial (R$): "))
        meses = int(input("Informe o período de investimento (em meses): "))
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")
        return

    taxa_renda_fixa = 0.008  
    taxa_acoes = 0.012       

    rf = saldo_inicial * ((1 + taxa_renda_fixa) ** meses)
    variable = saldo_inicial * ((1 + taxa_acoes) ** meses)

    print("\n" + "-" * 45)
    print(f"Resultado após {meses} meses:")
    print(f"• Renda Fixa (CDB/Tesouro): R$ {rf:.2f}")
    print(f"• Mercado de Ações (Estimado): R$ {variable:.2f}")
    print("-" * 45)

if __name__ == "__main__":
    simulador_investimentos()