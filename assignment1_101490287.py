# Author: Arshia Moradi
# Assignment: #1

# Define variables with comments for data types
gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25  # int
membership_active = True  # bool

# Define workout_stats dictionary

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 15),
    "Taylor": (40, 60, 30)
}


for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes


workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]


yoga_running_minutes = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_running_minutes)


weightlifting_minutes = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for the last two friends:", weightlifting_minutes)


for friend, total in [(key, value) for key, value in workout_stats.items() if "_Total" in key]:
    if total >= 120:
        friend_name = friend.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")


friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(f"{friend_name}'s workout minutes: Yoga: {yoga}, Running: {running}, Weightlifting: {weightlifting}. Total: {total}.")
else:
    print(f"Friend {friend_name} not found in the records.")


total_workouts = {key: value for key, value in workout_stats.items() if "_Total" in key}
max_friend = max(total_workouts, key=total_workouts.get).replace("_Total", "")
min_friend = min(total_workouts, key=total_workouts.get).replace("_Total", "")

print(f"Friend with highest total workout minutes: {max_friend}")
print(f"Friend with lowest total workout minutes: {min_friend}")