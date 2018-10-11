import gdb

class UniversePrint(gdb.Command):
    def __init___(self):
        super(gdb.Command,self).__init__("heap-print",gdb.COMMAND_USER)


    def invoke(self):
        gdb.:
