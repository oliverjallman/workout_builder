# I'm not a personal trainer
# It costs me mental energy to plan a workout
# So I want to automate it 
# I have a structure the workouts should follow
# Other than that, I dont care
# This program is going to build my workouts for me

import random

compound_list = ["Squats", "Deadlift"]
full_list = ["Cleans", "Burpees", "Overhead Dumbell Lunge"]
legs_list = ["Pistol Squat", "Side Lunges", "Romanian Deadlift", "Barbell Lunges"]
press_list = ["Shoulder Press", "Arnold Press", "Incline Press Ups", "Side Raises", "Incline Bench", "Dumbell Bench", "Bench"]
pull_list = ["Barbell Row", "Pull Ups", "Cable Row", "Rear Delt Flys"]
core_list = ["Leg Up Row", "Hanging Leg Raises", "Romanian Twist"]

list_of_list = [compound_list, full_list, legs_list, press_list, pull_list, core_list]

def workout_randomiser (list_of_list):
    index = 0
    workout_selection = []
    for list in list_of_list:
        workout_selection.append(random.choice(list))
        index += 1
    
    return workout_selection


def workout_builder (list):
    workout = "5x5: " + list[0] + "\n30s: " + list[1] + " 30s: " + list[2] + " 30s Rest " + "\nSuperset: " + list[3] + " " + list[4] + "\nSuperset " + list[5]
    return workout

workout_selection = workout_randomiser(list_of_list)
print(workout_builder(workout_selection))
