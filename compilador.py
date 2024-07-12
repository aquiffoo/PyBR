import sys

def executar_pybr(arquivo_pybr: str):
    with open(arquivo_pybr, 'r', encoding='utf-8') as f:
        codigo = f.read()

    # Substituições das palavras-chave
    substituicoes = {
        "definir": "def",
        "retornar": "return",
        "escrever": "print",
        "receber": "input",
        "inteiro": "int",
        "texto": "str",
        "tese": "bool",
        "funcao": "Callable",
        "decimal": "float",
        "lista": "List",
        "dicionario": "Dict",
        "uniao": "Union",
        "tupla": "Tuple",
        "qualquer": "Any",
        "se": "if",
        "enquanto": "while",
        "para": "for",
        "tentar": "try",
        "exceto": "except",
        "importar": "import",
        "como": "as",
        "chave": "get",
        "adicionar": "append",
        "remover": "remove",
        "encontrar": "next",
        "maiusculo": "upper",
        "minusculo": "lower",
        "dividir": "split",
        "juntar": "join",
        "raiz_quadrada": "math.sqrt",
        "ler_arquivo": "open",
        "escrever_arquivo": "open",
        "adicionar_arquivo": "open",
        "com_retorno": "return",
        "global": "globals()"
    }

    # Realiza as substituições
    for chave, valor in substituicoes.items():
        codigo = codigo.replace(chave, valor)

    # Executa o código
    exec(codigo, globals())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python compilador.py <arquivo.pybr>")
    else:
        executar_pybr(sys.argv[1])
