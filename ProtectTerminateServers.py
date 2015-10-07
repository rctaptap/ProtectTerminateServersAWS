import boto.ec2
regiones = ["us-east-1","us-west-1","us-west-2"]
for region in regiones:
	conn=boto.ec2.connect_to_region(region)	
	reservations = conn.get_all_instances()
	for res in reservations:		
		for inst in res.instances:
			atri = conn.get_instance_attribute(inst.id,'disableApiTermination')
			if str(atri) == "{u'disableApiTermination': False}":	
				if 'Name' in inst.tags:           	     
					print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, atri)
				else:
					print "%s [%s]" % (inst.id, inst.state, atri)		
				inst.modify_attribute('disableApiTermination', True)		

