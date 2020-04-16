### Refrence
### https://cs.au.dk/~amoeller/RegAut/JavaBNF.html



import sys
import ply.yacc as yacc
from javalex import *

if len(sys.argv)==2:
	filename = sys.argv[1]
else:
	print "No input file"
	exit(0)


def p_compilation_unit(p):
	"""compilation_unit : package_declaration_opt import_declarations_opt type_declarations_opt
	"""

def p_package_declaration_opt(p):
	"""package_declaration_opt : empty
		| PACKAGE package_name ENDCOLON
	"""

def p_import_declarations_opt(p):
	"""import_declarations_opt : empty
		| import_declarations
	"""

def p_import_declarations(p):
	"""import_declarations : import_declarations import_declaration
		| import_declaration
	"""

def p_import_declaration(p):
	"""import_declaration : single_type_import_declaration
		| type_import_on_demand_declaraton
	"""

def p_single_type_import_declaration(p):
	"""single_type_import_declaration : IMPORT type_name ENDCOLON
	"""

def p_type_import_on_demand_declaraton(p):
	"""type_import_on_demand_declaraton : IMPORT package_name DOT MULT ENDCOLON
	"""

def p_type_declarations_opt(p):
	"""type_declarations_opt : empty
		| type_declarations
	"""

def p_type_declarations(p):
	"""type_declarations : type_declaration type_declarations
		| type_declaration
	"""

def p_type_declaration(p):
	"""type_declaration : class_declaration
		| interface_declaration
		| ENDCOLON
	"""

def p_class_declaration(p):
	"""class_declaration : class_modifiers_opt CLASS ID super_opt interfaces_opt class_body
	"""

def p_class_modifiers_opt(p):
	"""class_modifiers_opt : empty
		| class_modifiers
	"""

def p_class_modifiers(p):
	"""class_modifiers : class_modifier class_modifiers
		| class_modifier
	"""

def p_class_modifier(p):
	"""class_modifier : PUBLIC
		| ABSTRACT
		| FINAL
	"""

def p_super_opt(p):
	"""super_opt : empty
		| super_c
	"""

def p_super_c(p):
	"""super_c : EXTENDS class_type
	"""

def p_interfaces_opt(p):
	"""interfaces_opt : empty
		| interfaces
	"""

def p_interfaces(p):
	"""interfaces : IMPLEMENTS interface_type_list
	"""

def p_interface_type_list(p):
	"""interface_type_list : interface_type
		| interface_type_list COMA interface_type
	"""

def p_class_body(p):
	"""class_body : BEGINBLOCK class_body_declarations_opt ENDBLOCK
	"""

def p_class_body_declarations_opt(p):
	"""class_body_declarations_opt : empty
		| class_body_declarations
	"""

def p_class_body_declarations(p):
	"""class_body_declarations : class_body_declaration class_body_declarations
		| class_body_declaration
	"""

def p_class_body_declaration(p):
	"""class_body_declaration : class_member_declaration
		| static_initializer
		| constructor_declaration
	"""

def p_class_member_declaration(p):
	"""class_member_declaration : field_declaration
		| method_declaration
	"""

def p_static_initializer(p):
	"""static_initializer : STATIC block
	"""

def p_constructor_declaration(p):
	"""constructor_declaration : constructor_modifiers_opt constructor_declarator throws_opt constructor_body
	"""

def p_constructor_modifiers_opt(p):
	"""constructor_modifiers_opt : empty
		| constructor_modifiers
	"""

def p_constructor_modifiers(p):
	"""constructor_modifiers : constructor_modifier constructor_modifiers
		| constructor_modifier
	"""

def p_constructor_modifier(p):
	"""constructor_modifier : PUBLIC
		| PROTECTED
		| PRIVATE
	"""

def p_constructor_declarator(p):
	"""constructor_declarator : simple_type_name LPREN formal_parameter_list_opt RPREN
	"""

def p_formal_parameter_list_opt(p):
	"""formal_parameter_list_opt : empty
		| formal_parameter_list
	"""

