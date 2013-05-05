import web

from schedule.monsched import MonitorSchedule
from config.yamlmonbox import YamlMonitorBox
	
class s_index:
	def GET(self):
		monitors = globals()['schedule'].monitors()
		render = web.template.render('../web/')
		return render.home(monitors)


class s_web:
	def GET(self):
		return "Hello world!"
	
class s_report:
	def GET(self):
		return "Hello world!"

class s_api:
	def GET(self):
		return "this is my: "+str(globals()['schedule'].monitor('monitor1').myName())

class TinyWeb:
	def __init__(self):
		self.app = web.application(self.__urls(), globals(), True)
		global schedule
		schedule = MonitorSchedule()		
		schedule.registeMonitors(YamlMonitorBox('conf/monitor.yaml').monitors());
		schedule.go()

	def __urls(self):
		return (
			'/','s_index',
			'/web', 's_web'
			'/api', 's_api'
			'/report', 's_report'
		)

	def start(self):
		self.app.run()

if __name__ == "__main__": 
	w = TinyWeb()
	w.start()