from antlr4 import *
from language.GrammarLexer import GrammarLexer
from language.GrammarParser import GrammarParser
from language.MyVisitor import MyVisitor
import io
import sys

def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()
    
    #Capturan la salida
    old_stdout=sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf

    #Creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    #Visitamos el árbol con nuestro visitor
    visitor.visit(tree)
    #Capturamos salida
    output=buf.getvalue()

    return output