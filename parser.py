import ply.yacc as yacc
from lexer import tokens


def p_S(p):
    'S : N VP'
    p[0] = '[S [N ' + p[1] + ' ] ' + p[2] + ' ]'

def p_VP_conj(p):
    'VP : VP Conj VP'
    p[0] = '[VP ' + p[1] + ' [Conj ' + p[2] + ' ] ' + p[3] + ' ]'

def p_VP_Vi(p):
    'VP : Vi'
    p[0] = '[VP [Vi ' + p[1] + ' ] ]'


def p_VP_Vt(p):
    'VP : Vt N'
    p[0] = '[VP [Vt ' + p[1] + ' ] [N ' + p[2] + ' ] ]'


def p_VP_Vd(p):
    'VP : Vd N N'
    p[0] = '[VP [Vd ' + p[1] + ' ] [N ' + p[2] + ' ] [N ' + p[3] + ' ] ]'


def p_error(p):
    print("Syntax Error in input!")


parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
