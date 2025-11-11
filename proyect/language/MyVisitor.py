from .GrammarVisitor import GrammarVisitor
from .GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def _init_(self):
        self.memory = {}

    #Definimos la asignación
    def visitAssign(self,ctx):
        #Se obtiene el id o nombre de la variable
        name=ctx.ID().getText()
        #Se obtiene el valor, ya sea un valor númerico o una expresión
        value=self.visit(ctx.expr())
        #Se almacena en memoria a partir del nombre y el valor
        self.memory[name]=value

    #Definimos la impresión
    def visitPrint(self,ctx):
        # Definimos la expresión que se desea mostrar
        value=self.visit(ctx.expr())
        #Imprime el valor
        print(value)
    
    #Definimos las expresiones
    def visitExpr(self, ctx):
        #Busca si existe ID
        if ctx.ID():
            #Obtiene del contexto el nombre de la variable
            name=ctx.ID().getText()
            if name not in self.memory:
                raise NameError(f"Variable '{name}' no definida")
            #Si existe el nombre retorna la variable
            return self.memory[name]
        #Busca el operador
        elif ctx.op:
            #Visita y obtiene el lado izquierdo
            left=self.visit(ctx.expr(0))
            #Visita y obtiene el lado derecho
            right=self.visit(ctx.expr(1))
            #Evalua la operación a realizar
            if ctx.op.text=="+":
                return left+right
            if ctx.op.text=="-":
                return left-right
            if ctx.op.text=="*":
                return left*right
            if ctx.op.text=="/":
                #Verifica la división por cero
                if right ==0:
                    raise ValueError("Divisón por cero")
                return left/right
            