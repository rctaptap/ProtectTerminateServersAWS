#===================================================
#07102015 by Roberto Carlos Reyes Fernandez @rctaptap
#====================================================

import boto.ec2
regiones = ["us-east-1","us-west-1","us-west-2","ap-northeast-1","ap-southeast-1","ap-southeast-2","eu-central-1","eu-west-1","sa-east-1"]
for region in regiones:
	conn=boto.ec2.connect_to_region(region)	
	reservations = conn.get_all_instances()
	for res in reservations:		
		for inst in res.instances:
			atri = conn.get_instance_attribute(inst.id,'disableApiTermination')
			if str(atri) == "{u'disableApiTermination': False}":	
				if 'Name' in inst.tags:           	     
					print "%s (%s) [%s] [%s]" % (inst.tags['Name'], inst.id, atri, inst.region)
				else:
					print "%s [%s] [%s]" % (inst.id, inst.state, atri, inst.region)		
				inst.modify_attribute('disableApiTermination', True)		

