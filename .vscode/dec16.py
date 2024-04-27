class Exercise:
    def __init__(self, name):
        self.name = name
        self.repetitions = 0

    def do_exercise(self, reps):
        self.repetitions += reps

class ExerciseApp:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def display_exercises(self):
        print("Available exercises:")
        for idx, exercise in enumerate(self.exercises, start=1):
            print(f"{idx}. {exercise.name}")

    def start(self):
        while True:
            print("\nWelcome to the Exercise App!")
            self.display_exercises()
            choice = input("Enter the number of the exercise you want to do (or 'q' to quit): ")

            if choice.lower() == 'q':
                break

            try:
                exercise_idx = int(choice) - 1
                if 0 <= exercise_idx < len(self.exercises):
                    reps = int(input("Enter the number of repetitions: "))
                    self.exercises[exercise_idx].do_exercise(reps)
                    print(f"You have completed {reps} reps of {self.exercises[exercise_idx].name}.")
                else:
                    print("Invalid exercise number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    app = ExerciseApp()
    
    # Adding exercises
    push_ups = Exercise("Push-ups")
    squats = Exercise("Squats")
    jumping_jacks = Exercise("Jumping Jacks")

    app.add_exercise(push_ups)
    app.add_exercise(squats)
    app.add_exercise(jumping_jacks)

    # Starting the exercise app
    app.start()