import requests

#Datos para la conexion a la API
user = "InternalSystems"
password ="s0SMDVvz36jl7ohi4kMgSHTm"
parametros = {"helpdesk_id": "424"}


#Conexion a la API
resp = requests.get('https://servicedesk.mercadolibre.com/api/v1/incidents.by.helpdesk?', params= parametros , auth= (user, password)) #Listamos todos los tickets de la mesa
#si esta OK se guarda la informacion
if resp.status_code != 200:
	print "Error"
else:
	lista = {}	
	lista = resp.json()['requestIds'] #Guardo la informacion en un json y solicito el ID de los tickets

for i in lista: #empiezo a iterar en mis tickets
	tktOpen = requests.get('https://servicedesk.mercadolibre.com/api/v1/incident?id=' + i, auth= (user, password))
	tktCat = tktOpen.json()['category_id'] #Categoria de los tickets
	tktDes = tktOpen.json()['description'] #Descripcion de los tickets
	tktId = tktOpen.json()['id'] #ID de los tickets
	if tktCat == "904":
		print tktDes
#print "Hola Mundo!"
























