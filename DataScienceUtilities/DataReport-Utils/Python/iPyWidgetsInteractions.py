import os
import errno
from functools import partial

import IPython
import ipywidgets
from ipywidgets import widgets
from ipywidgets import interact, interactive,fixed
from ReportMagics import *


class WidgetInteractions():
    
	@staticmethod
    def gen_report(conf_md,conf_code, md, code, filename):
        ReportGeneration.write_report(conf_md, conf_code, md, code, report_name=filename)

    @staticmethod
    def translate_code_commands(cell, exported_cols, composite=False):
        new_code_store = []
        exported_cols = [each for each in exported_cols if each!='']
        for each in exported_cols:
            
            w,x,y = each.split(',')
            
            with open('log.txt','w') as fout:
                fout.write('Processing call for the column {}'.format(each))
            temp = cell[0]#.strip()

            new_line = temp.replace('interact','apply').replace(
                "df=fixed(df)","df").replace("filename=fixed(filename)","'"+ReportMagic.var_files+"'").replace(
                "col1=w1","'"+w+"'").replace("col2=w2","'"+x+"'").replace("col3=w3","'"+y+"'").replace(
                "Export=w_export","False").replace("conf_dict=fixed(conf_dict)","conf_dict")
            new_line = new_line.replace("df,","[df,")
            new_line = new_line[:len(new_line)-1]+"])"
    #         print 'New formatted code ', new_line
            new_code_store.append(new_line)
        return new_code_store  

    @staticmethod
    def trigger_report(widgets,export_cols_file, output_report, no_widgets=1, md_text=''):
        exported_cols = []
        with open(export_cols_file,'r') as fin:
            for each in fin:
                each = each.strip()
                if each and not each.isspace():
                    exported_cols.append(each)
            
        exported_cols = list(set(exported_cols))
        conf_md, conf_code, md, code = WidgetInteractions.show_report() 
        md = md_text
        cell = code
        new_code_store = WidgetInteractions.translate_code_commands(cell,exported_cols)
        WidgetInteractions.gen_report(conf_md,conf_code, md, new_code_store, filename=output_report)
        
    @staticmethod
    def silentremove(filename):
        try:
            os.remove(filename)
        except OSError as e: # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                raise # re-raise exception if a different error occured

    @staticmethod
    def handle_change( value):
    #     print 'Toggle Checkbox called'
        w_export.value = False
    
    @staticmethod
    def getWidgetValue(w):
        w_value = ''
        try:
            w_value = w.value
        except:
            pass
        return w_value

    @staticmethod
    def handle_export( widget, w1,w2,w3,log_filename, export_filename='temp.ipynb',md_text=''):
        if widget['new'] == True:
            w1_value,w2_value,w3_value = WidgetInteractions.getWidgetValue(w1),WidgetInteractions.getWidgetValue(w2),WidgetInteractions.getWidgetValue(w3)

                
            st = ','.join(str(each) for each in [w1_value, w2_value, w3_value])
            with open(log_filename,'a') as fout:
                fout.write(st+'\n')

            WidgetInteractions.trigger_report(w1_value,log_filename, export_filename, False,md_text=md_text)
            
    @staticmethod
    def target_interaction(conf_dict,md_text, log_filename, export_filename ):
        md_text = 'Target Variable'
        log_filename = 'tmp/target_variables.csv'
        export_filename = 'target_report2.ipynb'
        w1_value,w2_value,w3_value = '','',''
        w1, w2, w3, w4 = None, None, None, None
        WidgetInteractions.silentremove(log_filename)    
        w1 = widgets.Dropdown(
            options = [conf_dict['Target']],
            value = conf_dict['Target'],
            description = 'Target Variable:',
        )
        ReportMagic.var_files = log_filename
        w_export = widgets.widget_bool.Checkbox(description='Export', value=False, options=[True, False])
        handle_export_partial = partial(WidgetInteractions.handle_export, w1=w1,w2=w2,w3=w3,log_filename=log_filename,export_filename=export_filename, md_text=md_text)
                
        w1.observe(WidgetInteractions.handle_change,'value')
        w_export.observe(handle_export_partial)
        return w1, w2, w3,w4, w_export
        
    @line_magic,@needs_local_scope, @staticmethod
    def add_conf_line_to_report(self, line, cell=None,local_ns=None):
        """store the cell in the store"""
        if cell is None:
            cell =line
        self._code_store.append(cell)
        self._code_store = list(set(self._code_store))
        self.ip.run_cell(cell)
        return cell
    
    @staticmethod
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
    
    @staticmethod
    @line_magic
    def add_markdown_to_report(self, line):
        """store the cell in the store"""
        
        self._markdown_store.append(cell)

    @cell_magic
    @staticmethod
    @needs_local_scope
    def add_conf_code_to_report(self, line, cell):
        """store the cell in the store"""
        self._conf_code_store.append("\r\n")    
        self._conf_code_store.append(cell)    
        self.ip.run_cell(cell)

    @cell_magic
    @staticmethod
    def add_conf_markdown_to_report(self, line, cell):
        """store the cell in the store"""
        self._conf_markdown_store.append(cell)
       
    @line_magic
    @staticmethod
    def show_report(self,line):
        """show all recorded statements"""
        self._conf_markdown_store = ['# Configuration Code']
        self._markdown_store = ['## Target variable']
        return self._conf_markdown_store,self._conf_code_store ,self._markdown_store,self._code_store

    @line_magic
    @staticmethod
    def reset_report(self, line):
        self._markdown_store = []
        self._code_store = []

# This class must then be registered with a manually created instance,
# since its constructor has different arguments from the default:
ip = get_ipython()
magics = ReportMagic(ip, 0)
ip.register_magics(magics)