def p_formal_parameter_list(p):
	"""formal_parameter_list : formal_parameter
		| formal_parameter_list COMA formal_parameter
	"""

def p_formal_parameter(p):
	"""formal_parameter : type variable_declarator_id
	"""

def p_throws_opt(p):
	"""throws_opt : empty
		| throws_d
	"""

def p_throws_d(p):
	"""throws_d : THROWS class_type_list
	"""

def p_class_type_list(p):
	"""class_type_list : class_type
		| class_type_list COMA class_type
	"""

def p_constructor_body(p):
	"""constructor_body : BEGINBLOCK explicit_constructor_invocation_opt block_statements_opt ENDBLOCK
	"""

def p_explicit_constructor_invocation_opt(p):
	"""explicit_constructor_invocation_opt : empty
		| explicit_constructor_invocation
	"""

def p_explicit_constructor_invocation(p):
	"""explicit_constructor_invocation : THIS LPREN argument_list_opt RPREN
		| SUPER LPREN argument_list_opt RPREN 
	"""


def p_field_declaration(p):
	"""field_declaration : field_modifiers_opt type variable_declarators ENDCOLON
	"""

def p_field_modifiers_opt(p):
	"""field_modifiers_opt : empty
		| field_modifiers
	"""

def p_field_modifiers(p):
	"""field_modifiers : field_modifier field_modifiers
		| field_modifier
	"""

def p_field_modifier(p):
	"""field_modifier : PUBLIC
		| PROTECTED
		| PRIVATE
		| STATIC
		| FINAL
		| TRANSIENT
		| VOLATILE
	"""

def p_variable_declarators(p):
	"""variable_declarators : variable_declarator
		| variable_declarator COMA variable_declarators
	"""

def p_variable_declarator(p):
	"""variable_declarator : variable_declarator_id ASSIGN variable_initializer
		| variable_declarator_id 
	"""

def p_variable_declarator_id(p):
	"""variable_declarator_id : ID
		| variable_declarator_id SQPRENLEFT SQPRENRIGHT 
	"""

def p_variable_initializer(p):
	"""variable_initializer : expression
		| array_initializer
	"""

def p_method_declaration(p):
	"""method_declaration : method_header method_body
	"""

def p_method_header(p):
	"""method_header : field_modifiers_opt result_type method_declarator throws_opt
	"""
def p_result_type(p):
	"""result_type : type
		| VOID
	"""

#def p_method_modifiers_opt(p):
#	"""method_modifiers_opt : empty
#		| method_modifiers
#	"""
#def p_method_modifiers(p):
#	"""method_modifiers : method_modifier
#		| method_modifiers method_modifier
#	"""
#def p_method_modifier(p):
#	"""method_modifier : PUBLIC
#		| PROTECTED
#		| PRIVATE
#		| STATIC
#		| ABSTRACT
#		| FINAL
#		| SYNCHRONIZED
#		| NATIVE
#	"""
def p_method_declarator(p):
	"""method_declarator : ID LPREN formal_parameter_list_opt RPREN
	"""



def p_method_body(p):
	"""method_body : block
		| ENDCOLON
	"""

def p_interface_declaration(p):
	"""interface_declaration : interface_modifiers_opt INTERFACE ID extends_interfaces_opt interface_body
	"""

def p_interface_modifiers_opt(p):
	"""interface_modifiers_opt : empty
		| interface_modifiers
	"""

def p_interface_modifiers(p):
	"""interface_modifiers : interface_modifiers interface_modifier
		| interface_modifier
	"""

def p_interface_modifier(p):
	"""interface_modifier : PUBLIC
		| ABSTRACT
	"""

def p_extends_interfaces_opt(p):
	"""extends_interfaces_opt : empty
		| extends_interfaces
	"""

def p_extends_interfaces(p):
	"""extends_interfaces : EXTENDS interface_type
		| extends_interfaces COMA interface_type
	"""

