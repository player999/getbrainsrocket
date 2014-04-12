#!/usr/bin/python3

#Call example ./test_flight.py [[0,500],[8,250],[20,150],[26,100],[50,95],[53,3.5],[70,7],[91.69,457.47],[200,0]]
import urllib.request
import sys

def print_waypoints(waypoints):
	#{"mass":89950.0,"time":0.0,"altitude":0.0,"velocity":6.865931072818234E-4,"thrust":500.0,"acceleration":0.6998910369845294}
	waypoints = eval(waypoints)
	wp = waypoints["waypoints"]
	rocket_log = open("rocket_log","w")
	rocket_log.write("time\tmass\taltitude\tvelocity\tthrust\tacceleration\n")
	for entry in wp:
		print("mass: %f"%entry["mass"]) 
		print("time: %f"%entry["time"]) 
		print("altitude: %f"%entry["altitude"]) 
		print("velocity: %f"%entry["velocity"]) 
		print("thrust: %f"%entry["thrust"]) 
		print("acceleration: %f"%entry["acceleration"]) 
		print("\n")
		rocket_log.write("%f\t%f\t%f\t%f\t%f\t%f\n"%(entry["time"], entry["mass"], entry["altitude"], entry["velocity"], entry["thrust"], entry["acceleration"]))
	rocket_log.close()

	#"state":"OVERLOAD","score":0,"position":-1
	print("STATE: %s"%waypoints["state"])	
	print("SCORE: %f"%waypoints["score"])
	print("POSITION: %f"%waypoints["position"])


if __name__=="__main__":
#[[0,500],[8,250],[20,150],[26,100],[50,95],[53,3.5],[70,7],[91.69,457.47],[200,0]]
	response = urllib.request.urlopen("http://rckt.jetbrains.com/compute.jsp", bytes(sys.argv[1],"ascii"))
	#response = urllib.request.urlopen("http://rckt.jetbrains.com/compute.jsp", bytes("[[0,500],[8,250],[20,150],[26,100],[50,95],[53,3.5],[70,7],[91.69,457.47],[200,0]]","ascii"))
	print_waypoints(response.read())
	
