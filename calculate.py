import numpy
def getDragForce(capacity, distance):
    work = capacity * 3600 # Watt Hours to Joules
    return work / distance # f = w/d

g=9.8 # ms^-2
print("### Welcome to EV Commute Calculator ###")
print("Battery Capacity (in Wh): ")
batteryCapacity = float(input())
print("Vehicle Range (in km): ")
range = float(input())*1000 # Convert km to m
print("Gross Vehicle Weight (in kg): ")
weight = float(input())
drag_force = getDragForce(batteryCapacity, range) # in Newtons
g_force = weight * g # in Newtons
print("   Calculated mean drag: " +str(format(drag_force/weight, '.2f')) +"ms^-2")
print("   Calculated mean drag force: " +str(format(drag_force, '.2f')) +"N")
print("   Calculated mean force due to gravity: " +str(format(g_force, '.2f')) +"N")
print("----------------------------------------")
print("Trip distance: (in km): ")
delta_x = float(input()) * 1000 # Horizontal Distance in m
print("Net Change in Elevation (in m): ")
delta_y = float(input()) # Change in Vertical Elevation in m
g_work = g_force * delta_y
drag_work = drag_force * (delta_x + delta_y) # drag force times maximum possible distance travelled (assuming right angle travel gradient)
watt_hours = (g_work+drag_work) / 3600 # convert Joules to Watt Hours
print("   Work done against Gravity: " + str(format(g_work, '.2f')) + "J")
print("   Work done against Drag: " + str(format(drag_work, '.2f')) + "J")
print("   Energy usage in Watt Hours: " + str(format(watt_hours, '.2f')) + "Wh")
print("   Percentage of capacity: " + str(format((watt_hours/batteryCapacity)*100, '.2f')) +"%")
print("----------------------------------------")
