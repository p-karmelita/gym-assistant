class ExerciseManager:
    def __init__(self):
        self.exercise_dict = self.exercises()

    @staticmethod
    def exercises():
        exercise_dict = {
            'quadriceps': ['Reverse lunges with barbell', 'Dumbbell split squat', 'Front squat', 'Dumbbells squat',
                           'Dumbbells lunges', 'Smith machine squat', 'Barbell lunges', 'Back squat',
                           'Reverse lunges with dumbbells'],
            'hamstrings_glutes': ['Hip adduction machine', 'Kickback machine', 'Elevated deadlift',
                                  'Stiff leg deadlift', 'Sumo deadlift', 'Barbell glute bridge', 'Barbell hip thrust',
                                  'Romanian deadlift'],
            'back': ['Deadlift', 'Bent over barbell row', 'Pull ups', 'Chin ups', 'Behind the head pull ups',
                     'Landmine row neutral grip', 'Single arm landmine row', 'T-bar row', 'Seated cable row',
                     'Lat pulldown wide grip', 'Lat pulldown behind the head', 'Bent over dumbbells row',
                     'Bent over row – Smith machine', 'Bent over barbell row – underhand grip', 'Barbell shrugs',
                     'Dumbbell shrugs', 'Dumbbell row – hand supported on bench', 'Bent over barbell row'],
            'chest': ['Decline barbell bench press', 'Dumbbell floor press', 'Dumbbell pullover', 'Low cable chest fly',
                      'Decline dumbbells bench press', 'Push ups', 'Dumbbells chest fly', 'Cable chest fly',
                      'Pec dec fly', 'Dips – chest version', 'Incline dumbbell bench press',
                      'Incline bench dumbbells chest fly', 'Hammer chest press', 'Barbell bench press',
                      'Incline barbell bench press', 'Dumbbells bench press'],
            'shoulders': ['Powell raise', 'T raise', 'Behind the neck overhead press', 'Seated overhead press',
                          'Smith machine shoulder press', 'Arnold press', 'Upright barbell row', 'Lateral raise',
                          'Front raise', 'Military press', 'Seated overhead dumbbell press', 'Bent-over raise'],
            'abdominal_muscles': ['Crunches', 'Reverse crunches', 'Leg raises', 'Plank', 'Side plank',
                                  'Russian twist', 'Cable crunch'],
            'triceps': ['Dumbbell triceps extension', 'Cable rope triceps extension', 'Bench press close grip',
                        'Dumbbell skull crusher', 'Dips – triceps version', 'Overhead dumbbell triceps extension',
                        'Skull crusher', 'Cable bar triceps extension underhand grip', 'Diamond push ups'],
            'biceps': ['Reverse barbell biceps curl', 'Preacher hammer curl', 'Preacher dumbbell curl',
                       'Dumbbell supinated biceps curls', 'Hammer curl', 'EZ bar preacher curls', 'EZ bar biceps curls',
                       'Concentration curl', 'Barbell biceps curl'],
            'calves': ['Seated calf raise machine', 'Seated barbell calf raise', 'Smith machine calf raise']
        }
        return exercise_dict

    def get_exercise(self):
        muscle_groups = {
            '1': 'quadriceps',
            '2': 'hamstrings glutes',
            '3': 'back',
            '4': 'chest',
            '5': 'shoulders',
            '6': 'abdominal muscles',
            '7': 'triceps',
            '8': 'biceps',
            '9': 'calves'
        }

        print('Choose the muscle group to train:')
        for num, muscle_group in muscle_groups.items():
            print(f'{num}. {muscle_group.capitalize()}')

        while True:
            muscle_group_input = input('Please choose a number between 1 and 9: ')
            try:
                int_input = int(muscle_group_input)
                if 1 <= int_input <= 9:
                    break
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        muscle_group = muscle_groups.get(muscle_group_input)

        if muscle_group:
            print(f'Available exercises for {muscle_group}:')
            for exercise in self.exercise_dict[muscle_group]:
                print(exercise)
        return muscle_group

exercise_manager = ExerciseManager()
exercise_manager.get_exercise()
