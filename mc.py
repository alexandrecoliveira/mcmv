import json
from urllib.request import urlopen

url = "https://geoservicos.inde.gov.br/geoserver/wms?service=WFS&version=1.0.0&request=GetFeature&typeName=MPOG:MCMV&outputFormat=JSON"
json_url = urlopen(url)
data = json.loads(json_url.read())

nomeArq = "mcmv_in_.csv"
arqCriado = open(nomeArq, "w+")	#Cria o arquivo no diretório atual

uf = ""
ibge = ""
capitais = ""
municipio = ""
uf1 = ""
faixa_de_r = ""
produto = ""
uh = ""
valor = ""
concluidas = ""
entregues = ""
sub_fgts = ""
sub_ogu = ""
iff = ""
faixa = ""
uh_conc = ""
x_coord = ""
y_coord = ""

#Escreve o cabeçalho do arquivo
arqCriado.write('uf,ibge,capitais,municipio,uf1,faixa_de_r,produto,uh,valor,concluidas,entregues,sub_fgts,sub_ogu,iff,faixa,uh_conc,x_coord,y_coord' + '\n')

for feature in data['features']:
	uf = feature['properties']['UF']
	ibge = feature['properties']['COD_IBGE']
	capitais = feature['properties']['CAPITAIS'] 	
	municipio = feature['properties']['Municipio']
	uf1 = feature['properties']['UF_1']
	faixa_de_r = feature['properties']['Faixa_de_r']
	produto = feature['properties']['Produto']
	uh = feature['properties']['UH']
	valor = feature['properties']['Valor']
	concluidas = feature['properties']['Concluidas']
	entregues = feature['properties']['Entregues']
	sub_fgts = feature['properties']['Sub_FGTS']
	sub_ogu = feature['properties']['Sub_OGU']
	iff = feature['properties']['IF']
	faixa = feature['properties']['Faixa']
	uh_conc = feature['properties']['UH_CONC']
	x_coord = feature['properties']['XCOORD']
	y_coord = feature['properties']['YCOORD']
	arqCriado.write(str(uf) + ',' + str(ibge) + ',' + str(capitais) + ',' + str(municipio) + ',' + str(uf1) + ',' + str(faixa_de_r) + ',' + str(produto) + ',' + str(uh) + ',' + str(valor) + ',' + str(concluidas) + ','  + str(entregues) + ',' + str(sub_fgts) + ',' + str(sub_ogu) + ',' + str(iff) + ',' + str(faixa) + ',' + str(uh_conc) + ',' + str(x_coord) + ',' + str(y_coord) + '\n')

arqCriado.close()
print("OK")