from reconhecedores import reconhece

def executar_testes():
    testes_falharam = 0

    casos_de_teste = [

        ("IDENT_BASE", "total2", True, "Comum: começa com letra e possui número"),
        ("IDENT_BASE", "_valor", True, "Comum: começa com sublinhado"),

        ("IDENT_BASE", "2total", False, "Comum: rejeitado, começa com número"),
        ("IDENT_BASE", "tot-al", False, "Comum: rejeitado, IDENT_BASE não permite hífen"),

        ("IDENT_BASE", "X", True, "Fronteira: identificador válido com uma única letra"),
        ("IDENT_BASE", "_", True, "Fronteira: underscore sozinho é um identificador válido"),



        ("INT_LITERAL", "123", True, "Comum: literal com múltiplos dígitos"),
        ("INT_LITERAL", "4", True, "Comum: literal de um único dígito"),

        ("INT_LITERAL", "A12", False, "Comum: rejeitado, começa com letra"),
        ("INT_LITERAL", "0.5", False, "Comum: rejeitado, não é inteiro"),

        ("INT_LITERAL", "0", True, "Fronteira: menor inteiro válido"),
        ("INT_LITERAL", "007", True, "Fronteira: zeros à esquerda são permitidos"),



        ("KEYWORD_CORE", "int", True, "Comum: palavra-chave válida"),
        ("KEYWORD_CORE", "print", True, "Comum: palavra-chave válida"),

        ("KEYWORD_CORE", "Int", False, "Comum: rejeitado, case-sensitive"),
        ("KEYWORD_CORE", "printf", False, "Comum: rejeitado, não é palavra-chave exata"),

        ("KEYWORD_CORE", "printer", False, "Fronteira: rejeitado, não é palavra-chave exata"),
        ("KEYWORD_CORE", "int2", False, "Fronteira: rejeitado, não é palavra-chave exata"),



        ("ARITH_OP", "+", True, "Comum: operador aritmético válido"),
        ("ARITH_OP", "-", True, "Comum: operador aritmético válido"),

        ("ARITH_OP", "%", False, "Comum: rejeitado, não é operador aritmético válido"),
        ("ARITH_OP", "++", False, "Comum: rejeitado, não é operador aritmético válido"),

        ("ARITH_OP", "a+-b", False, "Fronteira: rejeitado, string mista não é um único token"),
        ("ARITH_OP", "//", False, "Fronteira: prefixo de LINE_COMMENT, não pertence a ARITH_OP"),



        ("ASSIGN", "=", True, "Comum: único operador de atribuição válido (não há 2º aceito possível)"),

        ("ASSIGN", "==", False, "Comum: rejeitado, não é operador de atribuição válido"),
        ("ASSIGN", ":=", False, "Comum: rejeitado, não é operador de atribuição válido"),

        ("ASSIGN", "x==y", False, "Fronteira: rejeitado, string mista não é um único token"),
        ("ASSIGN", "+=", False, "Fronteira: rejeitado, não é operador de atribuição válido"),



        ("DELIMITER_CORE", "(", True, "Comum: delimitador válido"),
        ("DELIMITER_CORE", ")", True, "Comum: delimitador válido"),

        ("DELIMITER_CORE", "{", False, "Comum: rejeitado, pertence a BLOCK_DELIMITER, não a DELIMITER_CORE"),
        ("DELIMITER_CORE", "[", False, "Comum: rejeitado, colchete não pertence ao alfabeto da classe"),

        ("DELIMITER_CORE", "()", False, "Fronteira: rejeitado, deve ser dois tokens separados"),
        ("DELIMITER_CORE", "[]", False, "Fronteira: rejeitado, nenhum dos símbolos pertence à classe"),



        ("LINE_COMMENT", "//comentário", True, "Comum: comentário válido sem espaço"),
        ("LINE_COMMENT", "// ok", True, "Comum: comentário válido com espaço"),

        ("LINE_COMMENT", "/ab", False, "Comum: rejeitado, apenas uma barra"),
        ("LINE_COMMENT", "abc", False, "Comum: rejeitado, não começa com //"),

        ("LINE_COMMENT", "//", True, "Fronteira: menor comentário válido, sem conteúdo após as barras"),
        ("LINE_COMMENT", "// abc\ndef", False, "Fronteira: comentário termina no \\n, 'def' pertence a outro lexema"),



        ("WHITESPACE", " ", True, "Comum: espaço em branco válido"),
        ("WHITESPACE", "\t\t", True, "Comum: tabulação repetida válida"),

        ("WHITESPACE", "_", False, "Comum: underscore não pertence à classe WHITESPACE"),
        ("WHITESPACE", "abc", False, "Comum: letras não pertencem à classe WHITESPACE"),

        ("WHITESPACE", "\n", True, "Fronteira: menor sequência válida usando quebra de linha"),
        ("WHITESPACE", "", False, "Fronteira: vazio não satisfaz B+ (exige ao menos um símbolo)"),



        ("KEYWORD_EXT", "if", True, "Comum: palavra-chave válida"),
        ("KEYWORD_EXT", "while", True, "Comum: palavra-chave válida"),

        ("KEYWORD_EXT", "elseif", False, "Comum: rejeitado, não é palavra-chave exata"),
        ("KEYWORD_EXT", "while1", False, "Comum: rejeitado, não é palavra-chave exata"),

        ("KEYWORD_EXT", "ifelse", False, "Fronteira: rejeitado, não é palavra-chave exata"),
        ("KEYWORD_EXT", "returnValue", False, "Fronteira: seria IDENT_BASE, não KEYWORD_EXT"),


     
        ("REL_OP", "==", True, "Comum: operador relacional válido"),
        ("REL_OP", "!=", True, "Comum: operador relacional válido"),

        ("REL_OP", "=>", False, "Comum: ordem invertida, não corresponde a nenhum operador da linguagem"),
        ("REL_OP", "<>", False, "Comum: combinação inválida, não pertence à linguagem"),

        ("REL_OP", "=", False, "Fronteira: pertence à classe ASSIGN, não a REL_OP"),
        ("REL_OP", "", False, "Fronteira: vazio não satisfaz a regex de REL_OP"),



        ("BLOCK_DELIMITER", "{", True, "Comum: delimitador de bloco válido"),
        ("BLOCK_DELIMITER", "}", True, "Comum: delimitador de bloco válido"),

        ("BLOCK_DELIMITER", "[", False, "Comum: rejeitado, não é delimitador de bloco válido"),
        ("BLOCK_DELIMITER", "]", False, "Comum: rejeitado, não é delimitador de bloco válido"),

        ("BLOCK_DELIMITER", "{}", False, "Fronteira: deve ser dois tokens separados, não um único token"),
        ("BLOCK_DELIMITER", "", False, "Fronteira: linguagem não contém a palavra vazia"),
    ]

    for classe, palavra, esperado, motivo in casos_de_teste:
        resultado = reconhece(classe, palavra)

        if resultado == esperado:
            print(f"[PASSOU] {classe} -> '{palavra}'")
        else:
            print(f"[FALHOU] {classe} -> '{palavra}'")
            print(f"         Motivo: {motivo}")
            print(f"         Esperado: {esperado} | Obtido: {resultado}\n")
            testes_falharam += 1

    print("--------------------------------------------------------------------------------------------------------")
    if testes_falharam == 0:
        print("\nSUCESSO! Todos os casos de teste passaram perfeitamente.")
    else:
        print(f"\nATENÇÃO: {testes_falharam} teste(s) falhou/falharam. Verifique os logs.")


if __name__ == "__main__":
    executar_testes()