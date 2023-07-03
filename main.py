from lexico import tokens
import ply.yacc as yacc


#Interfazzz------------------

import tkinter as tk

def textoconsole():
      
    codigo = cajacodigo.get("1.0",'end-1c') #obtengo el texto que el usuario ingresa cuando da click en check
    #print(codigo) #muestra en consola el texto del user
    with open("codigo.txt", "w") as archivo:
        archivo.write(codigo) #lo guardo en un txt

    #programa principal PLY yacc----------

    #Intructions
    def p_instruction(p):
      'instruction : instructionBody'

    def p_instructionFunction(p):
      '''
      instruction : defFunction
                  | blockFunction
                  | lambda_expression
      '''

    #Andres
    def p_defFunction(p):
      '''
        defFunction : DEF ID LPAREN parameters RPAREN instructionBody END
                  | DEF ID LPAREN RPAREN END
                  | DEF ID LPAREN RPAREN instructionBody END
                  | DEF ID LPAREN RPAREN YIELD END
                  | DEF ID LPAREN parameters RPAREN instructionBody YIELD END
      '''

    #Nick
    def p_lambda_expression(p):
      """lambda_expression : LAMBDA LBRACE instructionBody RBRACE
                          |  ID ASSIGNMENT LAMBDA LBRACE instructionBody RBRACE
      """
    #estructura de control if ---------------------------------------
    #Andres
    def p_conditional(p):
      '''
        conditional : IF condition instructionBody END
                    | IF condition instructionBody conditionalElsif END
                    | IF condition instructionBody ELSE instructionBody END
                    | IF condition instructionBody conditionalElsif ELSE instructionBody END
      '''
    def p_elsif(p):
      '''
      elsif : ELSIF condition instructionBody 
      '''
    def p_conditionalElsif(p):
      '''
      conditionalElsif : elsif 
                      | elsif  conditionalElsif
      '''
    #-----------------------------------------------------
    # estructura de control while ------------------------
    #Yoser

    def p_whileLoop(P):
      '''
      whileLoop : WHILE condition instructionBody END
      '''
      
    #estructura de control for--------------------------
    #Nick
    def p_forLoop(p):
      'forLoop : FOR ID IN LPAREN INTEGER DOT DOT INTEGER RPAREN instructionBody END'
    #-------------------------------------------------
    #usos generales -----------------------------------
    def p_assignmentRule(p):
      '''
        assignmentRule : ID ASSIGNMENT number
                        | ID ASSIGNMENT ID
                        | ID ASSIGNMENT condition
                        | ID ASSIGNMENT TRUE
                        | ID ASSIGNMENT FALSE
                        | ID ASSIGNMENT creationTDA
                        | ID ASSIGNMENT operations
                        | ID ASSIGNMENT array
                        | ID ASSIGNMENT indexation
                        | ID ASSIGNMENT attribute
                        | ID ASSIGNMENT input
      '''
    def p_bodyLine(p):
      '''
        bodyLine : assignmentRule
                  | PRINT arguments
                  | conditional
                  | whileLoop
                  | functionCall
                  | arrayConcat
                  | RETURN arguments
                  | PUTS arguments
                  | method
                  | unaryOperator
                  | forLoop
      '''
    def p_instructionBody(p):
      '''
        instructionBody : bodyLine
                        | bodyLine instructionBody 
      '''

    def p_argument(p):
      '''
        argument : ID
                  | number
                  | attribute
                  | indexation
                  | STRING
                  | TRUE
                  | FALSE
                  | functionCall
                  | method
                  | condition
      '''

    def p_arguments(p):
      '''
      arguments : argument
                | argument COMMA arguments
      '''
    def p_method(p):
      '''
        method : ID DOT functionCall 
      '''

    def p_input(p):
      '''
      input : GETS DOT CHOMP DOT TO_F
            | GETS DOT CHOMP DOT TO_I
            | GETS DOT CHOMP
      '''

    #------------------------------------------------------------  
    #Parameters
    def p_parameters(p):
      '''
        parameters : ID 
                  | ID COMMA parameters 
      '''

    def p_functionCall(p):
      '''
      functionCall : ID LPAREN arguments RPAREN
                  | ID LPAREN RPAREN
                  | ID LPAREN RPAREN blockFunction
                  | ID LPAREN arguments RPAREN blockFunction
      '''

    #Yoser
    def p_blockFunction(p):
      '''
        blockFunction : LBRACE instructionBody RBRACE
                      | DO instructionBody END 
      '''

    #StructureData 
    #STACK
    #Yoser
    def p_creationStack(p):
      '''
      creationStack : STACK DOT NEW
                    | OPENBRACKET CLOSEDBRACKET
      '''

    #linkedlist
    #Andres
    def p_creationLinkedList(p):
      'creationLinkedList : LINKEDLIST DOT NEW'

    def p_creationTDA(p):
      '''
        creationTDA : creationStack
                    | creationLinkedList
                    | creationHashmap

      '''

    #Hashmap
    #Nick
    def p_creationHashmap(p):
      '''creationHashmap : HASH DOT NEW
                        | LBRACE pairs RBRACE
                        | LBRACE RBRACE
      '''
    def p_pair(p):
        '''pair : STRING COLON value'''

    def p_pairs(p):
        '''pairs : pair
                | pair COMMA pairs''' 
        
    def p_value(p):
        '''value : ID
                | STRING 
                | number
                | LBRACE pairs RBRACE
                | LBRACE RBRACE
        '''


    #Operations
    def p_arithmeticOperator(p):

      '''
        arithmeticOperator : PLUS
                            | MINUS
                            | POWER
                            | MULTIPLICATION 
                            | DIVISION
      '''
    def p_attribute(p):
      '''
        attribute : ID DOT ID
      '''

    def p_operationValue(p):
      '''
        operationValue : ID
                      | number
                      | attribute
                      | indexation
      '''
    def p_operation(p):
      '''operation : operationValue arithmeticOperator operationValue
                  | LPAREN operationValue arithmeticOperator operationValue RPAREN
      '''

    def p_operations(p):
      '''
        operations : operation
                  | operation arithmeticOperator operations
                  | operation arithmeticOperator operationValue
                  | operationValue arithmeticOperator operation
      '''

    #array----------------------------------------------
    def p_array(p):
      '''array : OPENBRACKET element_list CLOSEDBRACKET
              | OPENBRACKET CLOSEDBRACKET'''

    def p_element_list(p):
      '''element_list : conditionValue
                    | element_list COMMA conditionValue'''

    def p_conditionValue(p):
      '''
        conditionValue : ID
                      | number
                      | indexation
                      | attribute
      '''
    def p_arrayConcat(p):
      '''
      arrayConcat : ID ARRAYAPPEND ID
                  | ID ARRAYAPPEND number
      '''

    def p_indexation(p):
      '''
        indexation : ID OPENBRACKET element_list CLOSEDBRACKET
                  | ID OPENBRACKET operation CLOSEDBRACKET
      '''
    #----------------------------------------------

    def p_condition(p):
      '''
        condition : conditionValue comparator conditionValue
      '''

    def p_comparator(p):
      '''
        comparator : GREATERTHAN
                  | LESSTHAN
                  | EQUALS
                  | GREATEROREQUALS
                  | LESSOREQUALS
      '''
    def p_unaryOperator(p):
      ''' 
      unaryOperator : ID ASSIGNDECREMENT number
                    | ID ASSIGNINCREMENT number
      '''
    def p_number(p):
        '''
          number : FLOAT
                | INTEGER
        '''


    def p_error(p):
      if p:
        archivo = open("datos.txt", "a") #probar con "a"
        print("Error de sintaxis en token:", p.type)
        archivo.write("Error de sintaxis en token:{}\n".format(p.type))
        archivo.close()
        #sintactico.errok()
      else:
        archivo = open("datos.txt", "a")
        archivo.write("Syntax error at EOF\n")
        archivo.close()
        print("Syntax error at EOF")


    sintactico = yacc.yacc()

    #------leo los errores cuando ya están dentro del archivo datos.txt------------------------------
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    archivo.close()

    cajaconsole.delete("1.0", tk.END)  # Limpiar el contenido actual del widget Text
    cajaconsole.insert(tk.END, contenido)  # Insertar el contenido del archivo en el widget Text

    archivo = open("datos.txt", "w")
    archivo.write('')
    archivo.close()
    
    cajaconsole.delete("1.0", tk.END)  # Limpiar el contenido actual del widget Text
    cajaconsole.insert(tk.END, contenido)  # Insertar el contenido del archivo en el widget Text

    #----------------------------------------------Procesamiento de datos --------------------------------------------------
    archiCodigo = open('codigo.txt','r')
    for lineaCodigo in archiCodigo.readlines():
      result = sintactico.parse(lineaCodigo)

    #----------------------------------------------------fin programa principal----------------------

    
# Crear la ventana
ventana = tk.Tk()
ventana.geometry("730x700")

cajacodigo = tk.Text(ventana, width = 30,height=30 )
cajaconsole = tk.Text(ventana, width = 30,height=30 )
cajafiles = tk.Text(ventana, width = 30,height=30 )

titulo = tk.Label(ventana, text="RUBYLIX\n Simple Ruby Syntax Checker")
btopenfile = tk.Button(ventana, text = "Open file", width = 10, height=2)
btcheck = tk.Button(ventana, text = "Check", width = 10, height=2, command=textoconsole)

titulo.grid(row = 0, column = 1, pady=10)
btopenfile.grid(row = 0, column = 0, pady=10)
btcheck.grid(row = 0, column = 2, pady=10,)

cajacodigo.grid(row=1,column=1, pady=10)
cajaconsole.grid(row=1,column=2, pady=10)
cajafiles.grid(row=1,column=0, pady=10)


ventana.mainloop()

#-----------------

