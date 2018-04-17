import ply.lex as lex


tokens = ['N', 'Vi', 'Vt', 'Vd', 'Conj']

t_N = r'Homer|Marge|Bart|Maggie|Lisa|SLH'
t_Vi = r'ran|sleeps|crawls'
t_Vt = r'chased|saw|petted'
t_Vd = r'sent|handed'
t_Conj = r'and|or'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n,'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