def p_interface_body(p):
	"""interface_body : BEGINBLOCK interface_member_declarations_opt ENDBLOCK
	"""

def p_interface_member_declarations_opt(p):
	"""interface_member_declarations_opt : empty
		| interface_member_declarations
	"""

def p_interface_member_declarations(p):
	"""interface_member_declarations : interface_member_declaration interface_member_declarations
		| interface_member_declaration
	"""

def p_interface_member_declaration(p):
	"""interface_member_declaration : constant_declaration
		| abstract_method_declaration
	"""

def p_constant_declaration(p):
	"""constant_declaration : constant_modifiers type variable_declarator
	"""

def p_constant_modifiers(p):
	"""constant_modifiers : PUBLIC
		| STATIC
		| FINAL
	"""

def p_abstract_method_declaration(p):
	"""abstract_method_declaration : abstract_method_modifiers_opt result_type method_declarator throws_opt ENDCOLON
	"""

def p_abstract_method_modifiers_opt(p):
	"""abstract_method_modifiers_opt : empty
		| abstract_method_modifiers
	"""

def p_abstract_method_modifiers(p):
	"""abstract_method_modifiers : abstract_method_modifier abstract_method_modifiers
		| abstract_method_modifier
	"""

def p_abstract_method_modifier(p):
	"""abstract_method_modifier : PUBLIC
		| ABSTRACT
	"""

def p_array_initializer(p):
	"""array_initializer : BEGINBLOCK variable_initializers_opt ENDBLOCK
	"""


def p_variable_initializers_opt(p):
	"""variable_initializers_opt : empty
		| variable_initializers
	"""

def p_variable_initializers(p):
	"""variable_initializers : variable_initializer COMA variable_initializers
		| variable_initializer
	"""





#####################  TYPES ##########################




def p_type(p):
	"""type : primitive_type
		| reference_type
	"""

def p_primitive_type(p):
	"""primitive_type : numeric_type
		| BOOLEAN
	"""

def p_numeric_type(p):
	"""numeric_type : integral_type
		| floating_point_type
	"""

def p_integral_type(p):
	"""integral_type : BYTE
		| SHORT
		| INT
		| LONG
		| CHAR
	"""

def p_floating_point_type(p):
	"""floating_point_type : FLOAT
		| DOUBLE
	"""

def p_reference_type(p):
	"""reference_type : class_or_interface_type
		| array_type
	"""

def p_class_or_interface_type(p):
	"""class_or_interface_type : class_type
		| interface_type
	"""

def p_class_type(p):
	"""class_type : type_name
	"""

def p_interface_type(p):
	"""interface_type : type_name
	"""

def p_array_type(p):
	"""array_type : type SQPRENLEFT SQPRENRIGHT
	"""


############### Blocks and Commands ###################




def p_block(p):
	"""block : BEGINBLOCK block_statements_opt ENDBLOCK
	"""

def p_block_statements_opt(p):
	"""block_statements_opt : empty
		| block_statements
	"""

def p_block_statements(p):
	"""block_statements : block_statement block_statements
		| block_statement
	"""

def p_block_statement(p):
	"""block_statement : local_variable_declaration_statement
		| statement
	"""

def p_local_variable_declaration_statement(p):
	"""local_variable_declaration_statement : local_variable_declaration ENDCOLON
	"""

def p_local_variable_declaration(p):
	"""local_variable_declaration : type variable_declarators
	"""

def p_statement(p):
	"""statement : statement_without_trailing_substatement
		| labeled_statement
		| if_then_statement
		| if_then_else_statement
		| while_statement
		| for_statement
	"""

def p_statement_no_short_if(p):
	"""statement_no_short_if : statement_without_trailing_substatement
		| labeled_statement_no_short_if
		| if_then_else_statement_no_short_if
		| while_statement_no_short_if
		| for_statement_no_short_if
	"""

