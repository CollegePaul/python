

characters = ["Mario", "Toad"] 
age = 10
rain = True


def printvars():

   tmp = globals().copy()
   [print(k,'  :  ',v,' type:' , type(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]

printvars()


def printObj(Obj, OutputMax=100):

   tmp = Obj.__dict__
   [print(k,'  :  ',str(v)[:OutputMax],' type:' , type(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]