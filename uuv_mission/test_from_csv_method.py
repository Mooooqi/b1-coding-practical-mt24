import sys
import os

# Add the directory that contains 'uuv_mission' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from uuv_mission.dynamic import Mission  # Adjust the import based on your file structure

# Test the from_csv method
mission = Mission.from_csv('data/mission.csv')

# Print out the mission data to verify
print("Reference Trajectory:")
print(mission.reference)

print("\nCave Height (Upper Boundary):")
print(mission.cave_height)

print("\nCave Depth (Lower Boundary):")
print(mission.cave_depth)
