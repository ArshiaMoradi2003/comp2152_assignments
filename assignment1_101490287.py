# Author: Arshia Moradi
# Assignment: #1


# Define variables for datatypes
gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True

# Dictionary:
workout_stats = {
    "Alex":(30,45,20),
    "Jamie":(25,50,15),
    "Taylor":(40,60,30)
}

# Loop through dictionary and calculate total workout minutes for each friend
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_total"] = total_minutes

# Create 2D list (nested list) from dictionary values
workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

# Extract and print yoga and running minutes for all friends
yoga_running_minutes = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:" , yoga_running_minutes)
# Extract and print weightlifting minutes for the last two friends
weightlifting_minutes = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for the last two friends:", weightlifting_minutes)

# Check if any friend has total workout minutes >=120
for friend, total in workout_stats.items():
    if isinstance(total, int) and total >= 120:
        print(f"Great job staying active, {friend}!")

# Allow user to input a friend's name and display workout details
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    print(f"Workout details for {friend_name}: Yoga: {workout_stats[friend_name][0]} min, "
          f"Running: {workout_stats[friend_name][1]} min, "
          f"Weightlifting: {workout_stats[friend_name][2]} min, "
          f"Total: {workout_stats[f'{friend_name}_Total']} min")
else:
    print(f"Friend {friend_name} not found in the records.")