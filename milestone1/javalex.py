import ply.lex as lex
from sys import argv

lexeme=[]
tok=[]
count=[]


keywords=('ABSTRACT','BREAK','BYTE','CASE','CATCH','CONTINUE',
	'DEFAULT','DO','DOUBLE','ENUM','EXTENDS','FINAL',
	'IMPLEMENTS','IMPORT','INSTANCEOF','INTERFACE',
	'LONG','NEW','NULL','PACKAGE','PROTECTED','RETURN',
	'SHORT','STATIC','SUPER','SWITCH','THIS','THROW','THROWS',
	'TRY','VOID','VOLATILE',
	'CLASS','PUBLIC','PRIVATE','INT','FLOAT',
	'BOOLEAN','CHAR','IF','ELSE','WHILE','FOR','TRUE',
	'FALSE','TRANSIENT','SYNCHRONIZED','NATIVE',
	'FINALLY','ASSERT','GOTO','CONST')

tokens=['DOT',
	'LINECOMMENT',
	'COMMENT',
	'ID',
	'NUM',
	'STRING',
	'EQUALS',
	'ASSIGN',
	'OR','AND','NOT','NEQ','GTEQ','LTEQ','GTHAN','LTHAN',
	'ENDCOLON','COLON','PLUSPLUS','MINUSMINUS',
	'LPREN','RPREN','BEGINBLOCK','ENDBLOCK','SQPRENLEFT','SQPRENRIGHT',
	'PLUS','MINUS','MULT','DIVIDE','MODULO',
	'COMA','DIVIDEEQUALS','MULTEQUALS','PLUSEQUALS','MINUSEQUALS',
	'MODULOEQUALS','LEFTSHIFT','RIGHTSHIFT','URIGHTSHIFT',
	'LEFTSHIFTEQUALS','RIGHTSHIFTEQUALS','URIGHTSHIFTEQUALS',
	'BAND','BOR','BXOR','BCOMPLEMENT',
	'BANDEQUALS','BOREQUALS','BXOREQUALS'
	] +[ k for k in keywords]

literals='()+-*/=?:,.^|&~!=[]{};<>@%'

def t_DOT(t):
	r'\.'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t	

def t_DIVIDEEQUALS(t):
	r'/='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MULTEQUALS(t):
	r'\*='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_PLUSEQUALS(t):
	r'\+='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MINUSEQUALS(t):
	r'\-='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MODULOEQUALS(t):
	r'%='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_BAND(t):
	r'&'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_BOR(t):
	r'\|'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_BXOR(t):
	r'\^'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t


def t_BANDEQUALS(t):
	r'&='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_BOREQUALS(t):
	r'\|='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_BXOREQUALS(t):
	r'\^='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t


def t_BCOMPLEMENT(t):
	r'\~'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t


def t_URIGHTSHIFTEQUALS(t):
	r'>>>='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t


def t_URIGHTSHIFT(t):
	r'>>>'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_RIGHTSHIFTEQUALS(t):
	r'>>='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_RIGHTSHIFT(t):
	r'>>'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t
	
def t_LEFTSHIFTEQUALS(t):
	r'<<='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_LEFTSHIFT(t):
	r'<<'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_COMMENT(t):
		r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
		t.lexer.lineno += t.value.count('\n')

def t_ID(t):
	r'[A-Za-z][A-Za-z0-9_]*'
	if t.value.upper() in keywords:
		t.type = t.value.upper()
		try:
			i=lexeme.index(t.value)
			count[i]=count[i]+1
		except ValueError:
			lexeme.append(t.value)
			tok.append("Keywords")
			count.append(1)

	else:
		try:
			i=lexeme.index(t.value)
			count[i]=count[i]+1
		except ValueError:
			lexeme.append(t.value)
			tok.append("Identifier")
			count.append(1)
	return t

def t_NUM(t):
	#r'([1-9][0-9]*+0)(\.[0-9]*(E[+-]?[0-9]*)?)?'
	r'[+-]?[0-9]+'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Number")
		count.append(1)
	t.value=int(t.value)
	return t

def t_PLUS(t):
	r'\+'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MINUS(t):
	r'\-'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MULT(t):
	r'\*'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_DIVIDE(t):
	r'/'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MODULO(t):
	r'%'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_OR(t):
	r'\|\|'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_AND(t):
	r'&&'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_NOT(t):
	r'!'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_NEQ(t):
	r'!='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_GTEQ(t):
	r'>='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t;

def t_LTEQ(t):
	r'<='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_GTHAN(t):
	r'>'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t;

def t_LTHAN(t):
	r'<'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_ASSIGN(t):
	r'='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_EQUALS(t):
	r'=='
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_LPREN(t):
	r'\('
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_RPREN(t):
	r'\)'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_SQPRENLEFT(t):
	r'\['
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_SQPRENRIGHT(t):
	r'\]'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_BEGINBLOCK(t):
	r'\{'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_ENDBLOCK(t):
	r'\}'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t



def t_ENDCOLON(t):
	r'\;'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_COLON(t):
	r':'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_COMA(t):
	r','
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Separator")
		count.append(1)
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_MINUSMINUS(t):
	r'\-\-'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

def t_EXPONENT(t):
	r'\*\*'
	try:
		i=lexeme.index(t.value)
		count[i]=count[i]+1
	except ValueError:
		lexeme.append(t.value)
		tok.append("Operator")
		count.append(1)
	return t

t_ignore =' \t\x0c'

def t_LINECOMMENT(t):
	r'//(?!\n)*\n$'
	return t

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno+= len(t.value)

def t_error(t):
	print("Illegal character '{}' ({}) in line {}".format(t.value[0], hex(ord(t.value[0])), t.lexer.lineno))
	t.lexer.skip(1)



		
lexer=lex.lex()

