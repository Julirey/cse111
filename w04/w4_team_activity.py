# w04 team activity - tin can
import math
 
def main():
    can_number = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.50, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
  
    
    # for loop to print each value
    for name in range(len(can_number)):
        volume = compute_volume(radius[name], height[name])
        # print(f"{volume:.2f}")
        surface_area = compute_surface_area(radius[name], height[name])
        # print(f"{surface_area:.2f}")
        storage_efficency = volume / surface_area
        print(f"{can_number[name]} {storage_efficency:.2f}")
  
# this function computes the volume of the can
def compute_volume(radius, height):
    volume = math.pi * radius **2 * height
    return volume
 
# this function compuites the surface area of the can
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area
 
main()