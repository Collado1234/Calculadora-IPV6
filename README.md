==============================================
 CALCULADORA DE ENDEREÇOS IPv6 – PYTHON 3.10.x
==============================================

Autor: Rennan Furlaneto Collado
Disciplina: Redes de Computadores I
Trabalho: IPv6 - Abreviação, Geração Aleatória e Formatação com Prefixo
Data: 26/06/2025

----------------------------------------------
1. REQUISITOS DO SISTEMA
----------------------------------------------
- Python versão 3.13.1
- Nenhuma biblioteca externa é utilizada
- Código dividido em dois arquivos principais:
    - ipv6.py → implementação da classe IPv6
    - main.py → script que roda o menu da calculadora

----------------------------------------------
2. ESTRUTURA DOS ARQUIVOS
----------------------------------------------

> ipv6.py

Contém a classe `IPv6`, com os seguintes métodos:

- `abreviar_ipv6(ipv6: str) -> str`: 
    Abrevia um endereço IPv6 expandido, removendo zeros à esquerda e substituindo a maior sequência de zeros contínuos por "::".

- `formatar_com_prefixo(endereco_com_prefixo: str) -> str`: 
    Recebe um IPv6 com notação CIDR (ex: /48) e retorna a versão abreviada com o prefixo correto.

- `gerar_ipv6_aleatorio(prefixo: int) -> str`: 
    Gera um endereço IPv6 aleatório com os bits de host zerados conforme o prefixo fornecido (48, 54 ou 64).

- `validar_ipv6(ipv6: str) -> bool`: 
    Verifica se um IPv6 expandido está no formato correto (8 blocos de 4 dígitos hexadecimais separados por dois-pontos).

- `_pseudo_random_int(min, max) -> int`: 
    Gera números pseudoaleatórios com base em um algoritmo linear congruente, sem uso da biblioteca `random`.

> main.py

Script com a função principal (`main()`) que apresenta um menu interativo com as opções:

1 - Abreviar endereço IPv6 expandido  
2 - Gerar IPv6 aleatório com prefixo /48  
3 - Gerar IPv6 aleatório com prefixo /54  
0 - Sair do programa

----------------------------------------------
3. COMO EXECUTAR O PROGRAMA
----------------------------------------------

1. Certifique-se de ter o Python 3.10.x instalado ao menos.

2. Salve os arquivos `ipv6.py` e `main.py` na mesma pasta.

3. No terminal, acesse a pasta onde estão os arquivos.

4. Execute o programa com o comando:
   > python main.py

----------------------------------------------
4. OBSERVAÇÕES
----------------------------------------------
- O código está totalmente comentado, explicando cada função, classe e estrutura lógica.
- Não foi utilizada nenhuma biblioteca externa, conforme as exigências do trabalho.
- O endereço IPv6 gerado segue as normas das RFCs 4291 (endereçamento) e 5952 (abreviação).

----------------------------------------------
5. EXEMPLOS DE USO
----------------------------------------------

Entrada:
    2801:0390:0080:0000:0100:0000:0000:ff00/64

Saída:
    2801:390:80:0:100::ff00/64

Geração aleatória (exemplo):
    e82a:d61b:93b8::/48  → válido e conforme a RFC

----------------------------------------------
6. CONTATO
----------------------------------------------
Dúvidas ou sugestões podem ser encaminhadas ao autor diretamente.
