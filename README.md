**UNIMAR**  
**CIÊNCIA DA COMPUTAÇÃO**

Leonardo Perin Andreozi \- 1995746
Noah Vêri de Morais Franco \- 2014803  
Gustavo Rosa de Jesus \- 2012734  
Joaquim Pedro Augusto de Oliveira \- 1993926

**PROJETO DE COMPILADORES E LINGUAGENS FORMAIS E AUTÔMATOS**

Marília  
04/09/2026

## Tabela geral das classes

| Classe | Finalidade |
|---|---|
| `KEYWORD_CORE` | Palavras-chave principais da linguagem |
| `IDENT_BASE` | Identificadores básicos |
| `INT_LITERAL` | Literais inteiros |
| `ASSIGN` | Operador de atribuição |
| `ARITH_OP` | Operadores aritméticos |
| `DELIMITER_CORE` | Delimitadores básicos |
| `LINE_COMMENT` | Comentários de linha |
| `WHITESPACE` | Espaços em branco |
| `KEYWORD_EXT` | Palavras-chave de extensão |
| `REL_OP` | Operadores relacionais |
| `BLOCK_DELIMITER` | Delimitadores de bloco |


# Tabela 1 — IDENT\_BASE

| Classe 1 |  |
| :---- | :---- |
| **Nome da classe** | IDENT\_BASE |
| **Descrição** | Conjunto de regras que dita o quê pode ser classificado como identificador aceito, nesse caso deve começar com uma letra ou underscore seguida de letras,dígitos ou underscore |
| **Exemplos aceitos** | {x, total, total2, \_aux, contador\_1, int,, \_, IdentGrande}  |
| **Definição Matemática** | LIdentBase \= { c₀c₁...cₙ | c₀ ∈ (Letra ∪ {*}), cᵢ ∈ (Letra ∪ Dígito ∪ {*}) para 1 ≤ i ≤ n, n ≥ 0 }  |
| **Conjuntos Auxiliares** | Letra \= {a, ..., z, A, ..., Z} Dígito \= {0, ..., 9} Underscore \= {\_}  |
| **Expressão Regular Formal** | rIdentBase \= (Letra ∪ \_)(Letra ∪ Dígito ∪ \_)\* L(rIdentBase) \= LIdentBase  |
| **Regex Python** | r"\[A-Za-z\_\]\[A-Za-z0-9\_\]\*"  |
| **Ação Futura** | reclassificar, se a palavra reconhecida coincidir com KEYWORD\_CORE ou KEYWORD\_EXT, emitir o token da palavra reservada; caso contrário, emitir IDENT\_BASE. |
| **Testes aceitos** | total2(letra inicial \+ letras e dígito no meio), \_valor  (começa com sublinhado) |
| **Testes Rejeitados** | 2total(começa com dígito), tot-al (hífen não é aceito) |
| **Testes Fronteira** | X(menor identificador possível (1 caractere)), \_(underscore sozinho é válido ) |

# Tabela 2 — INT\_LITERAL

