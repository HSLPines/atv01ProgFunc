class GerenciadorDePacotes:
    def __init__(self):
        self.pacotes = {}

    def adicionar_pacote(self, codigo, cidade_destino, peso):
        if codigo in self.pacotes:
            raise ValueError("Código do pacote já existe.")
        self.pacotes[codigo] = (cidade_destino, peso)

    def remover_pacote(self, codigo):
        if codigo not in self.pacotes:
            raise ValueError("Código do pacote não encontrado.")
        del self.pacotes[codigo]

    def exibir_tres_pacotes_mais_pesados(self):
        pacotes_ordenados = sorted(self.pacotes.items(), key=lambda item: item[1][1], reverse=True)
        return pacotes_ordenados[:3]

    def calcular_peso_medio_por_cidade(self, cidade):
        pacotes_na_cidade = [peso for destino, peso in self.pacotes.values() if destino == cidade]
        if not pacotes_na_cidade:
            return 0
        return sum(pacotes_na_cidade) / len(pacotes_na_cidade)

    def listar_tres_cidades_com_mais_pacotes(self):
        from collections import Counter
        cidades = [destino for destino, _ in self.pacotes.values()]
        contagem_cidades = Counter(cidades)
        return contagem_cidades.most_common(3)