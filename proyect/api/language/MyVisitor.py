from grammarVisitor import grammarVisitor
from grammarParser import grammarParser

class MyVisitor(grammarVisitor):
    def _init_(self):
        self.memory = {}
    #Definimos la asignación
    def visitAssign(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value
    #Definimos la asignación
    def visitPrint(self,ctx):
        value=self.visit(ctx.expr())
        print(value)