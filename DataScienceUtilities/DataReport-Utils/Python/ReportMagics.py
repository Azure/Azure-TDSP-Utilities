#iPython notebook magic
from IPython.core.magic import  (
    Magics, magics_class, cell_magic, line_magic,register_line_cell_magic, needs_local_scope
)

@magics_class
class ReportMagic(Magics):
    var_files = ''
    def __init__(self, shell,  data):
        super(ReportMagic,self).__init__(shell)
        self._code_store = []
        self._markdown_store = []
        self._conf_code_store=[]
        self._conf_markdown_store=[]
        self.data = data
        shell.user_ns['__mycodestore'] = self._code_store
        shell.user_ns['__mymarkdownstore'] = self._markdown_store
        self.ip = get_ipython()
    
    @cell_magic
    @needs_local_scope
    def add_code_to_report(self, line='\r\n', cell='\r\n'):
        """store the cell in the store"""
            
        self._code_store.append('\r\n')
        self._code_store.append(cell)
        self.ip.run_cell(cell)
    
    @line_magic
    @needs_local_scope
    def add_conf_line_to_report(self, line, cell=None,local_ns=None):
        """store the cell in the store"""
        if cell is None:
            cell = line
        
        self._code_store.append(cell)
        self._code_store = list(set(self._code_store))
        self.ip.run_cell(cell)
        return cell
    
    @line_magic
    @needs_local_scope
    def add_interaction_code_to_report(self, line, cell=None,local_ns=None):
        """store the cell in the store"""
        if cell is None:
            cell = line
        
        self._code_store.append(cell)
        self._code_store = list(set(self._code_store))
        self.ip.run_cell(cell)
        return cell
    
    @line_magic
    def add_markdown_to_report(self, line):
        """store the cell in the store"""      
        self._markdown_store.append(cell)

    @cell_magic
    @needs_local_scope
    def add_conf_code_to_report(self, line, cell):
        """store the cell in the store"""
        self._conf_code_store.append("\r\n")    
        self._conf_code_store.append(cell)    
        self.ip.run_cell(cell)

    @cell_magic
    def add_conf_markdown_to_report(self, line, cell):
        """store the cell in the store"""
        self._conf_markdown_store.append(cell)
        
    @line_magic
    def show_report(self,line):
        """show all recorded statements"""
        self._conf_markdown_store = ['# Configuration Code']
        self._markdown_store = ['## Target variable']
        return self._conf_markdown_store,self._conf_code_store ,self._markdown_store,self._code_store

    @line_magic
    def reset_report(self, line):
        self._markdown_store = []
        self._code_store = []

    @line_magic
    def reset_all(self, line):
        self._conf_markdown_store = []
        self._markdown_store = []
        self._conf_code_store = []
        self._code_store = []

# This class must then be registered with a manually created instance,
# since its constructor has different arguments from the default:
ip = get_ipython()
magics = ReportMagic(ip, 0)
ip.register_magics(magics)
