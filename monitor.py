#!/usr/bin/env python

import psutil
import datetime
import time
import pprint

wait_time = 2
possible_ops = ['cpu', 'mem', 'network']
ops = ['cpu', 'mem', 'disk', 'sys', 'proc']

pp = pprint.PrettyPrinter(indent=4)

while True:
	result = {}
	result['datetime'] = str(datetime.datetime.now())

	if 'cpu' in ops:
		result['cpu_times'] = psutil.cpu_times()
		result['cpu_percent'] = psutil.cpu_percent()

	if 'mem' in ops:
		result['virtual_memory'] = psutil.virtual_memory()
		result['swap_memory'] = psutil.swap_memory()

	if 'disk' in ops:
		result['disk_usage'] = psutil.disk_usage('/')
		result['disk_io_counters'] = psutil.disk_io_counters()

	if 'net' in ops:
		result['net_io_counters'] = psutil.net_io_counters()
		result['net_connections'] = psutil.net_connections()
		result['net_if_addrs'] = psutil.net_if_addrs()
		result['net_if_stats'] = psutil.net_if_stats()

	if 'sensor' in ops:
		result['sensors_temperatures'] = psutil.sensors_temperatures()
		result['sensors_fans'] = psutil.sensors_fans()
		result['sensors_battery'] = psutil.sensors_battery()

	if 'sys' in ops:
		result['boot_time'] = psutil.boot_time()
		result['users'] = psutil.users()

	if 'proc' in ops:
		#result['pids'] = psutil.pids()
		procs = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username', 'pid'])}
		result['procs'] = procs

	pp.pprint(result)
	time.sleep(wait_time)
