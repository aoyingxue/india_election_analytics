import os

os.chdir(os.path.join(os.getcwd(),"pdf"))
filepath=os.listdir()

from pylovepdf.ilovepdf import ILovePdf

ilovepdf = ILovePdf('project_public_6b7702959947cac2ffb4f1c9d9e6828a_a_bN4ea03f4a266a23f67543c3dbc432b2df5',
                    verify_ssl=True)
for file in filepath:
    task = ilovepdf.new_task('compress')
    task.add_file('pdf_file')
    task.set_output_folder('output_directory')
    task.execute()
    task.download()
    task.delete_current_task()



### lib not working
# import pdftables_api
# c = pdftables_api.Client('jmpout8adc0z')
# for file in filepath:
#     print(file)
#     c.xlsx(file, file.replace("pdf","xlsx"))
# #replace c.xlsx with c.csv to convert to CSV
# #replace c.xlsx with c.xml to convert to XML
# #replace c.xlsx with c.html to convert to HTML

