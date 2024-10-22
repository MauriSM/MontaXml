import csv

f = open(r'C:\Users\mauricio.magalhaes\Downloads\ref_Status_voos_mod.CSV')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
    data.append(row)

f.close()
indice = int(len(data)*2)
print (indice)
def convert_row(row):
    
    return """<TranslationBE>
        <Id>%s</Id>
        <StatusCode>%s</StatusCode>
        <Language>en-US</Language>
        <Description>%s</Description>
    </TranslationBE>
    <TranslationBE>
        <Id>%s</Id>
        <StatusCode>%s</StatusCode>
        <Language>pt-BR</Language>
        <Description>%s</Description>
    </TranslationBE>""" % (row[0], row[1], row[3], row[0], row[1], row[4])
    

with open(r'C:\Wcf\CodesTranslations_novo.xml', 'w') as f: f.write('\n'.join([convert_row(row) for row in data[1:]]))