def p_statement_without_trailing_substatement(p):
	"""statement_without_trailing_substatement : block
		| empty_statement
		| expression_statement
		| switch_statement
		| do_statement
		| break_statement
		| continue_statement
		| return_statement
		| synchronized_statement
		| throws_statement
		| try_statement
	"""

def p_empty_statement(p):	
	"""empty_statement : ENDBLOCK
	"""

def p_labeled_statement(p):
	"""labeled_statement : ID COLON statement
	"""

def p_labeled_statement_no_short_if(p):
	"""labeled_statement_no_short_if : ID COLON statement_no_short_if
	"""

def p_expression_statement(p):
	"""expression_statement : statement_expression ENDCOLON
	"""

def p_statement_expression(p):
	"""statement_expression : assignment
		| preincrement_expression
		| postincrement_expression
		| predecrement_expression
		| postdecrement_expression
		| method_invocation
		| class_instance_creation_expression
	"""

def p_if_then_statement(p):
	"""if_then_statement : IF LPREN expression RPREN statement
	"""

def p_if_then_else_statement(p):
	"""if_then_else_statement : IF LPREN expression RPREN statement_no_short_if ELSE statement
	"""

def p_if_then_else_statement_no_short_if(p):
	"""if_then_else_statement_no_short_if : IF LPREN expression RPREN statement_no_short_if ELSE statement_no_short_if
	"""

def p_switch_statement(p):
	"""switch_statement : SWITCH LPREN expression RPREN switch_block
	"""

def p_switch_block(p):
	"""switch_block : BEGINBLOCK switch_block_statement_groups_opt switch_labels_opt ENDBLOCK
	"""

def p_switch_block_statement_groups_opt(p):
	"""switch_block_statement_groups_opt : empty
		| switch_block_statement_groups
	"""

def p_switch_block_statement_groups(p):
	"""switch_block_statement_groups : switch_block_statement_group switch_block_statement_groups
		| switch_block_statement_group
	"""

def p_switch_block_statement_group(p):
	"""switch_block_statement_group : switch_labels block_statements
	"""


def p_switch_labels_opt(p):
	"""switch_labels_opt : empty
		| switch_labels
	"""


def p_switch_labels(p):
	"""switch_labels : switch_label switch_labels
		| switch_label
	"""

def p_switch_label(p):
	"""switch_label : CASE constant_expression COLON
		| DEFAULT COLON
	"""

def p_while_statement(p):
	"""while_statement : WHILE LPREN expression RPREN statement
	"""

def p_while_statement_no_short_if(p):
	"""while_statement_no_short_if : WHILE LPREN expression RPREN statement_no_short_if
	"""

def p_do_statement(p):
	"""do_statement : DO statement WHILE LPREN expression RPREN ENDCOLON
	"""


def p_for_statement(p):
	"""for_statement : FOR LPREN for_init_opt ENDCOLON expression_opt ENDCOLON for_update_opt RPREN statement
	"""

def p_for_statement_no_short_if(p):
	"""for_statement_no_short_if : FOR LPREN for_init_opt ENDCOLON expression_opt ENDCOLON for_update_opt RPREN statement_no_short_if
	"""

def p_for_init_opt(p):
	"""for_init_opt : empty
		| for_init
	"""
def p_expression_opt(p):
	"""expression_opt : empty
		| expression
	"""

def p_for_update_opt(p):
	"""for_update_opt : empty
		| for_update
	"""
def p_for_init(p):
	"""for_init : statement_expression_list
		| local_variable_declaration
	"""

def p_for_update(p):
	"""for_update : statement_expression_list
	"""

def p_statement_expression_list(p):
	"""statement_expression_list : statement_expression COMA statement_expression_list
		| statement_expression
	"""

def p_break_statement(p):
	"""break_statement : BREAK id_opt ENDCOLON
	"""

def p_continue_statement(p):
	"""continue_statement : CONTINUE id_opt ENDCOLON
	"""

def p_id_opt(p):
	"""id_opt : empty
		| ID
	"""

