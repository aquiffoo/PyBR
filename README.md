# PyBR

## Sobre

**PyBR** é um compilador do Python para a língua portuguesa, desenvolvido para facilitar o aprendizado e a programação em Python usando uma sintaxe mais acessível para falantes de português. Este projeto é destinado a usuários do Windows.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/PyBR.git
   ```

2. **Adicione a pasta do projeto ao seu PATH:**

   Coloque a pasta `C:\Compilador_PyBR` no seu PATH do sistema para facilitar a execução dos comandos.

## Estrutura do Projeto

```
C:\Compilador_PyBR\
│
├── compilador.py       # Script principal do compilador
└── py_executar.bat     # Script para executar arquivos .pybr
```

## Sintaxe

A sintaxe do PyBR utiliza palavras em português para substituir palavras-chave do Python. Veja alguns exemplos:

| Português     | Python      |
|---------------|-------------|
| definir       | def         |
| retornar      | return      |
| escrever      | print       |
| receber       | input       |
| inteiro       | int         |
| texto         | str         |
| tese          | bool        |
| funcao        | Callable    |
| decimal       | float       |
| lista         | List        |
| dicionario    | Dict        |
| uniao         | Union       |
| tupla         | Tuple       |
| qualquer      | Any         |
| se            | if          |
| enquanto      | while       |
| para          | for         |
| tentar        | try         |
| exceto        | except      |
| importar      | import      |
| como          | as          |
| chave         | get         |
| adicionar     | append      |
| remover       | remove      |
| encontrar     | next        |
| maiusculo     | upper       |
| minusculo     | lower       |
| dividir       | split       |
| juntar        | join        |
| raiz_quadrada | math.sqrt   |
| ler_arquivo   | open        |
| escrever_arquivo | open     |
| adicionar_arquivo | open    |
| com_retorno   | return      |
| global        | globals()   |
| senão         | else        |

## Exemplo de Uso

Aqui está um exemplo de um arquivo `ola.pybr` que demonstra o uso da sintaxe do PyBR:

```python
definir ola(pessoa):
    retornar f"Olá, {pessoa}!"

nome = receber("Qual é o teu nome? ")
escrever(ola(nome))
```

### Executando o Exemplo

1. **Crie o arquivo `ola.pybr`:**

   Salve o código acima em um arquivo chamado `ola.pybr`.

2. **Execute o arquivo usando o comando:**

   ```bash
   py_executar ola
   ```

3. **Interaja com o programa**, fornecendo seu nome quando solicitado.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o projeto.
