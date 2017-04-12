# _*_ coding:utf-8 _*_
import web
import web.db
import sae.const

db = web.database(
    dbn='mysql',
    host=sae.const.MYSQL_HOST,
    port=int(sae.const.MYSQL_PORT),
    user=sae.const.MYSQL_USER,
    passwd=sae.const.MYSQL_PASS,
    db=sae.const.MYSQL_DB
)
 
    
    
def checkName(username,password):
	try:
		a = list(db.select('login',where=('username='+username)))
		return a
	except:
		return 'error'
def addfk(time, numOfRoom,pm25,pm10,tem,dam,co2):
    return db.update('fk1',where='id=$id',vars={'id':(int)(numOfRoom)},time=time, numOfRoom=numOfRoom, pm25=pm25,pm10=pm10,tem=tem,dam=dam,co2=co2)

def addfk1(time,pm25,pm10,tem,dam,co2):
    return db.insert('fk2',time=time, pm25=pm25,pm10=pm10,tem=tem,dam=dam,co2=co2) 
def addfk2(time,pm25,pm10,tem,dam,co2):
    return db.insert('fk3',time=time, pm25=pm25,pm10=pm10,tem=tem,dam=dam,co2=co2) 
def addfk3(time,pm25,pm10,tem,dam,co2):
    return db.insert('fk4',time=time, pm25=pm25,pm10=pm10,tem=tem,dam=dam,co2=co2) 
def addfk4(time,pm25,pm10,tem,dam,co2):
    return db.insert('fk5',time=time, pm25=pm25,pm10=pm10,tem=tem,dam=dam,co2=co2) 
def addfk5(time,pm25,pm10,tem,dam,co2):
    return db.insert('fk6',time=time, pm25=pm25,pm10=pm10,tem=tem,dam=dam,co2=co2)
def delete_all():
	db.query("TRUNCATE TABLE  `fk2`")
	db.query("TRUNCATE TABLE  `fk3`")
	db.query("TRUNCATE TABLE  `fk4`")
	db.query("TRUNCATE TABLE  `fk5`")
	db.query("TRUNCATE TABLE  `fk6`")

def get_fkcontent():
    return db.select('fk1')

def get_time(numOfRom):
	if numOfRom=='1':
		return db.select('fk2',what='time')
	elif numOfRom=='2':
		return db.select('fk3',what='time')
	elif numOfRom=='3':
		return db.select('fk4',what='time')
	elif numOfRom=='4':
		return db.select('fk5',what='time')
	elif numOfRom=='5':
		return db.select('fk6',what='time')
def get_co2(numOfRom):
	if numOfRom=='1':
		return db.select('fk2',what='co2')
	elif numOfRom=='2':
		return db.select('fk3',what='co2')
	elif numOfRom=='3':
		return db.select('fk4',what='co2')
	elif numOfRom=='4':
		return db.select('fk5',what='co2')
	elif numOfRom=='5':
		return db.select('fk6',what='co2')
def get_pm10(numOfRom):
	if numOfRom=='1':
		return db.select('fk2',what='pm10')
	elif numOfRom=='2':
		return db.select('fk3',what='pm10')
	elif numOfRom=='3':
		return db.select('fk4',what='pm10')
	elif numOfRom=='4':
		return db.select('fk5',what='pm10')
	elif numOfRom=='5':
		return db.select('fk6',what='pm10')
def get_pm25(numOfRom):
	if numOfRom=='1':
		return db.select('fk2',what='pm25')
	elif numOfRom=='2':
		return db.select('fk3',what='pm25')
	elif numOfRom=='3':
		return db.select('fk4',what='pm25')
	elif numOfRom=='4':
		return db.select('fk5',what='pm25')
	elif numOfRom=='5':
		return db.select('fk6',what='pm25')
def get_tem(numOfRom):
	if numOfRom=='1':
		return db.select('fk2',what='tem')
	elif numOfRom=='2':
		return db.select('fk3',what='tem')
	elif numOfRom=='3':
		return db.select('fk4',what='tem')
	elif numOfRom=='4':
		return db.select('fk5',what='tem')
	elif numOfRom=='5':
		return db.select('fk6',what='tem')
def get_dam(numOfRom):
	if numOfRom=='1':
		return db.select('fk2',what='dam')
	elif numOfRom=='2':
		return db.select('fk3',what='dam')
	elif numOfRom=='3':
		return db.select('fk4',what='dam')
	elif numOfRom=='4':
		return db.select('fk5',what='dam')
	elif numOfRom=='5':
		return db.select('fk6',what='dam')
