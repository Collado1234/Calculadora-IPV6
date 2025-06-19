import re

class IPv6:
    """
    Classe para manipulação de endereços IPv6.
    Inclui métodos para abreviar, validar e gerar endereços IPv6 aleatórios.
    """

    _seed = 123456789

    @staticmethod
    def _pseudo_random_int(min_value: int, max_value: int) -> int:  #metodo auxiliar para gerar números pseudo-aleatórios
        IPv6._seed = (1103515245 * IPv6._seed + 12345) % (2**31) # gera um novo valor de semente
        return min_value + (IPv6._seed % (max_value - min_value + 1))

    def __init__(self):
        pass

    @staticmethod
    def abreviar_ipv6(ipv6: str) -> str:
        """
        Abrevia um endereço IPv6 expandido conforme RFC 5952.
        """
        partes = ipv6.split(':')

        # Remove zeros à esquerda
        partes = [parte.lstrip('0') or '0' for parte in partes]

        # Localiza maior sequência de blocos '0'
        max_len = 0
        max_start = -1
        i = 0

        while i < len(partes): # percorre as partes do IPv6
            if partes[i] == '0':
                start = i
                while i < len(partes) and partes[i] == '0':
                    i += 1
                length = i - start
                if length > max_len:
                    max_len = length
                    max_start = start
            else:
                i += 1

        # Substitui maior sequência de '0' por ''
        if max_len > 1:
            partes = partes[:max_start] + [''] + partes[max_start + max_len:]
            # Adiciona vazio extra no início ou fim, se necessário
            if max_start == 0:
                partes = [''] + partes
            if max_start + max_len == 8:
                partes += ['']

        resultado = ':'.join(partes)

        # Garante que apenas '::' apareça, e não ':::'
        return resultado.replace(':::', '::')

    @staticmethod
    def formatar_com_prefixo(endereco_com_prefixo: str) -> str:
        """
        Recebe um endereço IPv6 com prefixo, aplica a abreviação e retorna o resultado como string.
        Exemplo de entrada: '2801:0390:0080:0000:0100:0000:0000:ff00/64'
        Retorna: '2801:390:80:0:100::ff00/64'
        """
        if '/' not in endereco_com_prefixo:
            raise ValueError("Endereço deve conter um prefixo (ex: /48, /54, /64).")

        endereco, barra_prefixo = endereco_com_prefixo.strip().split('/')
        prefixo = int(barra_prefixo)

        if prefixo not in (48, 54, 64):
            raise ValueError("Prefixo inválido. Os valores aceitos são: 48, 54 ou 64.")

        abreviado = IPv6.abreviar_ipv6(endereco)
        return f"{abreviado}/{prefixo}"
    
    @staticmethod
    def gerar_ipv6_aleatorio(prefixo: int = 48) -> str:
        """
        Gera um endereço IPv6 aleatório com o prefixo indicado (/48, /54 ou /64).
        Os bits após o prefixo são zerados.
        Retorna a string formatada com prefixo, por ex: '2001:db8:abcd::/48'
        """
        if prefixo not in (48, 54, 64):
            raise ValueError("Prefixo inválido. Use 48, 54 ou 64.")

        # Gera 8 blocos de 16 bits (0 a 0xFFFF)
        blocos = [IPv6._pseudo_random_int(0, 0xFFFF) for _ in range(8)]

        # Converte para binário string
        binario = ''.join(f'{b:016b}' for b in blocos)

        # Zera os bits após o prefixo
        bits_zerar = 128 - prefixo
        binario = binario[:prefixo] + '0' * bits_zerar

        # Reparte em blocos de 16 bits e converte para inteiros
        blocos = [int(binario[i:i+16], 2) for i in range(0, 128, 16)]

        # Converte para string hexadecimal com 4 dígitos (com zeros à esquerda)
        endereco = ':'.join(f'{b:x}' for b in blocos)

        return f"{endereco}/{prefixo}"
    
    @staticmethod
    def validar_ipv6(ipv6: str) -> bool:
        """
        Valida se o IPv6 informado está no formato expandido correto.
        """
        # Regex para validar grupos hexadecimais separados por ':', total 8 grupos
        pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
        return bool(pattern.match(ipv6))