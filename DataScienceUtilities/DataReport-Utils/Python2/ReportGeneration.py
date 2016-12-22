class ReportGeneration:
    @staticmethod
    def write_report(  conf_markdown_store,conf_code_store, markdown_store,code_store, report_name='my_notebook.ipynb'):
        
        #print 'code_store', code_store
        from nbformat import current as nbf
        nb = nbf.new_notebook()
        cells = []

        # Write conf markdown
        text = ''.join(each for each in conf_markdown_store)
        conf_markdown_cell = nbf.new_text_cell('markdown', text)
        cells.append(conf_markdown_cell)

        # Write conf code
        text = ''.join(each for each in conf_code_store)
        conf_code_cell = nbf.new_code_cell( text)
        cells.append(conf_code_cell)


        # Write main/report markdown
        text = ''.join(each for each in markdown_store)
        report_markdown = nbf.new_text_cell('markdown', text)
        cells.append(report_markdown)

        # Write main /report code
        if code_store:
            for each in code_store:
                text = '\r\n'+each
                report_code = nbf.new_code_cell( text)
                cells.append(report_code)
        nb['worksheets'].append(nbf.new_worksheet(cells=cells))
        # Writing to the notebook
        with open(report_name, 'w') as f:
                nbf.write(nb, f, 'ipynb')

                