import sys
import os

def executar_pybr(arquivo_pybr: str):
    if not os.path.isabs(arquivo_pybr):
        arquivo_pybr = os.path.abspath(arquivo_pybr)

    with open(arquivo_pybr, 'r', encoding='utf-8') as f:
        codigo = f.read()

    # Substituições das palavras-chave
    substituicoes = {
        "definir ": "def ",
        "retornar": "return",
        "escrever": "print",
        "receber": "input",
        "inteiro": "int",
        "texto": "str",
        "tese": "bool",
        "funcao": "Callable",
        "decimal": "float",
        "lista": "list",
        "dicionario": "dict",
        "nao": "not",
        "uniao": "Union",
        "tupla": "Tuple",
        "qualquer": "Any",
        "se ": "if ",
        "senao": "else",
        "em": "in",
        "enquanto ": "while ",
        "para": "for",
        "tentar ": "try ",
        "exceto ": "except ",
        "importar": "import",
        " como ": " as ",
        "chave": "get",
        ".adicionar": ".append",
        ".remover": ".remove",
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
        "global": "globals()",
        "quebrar": "break",
        "continuar": "continue",
        "self": "instancia",
        "atributo ": "self.",
        "de ": "from ",
        
    }

    # Realiza as substituições
    for chave, valor in substituicoes.items():
        codigo = codigo.replace(f" {chave} ", f" {valor} ")
        codigo = codigo.replace(f"\n{chave} ", f"\n{valor} ")
        codigo = codigo.replace(f"{chave}\n", f"{valor}\n")
        codigo = codigo.replace(f"({chave} ", f"({valor} ")
        codigo = codigo.replace(f" {chave})", f" {valor})")
        codigo = codigo.replace(f"{chave}(", f"{valor}(")
        codigo = codigo.replace(f" {chave}.", f" {valor}.")
        
    # Certificação de substituições problemáticas
    codigo = codigo.replace("senao", "else")
    codigo = codigo.replace("definir ", "def ")
    codigo = codigo.replace("importar ", "import ")
    codigo = codigo.replace("se ", "if ")
    codigo = codigo.replace("enquanto ", "while ")

    # Executa o código
    try:
        exec(codigo, globals())
    except SyntaxError as e:
        print(f"Erro de sintaxe no código: {e}")
        print("Código após substituições:")
        print(codigo)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python compilador.py <nome do arquivo>")
    else:
        executar_pybr(sys.argv[1])
