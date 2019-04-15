mport os
c = get_config()
c.NbConvertApp.export_format = 'pdf'
c.TemplateExporter.template_path = ['.', os.path.expanduser('~/.jupyter/templates/')]
c.Exporter.template_file = 'mytemplate'
