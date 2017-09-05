topology=[1, 2, 3, 4, 5]

bus_switch_count=[8, 16, 24, 32, 40]
bus_host_per_switch=[3]
bus_switch_link_speed=[4,8,16,32]
bus_hosst_link_speed=[10]

ring_switch_count=[8, 16, 24, 32, 40]
ring_host_per_switch=[3]
ring_switch_link_speed=[4,8,16,32]
ring_hosst_link_speed=[10]

mesh_switch_count=[4, 8, 12, 16]
mesh_host_per_switch=[3]
mesh_switch_link_speed=[4,8,16,32]
mesh_hosst_link_speed=[10]

star_host_count=[4,8,16,32]

random_switch_count=[8, 16, 24, 32, 40]
random_host_per_switch=[3]
random_total_count=dict(zip(random_switch_count, [12, 24, 36, 48, 60]))
random_switch_max_links=dict(zip(random_switch_count, [16, 32, 48, 64, 80]))
random_switch_link_speed=[4,8,16,32]
random_hosst_link_speed=[10]
random_stp_option=['T','F']

file_object=open("data_plane_test_cases.txt",'w')
if 1 in topology:
	for i in bus_switch_count:
		for j in bus_host_per_switch:
			for k in bus_switch_link_speed:
				for l  in bus_hosst_link_speed:
					line="'1' " + "'"+str(i)+"' "+"'"+str(j)+"' "+"'"+str(k)+"' "+"'"+str(l)+"'"
					file_object.write(line+"\n")
if 2 in topology:
	for i in ring_switch_count:
		for j in ring_host_per_switch:
			for k in ring_switch_link_speed:
				for l  in ring_hosst_link_speed:
					line="'2' " + "'"+str(i)+"' "+"'"+str(j)+"' "+"'"+str(k)+"' "+"'"+str(l)+"'"
					file_object.write(line+"\n")
if 3 in topology:
	for i in mesh_switch_count:
		for j in mesh_host_per_switch:
			for k in mesh_switch_link_speed:
				for l  in mesh_hosst_link_speed:
					line="'3' " + "'"+str(i)+"' "+"'"+str(j)+"' "+"'"+str(k)+"' "+"'"+str(l)+"' "+"'F'"
					file_object.write(line+"\n")
if 4 in topology:
	for i in star_host_count:
		line="'4' " + "'"+str(i)+"'"
		file_object.write(line+"\n")

if 5 in topology:
	for i in random_switch_count:
		for j in random_host_per_switch:
			for k in random_switch_link_speed:
				for l  in random_hosst_link_speed:
					for m in random_stp_option:
						line="'5' " + "'"+str(i)+"' "+"'"+str(j)+"' "+"'"+str(random_total_count[i])+"' "+"'"+str(random_switch_max_links[i])+"' "+"'"+str(k)+"' "+"'"+str(l)+"' "+"'"+str(m)+"'"
						file_object.write(line+"\n")
file_object.close()
