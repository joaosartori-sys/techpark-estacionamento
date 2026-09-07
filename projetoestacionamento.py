vagas_ocupadas = 0
capacidade_total = 10
estacionamento = {}
id_veiculo = 1

print("Bem-vindo ao Estacionamento TechPark!")

while True:
    print("""
Escolha uma operação:
1 - Entrada de Veículo
2 - Saída de Veículo
3 - Verificar Vagas Disponíveis
4 - Encerrar
""")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        if vagas_ocupadas >= capacidade_total:
            print("Estacionamento cheio!")
        else:
            hora_entrada = input("Digite a hora de entrada (ex: 14:30): ")
            estacionamento[id_veiculo] = hora_entrada
            vagas_ocupadas += 1
            print(f"Vaga registrada. Vagas disponíveis: {capacidade_total - vagas_ocupadas}")
            print(f"ID do veículo: {id_veiculo} | Entrada: {hora_entrada}")
            id_veiculo += 1

    elif opcao == "2":
        if vagas_ocupadas == 0:
            print("Estacionamento vazio! Nenhum veículo para sair.")
        else:
            try:
                id_saida = int(input("Informe o ID do veículo que está saindo: "))
                if id_saida in estacionamento:
                    entrada = estacionamento[id_saida]
                    saida = input("Digite a hora de saída (ex: 17:45): ")

                    h1, m1 = map(int, entrada.split(":"))
                    h2, m2 = map(int, saida.split(":"))
                    tempo_entrada = h1 * 60 + m1
                    tempo_saida = h2 * 60 + m2
                    tempo_total_min = max(0, tempo_saida - tempo_entrada)
                    horas = tempo_total_min // 60
                    if tempo_total_min % 60 != 0:
                        horas += 1

                    valor_a_pagar = horas * 10
                    print(f"Tempo total: {horas} hora(s)")
                    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

                    valor_pago = float(input("Informe o valor pago: R$ "))
                    if valor_pago >= valor_a_pagar:
                        troco = valor_pago - valor_a_pagar
                        print(f"Troco: R$ {troco:.2f}")
                        del estacionamento[id_saida]
                        vagas_ocupadas -= 1
                        print(f"Saída registrada. Vagas disponíveis: {capacidade_total - vagas_ocupadas}")
                    else:
                        print("Valor insuficiente. Operação cancelada.")
                else:
                    print("ID de veículo não encontrado.")
            except ValueError:
                print("Entrada inválida. Use apenas números.")

    elif opcao == "3":
        print(f"Vagas disponíveis: {capacidade_total - vagas_ocupadas}")

    elif opcao == "4":
        print("Encerrando o sistema. Obrigado por usar o TechPark!")
        break

    else:
        print("Opção inválida. Tente novamente.")