#%%add_conf_code_to_report

import collections
import types

try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring

from six import string_types
	
from IPython.core.display import HTML
from IPython.display import display

class ConfUtility():
	@staticmethod
	def write_conf_to_file(workingDir, data_file, conf_file):
		with open('tmp/conf_file.txt','w') as fout:
			fout.write('workingDir={}\n'.format(workingDir))
			fout.write('data_file={}\n'.format(data_file))
			fout.write('conf_file={}\n'.format(conf_file))
			
	@staticmethod
	def read_conf_from_file(input_file='tmp/conf_file.txt'):
		with open(input_file) as fin:
			for each_line in fin:
				k, v = each_line.split('=')
				k, v = k.strip(), v.strip()
				if k == 'workingDir':
					workingDir = v
				elif k == 'data_file':
					data_file = v
				else:
					conf_file = v

		return workingDir, data_file, conf_file

	@staticmethod
	def parse_yaml(input_file):

		import yaml
		yaml_dict = {}
		with open (input_file,'r') as fin:
			try:
				yaml_dict = yaml.load(fin)
			except Exception as ex:
				print (ex)
		return yaml_dict
	
	@staticmethod
	def dict_to_htmllist(dc, include_list=None):
		dc2 = {}
		output_formatting = {'Target':'Target variable is ','CategoricalColumns':'Categorical Columns are ',
						   'NumericalColumns':'Numerical Columns are '}
		for each in dc.keys():
			if not include_list or each in include_list:
				if isinstance(dc[each],  collections.Iterable) and not isinstance(dc[each], str):
					dc2[each] = ', \n'.join(val for val in dc[each])
				else:
					dc2[each] = dc[each]		
		html_list = "<ul>{}</ul>"
		html_list_entry = "<li>{}</li>"
		output3 = ''

		for each in set(include_list)|set(dc2.keys()):
			output3 += html_list_entry.format(output_formatting[each]+dc2[each])
		html_list = html_list.format(output3)
		return HTML(html_list)