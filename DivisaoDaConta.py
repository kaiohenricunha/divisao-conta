def valorTotal(taxa, conta, numeroPessoas):
    if taxa < 0 or taxa > 100:
        return print("Valor inválido!")
    else:
        taxa = taxa / 100  #transforma a porcentagem num número décimal(mais fácil de utilizar)

    contaTotal = conta + conta * taxa
    contaTotalissima = str(contaTotal)
    contaIndividual = contaTotal / numeroPessoas
    contaIndividualissima = str(contaIndividual)

    print(f"O valor total da conta, com a taxa de serviço, será de R$ {contaTotalissima.replace('.', ',')}")
    return print(f"Dividindo a conta por {numeroPessoas} pessoa(s), cada pessoa deverá pagar R$ {contaIndividualissima.replace('.',',')}")

valorTotal(3, 100, 10)



