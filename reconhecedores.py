import re

pattern = {
    "KEYWORD_CORE": re.compile(r"int|print"),
    "IDENT_BASE": re.compile(r"[A-Za-z_][A-Za-z0-9_]*"),
    "INT_LITERAL": re.compile(r"[0-9]+"),
    "ARITH_OP": re.compile(r"[-+*/]"),
    "ASSIGN": re.compile(r"="),
    "DELIMITER_CORE": re.compile(r"[();]"),
    "LINE_COMMENT": re.compile(r"//[^\r\n]*"),
    "WHITESPACE": re.compile(r"[ \t\r\n]+"),
    
    "KEYWORD_EXT": re.compile(r"if|else|while"),
    "REL_OP": re.compile(r"==|!=|<=|>=|<|>"),
    "BLOCK_DELIMITER": re.compile(r"[{}]")
}

def reconhece(classe: str, palavra: str) -> bool:
    
    if classe not in pattern:
        return False
    
    padrao = pattern[classe]
    return padrao.fullmatch(palavra) is not None