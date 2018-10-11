import gdb

def addr_val(var_or_addr):
    if var_or_addr[0]=='*':
        return var_or_addr[1:]
    else:
        return gdb.parse_and_eval(var_or_addr)


class UniversePrint(gdb.Command):
    def __init__(self):
        super(self.__class__,self).__init__("heap-print",gdb.COMMAND_USER)

    def invoke(self,args,from_tty):
        gdb.execute("print Univser::heap()->print()")


class OopInfo(gdb.Command):
    def __init__(self):
        super(self.__class__,self).__init__("oop-info",gdb.COMMAND_USER)

    def invoke(self,arg,from_tty):
        is_oop = gdb.parse_and_eval("((oop)%s)->is_oop()" % (arg))
        if not is_oop:
            print("is not oop")
            return
        size = gdb.parse_and_eval("((oop)%s)->size()" % (arg))
        name = gdb.parse_and_eval("((oop)%s)->klass()->name()->base()" % (arg))
        print (size)
        print(name)


class OopNext(gdb.Command):
    pass


class ObjStart(gdb.Command):
    def __init__(self):
        super(self.__class__,self).__init__("obj-start",gdb.COMMAND_USER)

    def invoke(self,arg,from_tty):
        addr = addr_val(arg)
        print(addr)

UniversePrint()

OopInfo()

ObjStart()
