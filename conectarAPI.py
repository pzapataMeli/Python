import requests

#Datos para la conexion a la API
user = "InternalSystems"
password ="s0SMDVvz36jl7ohi4kMgSHTm"
parametros = {"helpdesk_id": "424"}


#Conexion a la API
resp = requests.get('https://servicedesk.mercadolibre.com/api/v1/incidents.by.helpdesk?', params= parametros , auth= (user, password))
#si esta OK se guarda la informacion
if resp.status_code != 200:
	print "Error"
else:
	lista = {}	
	lista = resp.json()

#Almaceno la lista con los tickets de la mesa en otra lista
if lista.has_key('requestIds'):
	tickets = []
	tickets = lista['requestIds']
	for i in tickets:
		a = i
		parametros2 = {"id": a}
		sec = requests.get('https://servicedesk.mercadolibre.com/api/v1/incident', params= parametros2, auth = (user, password))
		lista2 = {}
		lista2 = sec.json()
		
		print lista2['category_id']
		print "---------------------------------------------"