| Classe 2 |  |
| :---- | :---- |
| **Nome da classe** | INT\_LITERAL |
| **Descrição** | Classe responsável por lidar com inteiros literais, não aceita números flutuantes(exemplo 0.1)|
| **Exemplos aceitos** | 0, 001, 2s, 34,9 |
| **Definição Matemática** | Dígito \= {0, 1, 2, ..., 9}  LIntLiteral \= { s | s \= d₁d₂...dₙ, dᵢ ∈ Dígito para todo i, n ≥ 1 }  |
| **Conjuntos Auxiliares** | Dígito \= {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  |
| **Expressão Regular Formal** | LIntLiteral \= { s | s \= d₁...dₙ, dᵢ ∈ Dígito, n ≥ 1 }  |
| **Regex Python** | rIntLiteral \= \[0-9\]⁺  |
| **Ação Futura** | emitir token INT\_LITERAL, essa classe não lida com sinal de \+/-, é tokenizado separadamente como ARITH\_OP |
| **Testes aceitos** | 123, 4 |
| **Testes Rejeitados** | A12, 0.5 |
| **Testes Fronteira** | 0(menor literal válido), 007 (testa a regras dos zeros a esquerda) |

# Tabela 3 — KEYWORD\_CORE

| Classe 3 | KEYWORD\_CORE  |
| :---- | :---- |
| **Nome da classe** | KEYWORD\_CORE  |
| **Descrição** | Conjunto finito e fixo de palavras reservadas "nucleares" da MiniLang. São strings que, mesmo casando com o padrão de IDENT\_BASE, precisam ser reconhecidas como token à parte, com prioridade sobre identificador.  |
| **Exemplos aceitos** |  int, print  |
| **Definição Matemática** | RCore \= {"int", "print"}  |
| **Conjuntos Auxiliares** | Nenhum  RCore é definida por enumeração direta (união de literais fixos), não depende de Letra/Dígito  |
| **Expressão Regular Formal** | rKeywordCore \= "int" | "print"  |
| **Regex Python** |  \`r'int  |
| **Ação futura** | Emitir token KEYWORD\_CORE com o lexema exato reconhecido; essa regra tem **prioridade sobre IDENT\_BASE** (mesma string "int" nunca deve virar IDENT\_BASE)  |
| **Testes aceitos** | int (palavra-chave válida); print (palavra-chave válida)  |
| **Testes Rejeitados** | Int (case-sensitive); printf (não é palavra-chave exata)  |
| **Testes Fronteira** | printer (rejeitado  não é palavra-chave exata); int2 (rejeitado não é palavra-chave exata)  |

# Tabela 4 — ARITH\_OP

| Classe 4 | ARITH\_OP  |
| :---- | :---- |
| **Nome da classe** | ARITH\_OP  |
| **Descrição** | Operadores aritméticos binários de 1 caractere: soma, subtração, multiplicação, divisão. Classe enumerável  mesmo padrão de resolução de ASSIGN, só muda o conjunto de símbolos.  |
| **Exemplos aceitos** | \+, \-, \*, /   |
| **Definição Matemática** | RArith \= { "+", "-", "\*", "/" }   |
| **Conjuntos Auxiliares** | Nenhum  enumeração direta de símbolos  |
| **Expressão Regular Formal** | rArithOp \= "+" | "-" | "\*" | "/"  |
| **Regex Python** | r”\[-+\*/\]”  |
| **Ação da Futura** | Emitir o token específico do símbolo casado (PLUS, MINUS, TIMES, DIV)  cada caractere gera exatamente um token, sem lookahead necessário (assumindo que a MiniLang não tem \++, \--, \*\* nem comentários de bloco /\* \*/ que comecem com /)  |
| **Testes aceitos** | \+ (operador aritmético válido); \- (operador aritmético válido)  |
| **Testes Rejeitados** | % (não é operador aritmético válido); \++ (não é operador aritmético válido)  |
| **Testes Fronteira** | a+-b (rejeitado — string mista não é um único token); // (rejeitado  prefixo de LINE\_COMMENT, não pertence a ARITH\_OP)  |

# Tabela 5 — ASSIGN

| Classe 5 | ASSIGN  |
| :---- | :---- |
| **Nome da classe** | ASSIGN  |
| **Descrição** | Símbolo de atribuição: associa o valor de uma expressão a uma variável. Classe enumerável de 1 símbolo (assumindo que a MiniLang não tem atribuições compostas como `+=`; se tiver, ver nota de fronteira abaixo).  |
| **Exemplos aceitos** | \=  |
| **Definição Matemática** | RAssign \= { "=" }  |
| **Conjuntos Auxiliares** | Nenhum —enumeração direta de símbolo  |
| **Expressão Regular Formal** | rAssign \= "="  |
| **Regex Python** | r'='  |
| **Ação Futura** | Emitir token ASSIGN; o lexer deve garantir que `=` sozinho **não seja confundido** com o primeiro caractere de `==` (ver nota de fronteira) — se REL\_OP incluir `==`, ASSIGN precisa de regra de precedência/maximal munch  |
| **Testes aceitos** | \= (único operador de atribuição válido — não há 2º aceito possível)   |
| **Testes Rejeitados** | \== (não é operador de atribuição válido); := (não é operador de atribuição válido)  |
| **Testes Fronteira** | x==y (rejeitado — string mista não é um único token); \+= (rejeitado  não é operador de atribuição válido)   |

# Tabela 6 — DELIMITER\_CORE

| Classe 6 | DELIMITER\_CORE  |
| :---- | :---- |
| **Nome da classe** | DELIMITER\_CORE  |
| **Descrição** | Símbolos de pontuação de uso geral: separam argumentos, agrupam expressões e marcam fim de instrução. Não definem blocos de código (isso é BLOCK\_DELIMITER). Cada símbolo é um token de 1 caractere, sem combinação possível entre eles.  |
| **Exemplos aceitos** | ( , ) ;  |
| **Definição Matemática** | RDelimCore \= { "(", ")", ";" }  |
| **Conjuntos Auxiliares** | Nenhum  enumeração direta de símbolos  |
| **Expressão Regular Formal** | rDelimCore \= "(" | ")" | ";"  |
| **Regex Python** | r'\[();\]'  |
| **Ação Futura** | Emitir o token específico do símbolo casado (LPAREN, RPAREN, COMMA, SEMI)  cada caractere gera exatamente um token, sem lookahead necessário  |
| **Testes aceitos** | ( (delimitador válido); ) (delimitador válido)  |
| **Testes Rejeitados** | { (pertence a BLOCK\_DELIMITER, não a DELIMITER\_CORE); \[ (colchete não pertence ao alfabeto da classe)  |
| **Testes Fronteira** | () (rejeitado  deve ser dois tokens separados, não um único token); \[\] (rejeitado —nenhum dos símbolos pertence à classe)  |

# Tabela 7 — LINE\_COMMENT

| Classe 7 | LINE\_COMMENT  |
| :---- | :---- |
| **Nome da classe** | LINE\_COMMENT  |
| **Descrição** | Sequência que começa com `//` e se estende até (mas não incluindo) o próximo caractere de nova linha. Usada para anotações que o compilador deve ignorar na análise sintática.  |
| **Exemplos aceitos** | `// comentario`, `//`, `//x=1`  |
| **Definição Matemática** | Seja NL \= {'\\n'} e Σ' \= ΣFonte − NL. LineComment \= { "//" · x | x ∈ Σ'\* }  |
| **Conjuntos Auxiliares** | Σ' \= ΣFonte − {'\\n'} (qualquer caractere da fonte, exceto quebra de linha)  |
| **Expressão Regular Formal** | rLineComment \= "//" · (Σ')\*  |
| **Regex Python** | r"//\[^\\r\\n\]\*"  |
| **Ação futura** | **Não emitir token** para o parser  comentário é descartado no lexer (skip), assim como WHITESPACE  |
| **Testes aceitos** | //comentário (comentário válido sem espaço); // ok (comentário válido com espaço)  |
| **Testes Rejeitados** | /ab (apenas uma barra); abc (não começa com //)   |
| **Testes Fronteira** | // (aceito — menor comentário válido, sem conteúdo após as barras); "// abc\\ndef" (rejeitado como token único — comentário termina no \\n, "def" pertence a outro lexema)  |

# Tabela 8 — WHITESPACE

| Classe 8 |  |
| :---- | :---- |
| **Nome da classe** | WHITESPACE |
| **Descrição** | Caracteres de espaçamento invisíveis usados para separar os demais tokens no código  |
| **Exemplos aceitos** | ‘ ‘(espaço) \\t, \\n, \\r |
| **Definição Matemática** | L\_Espaco \= B⁺  |
| **Conjuntos Auxiliares** | B \= {ESP, TAB, CR, NL}  |
| **Expressão Regular Formal** | r\_Espaco \= B⁺  L(r\_Espaco) \= L\_Espaco  |
| **Regex Python** | r"\[ \\t\\r\\n\]+"  |
| **Ação futura** | Ignorar não é enviado ao parser; serve apenas para delimitar os demais tokens.  |
| **Testes aceitos** | \\n (quebra de linha pertence a B ) \\t\\t (uma ou mais ocorrências, mesmo símbolo repetido) |
| **Testes Rejeitados** | \_(underscore não pertence a B) ‘’ (vazio não satisfaz, exige símbolo) |
| **Testes Fronteira** | ‘ ‘ (espaço, menor sequência válida) ‘’(B⁺ exige ao menos um símbolo; vazio não satisfaz ) |


# Tabela 9 — KEYWORD\_EXT

| Classe 9 | KEYWORD\_EXT  |
| :---- | :---- |
| **Nome da classe** | KEYWORD\_EXT  |
| **Descrição** | Conjunto finito de palavras reservadas "estendidas": controlam fluxo de execução (condicionais, laços, retorno), em vez de declarar tipo/E-S como em KEYWORD\_CORE. Mesmo mecanismo de reconhecimento de KEYWORD\_CORE, só muda o conjunto enumerado.  |
| **Exemplos aceitos** | if, else, while  |
| **Definição Matemática** | RExt \= { "if", "else", "while" }  |
| **Conjuntos Auxiliares** | Nenhum enumeração direta, igual a KEYWORD\_CORE  |
| **Expressão Regular Formal** | rKeywordExt \= "if" | "else" | "while" | "return"  |
| **Regex Python** | \`r'if  |
| **Ação Futura** | Emitir token KEYWORD\_EXT com o lexema exato; prioridade sobre IDENT\_BASE, igual KEYWORD\_CORE. Na prática, RCore ∪ RExt formam a "tabela de reservadas" consultada após casar IDENT\_BASE (ver nota do slide 26\)  |
| **Testes aceitos** | if (palavra-chave válida); while (palavra-chave válida)  |
| **Testes Rejeitados** | elseif (não é palavra-chave exata); while1 (não é palavra-chave exata)  |
| **Testes Fronteira** | ifelse (rejeitado — não é palavra-chave exata); returnValue (rejeitado — seria IDENT\_BASE, não KEYWORD\_EXT)   |



# Tabela 10 — REL\_OP

| Classe 10 |  |
| :---- | :---- |
| **Nome da classe** | REL\_OP |
| **Descrição** | Operadores relacionais utilizados para realizar comparações lógicas no código  |
| **Exemplos aceitos** | \==, \!=, \<, \<=, \>, \>= |
| **Definição Matemática** | L\_Rel \= { \==, \!=, \<=, \>=, \<, \> }  |
| **Conjuntos Auxiliares** | Nenhum |
| **Expressão Regular Formal** | r\_Rel \= \== ∪ \!= ∪ \<= ∪ \>= ∪ \< ∪ \>  L(r\_Rel) \= L\_Rel  |
| **Regex Python** | r"==|\!=|\<=|\>=|\<|\>"  |
| **Ação Futura** | Emitir o token REL\_OP correspondente ao operador reconhecido  |
| **Testes aceitos** | \== (Igualdade) \!= (diferença) |
| **Testes Rejeitados** | \=> (Ordem invertida dos símbolos, não corresponde a nenhum operador da linguagem) |
| **Testes Fronteira** | \= (Pertence a classe ASSIGN), ‘’ (não contém palavra vazia) |


# Tabela 11 — BLOCK\_DELIMITER

| Classe 11 | BLOCK\_DELIMITER  |
| :---- | :---- |
| **Nome da classe** | BLOCK\_DELIMITER |
| **Descrição** | Chaves usadas como delimitadores para agrupar e separar blocos de código na extensão |
| **Exemplos aceitos** | {, }  |
| **Definição Matemática** | L\_BlockDelim \= { {, } }  |
| **Conjuntos Auxiliares** | Nenhum |
| **Expressão Regular Formal** | r\_BlockDelim \= { ∪ } L(r\_BlockDelim) \= L\_BlockDelim |
| **Regex Python** | r"\[{}\]" |
| **Ação Futura** | Emitir o token BLOCK\_DELIMITER correspondente ao símbolo reconhecido  |
| **Testes aceitos** | { (símbolo de abertura de bloco), } (símbolo de fechamento de bloco) |
| **Testes Rejeitados** | \[, \] (ambos não pertencem ao alfabeto da calsse) |
| **Testes Fronteira** | {} (deve ser dois tokens separados) |
