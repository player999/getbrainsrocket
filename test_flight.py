#!/usr/bin/python3

#Call example ./test_flight.py [[0,500],[8,250],[20,150],[26,100],[50,95],[53,3.5],[70,7],[91.69,457.47],[200,0]]
import urllib.request
import sys
import subprocess

PLOT_CMD = "gnuplot -e \"%s pause -1\""

MAS="set term x11 %d; plot 'rocket_log' using 1:2 with lines; set xlabel 'time'; set ylabel 'mass'; "
ALT="set term x11 %d; plot 'rocket_log' using 1:3 with lines; set xlabel 'time'; set ylabel 'altitude'; "
VEL="set term x11 %d; plot 'rocket_log' using 1:4 with lines; set xlabel 'time'; set ylabel 'velocity'; "
THR="set term x11 %d; plot 'rocket_log' using 1:5 with lines; set xlabel 'time'; set ylabel 'thrust'; "
ACC="set term x11 %d; plot 'rocket_log' using 1:6 with lines; set xlabel 'time'; set ylabel 'acceleration'; "

def make_plot(plot_list):
	pline = ""
	for i in range(0, len(plot_list)):
		pline = pline + (plot_list[i])%i
	plot_req = PLOT_CMD%pline
	subprocess.call(plot_req, shell=True)

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
	#MAS ALT VEL THR ACC
	make_plot([MAS,ALT])
