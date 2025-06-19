from ipv6 import IPv6  # importa a classe do módulo ipv6.py

def main():
    """
    Função principal da calculadora IPv6.
    Apresenta um menu de opções para o usuário:
    - Abreviar um IPv6
    - Gerar IPv6 aleatório com /48 ou /54
    - Sair
    """
    print("=== CALCULADORA IPv6 ===")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Abreviar endereço IPv6")
        print("2 - Gerar IPv6 aleatório /48")
        print("3 - Gerar IPv6 aleatório /54")
        #print("4 - Executar testes4")
        print("0 - Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            endereco = input("Digite o IPv6 expandido (ex: 2801:0390:0080:0000:0100:0000:0000:ff00): ").strip()
            if IPv6.validar_ipv6(endereco):
                abreviado = IPv6.abreviar_ipv6(endereco)
                print(f"IPv6 abreviado: {abreviado}")
            else:
                print("IPv6 inválido. Verifique o formato.")

        elif opcao == "2":
            ipv6_aleatorio = IPv6.gerar_ipv6_aleatorio(prefixo=48)
            print(f"IPv6 aleatório /48: {IPv6.formatar_com_prefixo(ipv6_aleatorio)}")

        elif opcao == "3":
            ipv6_aleatorio = IPv6.gerar_ipv6_aleatorio(prefixo=54)
            print(f"IPv6 aleatório /54: {IPv6.formatar_com_prefixo(ipv6_aleatorio)}")

        # elif opcao == "4":
        #     print("Iniciando testes...")
        #     executar_todos_os_testes()
        #     print("Todos os testes foram executados com sucesso!")

        elif opcao == "0":
            print("Encerrando a calculadora.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Proteção para execução direta
if __name__ == "__main__":
    main()