def p_return_statement(p):
	"""return_statement : RETURN expression_opt ENDCOLON
	"""

def p_throws_statement(p):
	"""throws_statement : THROW expression ENDCOLON
	"""

def p_synchronized_statement(p):
	"""synchronized_statement : SYNCHRONIZED LPREN expression RPREN block
	"""

def p_try_statement(p):
	"""try_statement : TRY block catches
		| TRY block catches_opt finally_c
	"""

def p_catches_opt(p):
	"""catches_opt : empty
		| catches
	"""

def p_catches(p):
	"""catches : catch_clause
		| catches catch_clause
	"""

def p_catch_clause(p):
	"""catch_clause : CATCH LPREN formal_parameter RPREN block
	"""

def p_finally_c(p):
	"""finally_c : FINALLY block
	"""




####################### Expressions ##################

def p_constant_expression(p):
	"""constant_expression : expression
	"""

def p_expression(p):
	"""expression : assignment_expression
	"""

def p_assignment_expression(p):
	"""assignment_expression : conditional_expression
		| assignment
	"""

def p_assignment(p):
	"""assignment : left_hand_side assignment_operator assignment_expression
	"""

def p_left_hand_side(p):
	"""left_hand_side : expression_name
		| field_access
		| array_access
	"""

def p_assignment_operator(p):
	"""assignment_operator : ASSIGN
		| MULTEQUALS
		| DIVIDEEQUALS
		| MODULOEQUALS
		| PLUSEQUALS
		| MINUSEQUALS
		| LEFTSHIFTEQUALS
		| RIGHTSHIFTEQUALS
		| URIGHTSHIFTEQUALS
		| BANDEQUALS
		| BXOREQUALS
		| BOREQUALS
	"""





def p_conditional_expression(p):
	"""conditional_expression : conditional_or_expression_opt expression COLON conditional_expression 
		| conditional_or_expression
	"""

def p_conditional_or_expression_opt(p):
	"""conditional_or_expression_opt : empty
		| conditional_or_expression
	"""

def p_conditional_or_expression(p):
	"""conditional_or_expression : conditional_or_expression OR conditional_and_expression
		| conditional_and_expression
	"""


def p_conditional_and_expression(p):
	"""conditional_and_expression : conditional_and_expression AND inclusive_or_expression
		| inclusive_or_expression
	"""

def p_inclusive_or_expression(p):
	"""inclusive_or_expression : inclusive_or_expression BOR exclusive_or_expression
		| exclusive_or_expression
	"""

def p_exclusive_or_expression(p):
	"""exclusive_or_expression : exclusive_or_expression BXOR and_expression
		| and_expression
	"""

def p_and_expression(p):
	"""and_expression : and_expression BAND equality_expression
		| equality_expression
	"""

def p_equality_expression(p):
	"""equality_expression : equality_expression EQUALS relational_expression
		| equality_expression NEQ relational_expression
		| relational_expression
	"""

def p_relational_expression(p):	
	"""relational_expression : relational_expression LTHAN shift_expression
		| relational_expression GTHAN shift_expression
		| relational_expression LTEQ shift_expression
		| relational_expression GTEQ shift_expression
		| relational_expression INSTANCEOF reference_type
		| shift_expression
	"""

def p_shift_expression(p):
	"""shift_expression : shift_expression LEFTSHIFT additive_expression
		| shift_expression RIGHTSHIFT additive_expression
		| shift_expression URIGHTSHIFT additive_expression
		| additive_expression	
	"""

def p_additive_expression(p):
	"""additive_expression : additive_expression PLUS multiplicative_expression
		| additive_expression MINUS multiplicative_expression
		| multiplicative_expression
	"""

def p_multiplicative_expression(p):
	"""multiplicative_expression : multiplicative_expression MULT unary_expression
		| multiplicative_expression DIVIDE unary_expression
		| multiplicative_expression MODULO unary_expression
		| unary_expression
	"""

