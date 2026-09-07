from reconhecedores import reconhece

def executar_testes():
    testes_falharam = 0

    
    casos_de_teste = [
        # minilangCore
        ("INT_LITERAL", "0", True, "Menor palavra válida aceita"),
        ("INT_LITERAL", "007", True, "Zeros à esquerda são permitidos"),
        ("INT_LITERAL", "", False, "Fronteira: string vazia deve ser rejeitada"),
        
        ("IDENT_BASE", "total2", True, "Começa com letra e possui número"),
        ("IDENT_BASE", "_valor", True, "Começa com sublinhado"),
        ("IDENT_BASE", "2total", False, "Fronteira: não pode começar com número"),
        
        ("LINE_COMMENT", "// ok", True, "Comentário válido com espaço"),
        ("LINE_COMMENT", "/ ok", False, "Comentário inválido sem duas barras"),


        # conflito e interseção
        ("ASSIGN", "==", False, "Conflito: '==' pertence a REL_OP, não a ASSIGN"),
        ("REL_OP", "==", True, "'==' é um operador relacional válido"),
        ("REL_OP", "=", False, "Conflito: '=' pertence a ASSIGN, não a REL_OP"),

        ("ARITH_OP", "-10", False, "Conflito: lexer deve separar operador e número, falha no fullmatch"),
        ("INT_LITERAL", "-10", False, "Conflito: '-' não faz parte de INT_LITERAL isoladamente"),
        
        ("ARITH_OP", "//", False, "Conflito: '//' sobrepõe divisão simples, deve ser LINE_COMMENT"),
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