def p_cast_expression(p):
	"""cast_expression : LPREN primitive_type RPREN unary_expression
		| LPREN reference_type RPREN unary_expression_not_plus_minus
	"""

def p_unary_expression(p):
	"""unary_expression : preincrement_expression
		| predecrement_expression
		| PLUS unary_expression
		| MINUS unary_expression
		| unary_expression_not_plus_minus
	"""

def p_preincrement_expression(p):
	"""preincrement_expression : PLUSPLUS unary_expression
	"""

def p_predecrement_expression(p):
	"""predecrement_expression : MINUSMINUS unary_expression
	"""

def p_unary_expression_not_plus_minus(p):
	"""unary_expression_not_plus_minus : postfix_expression
		| '~' unary_expression
		| NOT unary_expression
		| cast_expression
	"""

def p_postdecrement_expression(p):
	"""postdecrement_expression : postfix_expression MINUSMINUS
	"""

def p_postincrement_expression(p):
	"""postincrement_expression : postfix_expression PLUSPLUS
	"""

def p_postfix_expression(p):
	"""postfix_expression : primary
		| expression_name
		| postincrement_expression
		| postdecrement_expression
	"""

def p_method_invocation(p):
	"""method_invocation : method_name LPREN argument_list_opt RPREN
		| primary DOT ID LPREN argument_list_opt RPREN
		| SUPER DOT ID LPREN argument_list_opt RPREN
	"""

def p_field_access(p):
	"""field_access : primary DOT ID
		| SUPER DOT ID
	"""

def p_primary(p):
	"""primary : primary_no_new_array
		| array_creation_expression
	"""

def p_primary_no_new_array(p):
	"""primary_no_new_array : literal
		| THIS
		| LPREN expression RPREN
		| class_instance_creation_expression
		| field_access
		| method_invocation
		| array_access
	"""

def p_class_instance_creation_expression(p):
	"""class_instance_creation_expression : NEW class_type LPREN argument_list_opt RPREN
	"""


def p_argument_list_opt(p):
	"""argument_list_opt : empty
		| argument_list
	"""

def p_argument_list(p):
	"""argument_list : expression COMA argument_list 
		| expression
	"""


def p_array_creation_expression(p):
	"""array_creation_expression : NEW primitive_type dim_exprs dims_opt
		| NEW class_or_interface_type dim_exprs dims_opt
	"""


def p_dim_exprs(p):
	"""dim_exprs : dim_expr dim_exprs
		| dim_expr
	"""

def p_dim_expr(p):
	"""dim_expr : SQPRENLEFT expression SQPRENRIGHT
	"""

def p_dims_opt(p):
	"""dims_opt : empty
		| dims
	"""

def p_dims(p):
	"""dims : SQPRENLEFT SQPRENRIGHT dims
		| SQPRENLEFT SQPRENRIGHT
	"""

def p_array_access(p):
	"""array_access : expression_name SQPRENLEFT expression SQPRENRIGHT
		| primary_no_new_array SQPRENLEFT expression SQPRENRIGHT 
	"""

def p_package_name(p):
	"""package_name : type_name
	"""

def p_type_name(p):
	"""type_name : ID
		| package_name DOT ID
	"""

def p_simple_type_name(p):
	"""simple_type_name : ID
	"""

def p_expression_name(p):
	"""expression_name : method_name
	"""

def p_method_name(p):
	"""method_name : ID
		| ambiguous_name DOT ID
	"""

def p_ambiguous_name(p):
	"""ambiguous_name : ID DOT ambiguous_name
		| ID
	"""

def p_literal(p):
	"""literal : NUM
		| STRING
		| boolean_literal
	"""

def p_boolean_literal(p):
	"""boolean_literal : TRUE
		| FALSE
	"""

def p_empty(p):
	"""empty : """
	pass

def p_error(p):
	print("Syntax error in input!", p)


parser=yacc.yacc(start="compilation_unit",debug="True",optimize=False)


inputfile=open(filename,'r')
data=inputfile.read()
result=parser.parse(data,debug=2) 
