import sqlite3
import random

def check_input(input_routine):
        selected = input_routine
        if selected in ['Full body', 'Push', 'Pull', 'Legs', 'Abductors',
                        'Chest', 'Glutes', 'Triceps','Traps', 'Calves',
                        'Quadriceps', 'Lower back', 'Neck','Middle back',
                        'Lats', 'Shoulders', 'Adductors', 'Abdominals',
                        'Biceps', 'Forearms', 'Hamstrings']:
            return selected
        
        
def get_exercise(force):
    connect = sqlite3.connect('database/exercises-data.db')
    db = connect.cursor()
    
    db.execute('''SELECT exercise muscle_name FROM exercises
               INNER JOIN muscles USING (muscle_id)
               WHERE muscle_name = ?''', [force])    
    
    exercises = db.fetchall()
    exercise = random.choice(exercises)[0]
    
    db.close()
    return exercise


def full():
    exercises = [] #[('Full Body Day','3 sets x 8~12 reps')]
    for target in ['Middle back', 'Lower back', 'Chest', 'Chest',
                   'Hamstrings', 'Quadriceps', 'Calves', 'Shoulders', 
                   'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises
    

def push():
    exercises = [] # [('Push Day','3 sets x 8~12 reps')]
    for target in ['Middle back', 'Middle back', 'Lower back', 'Lower back', 
                   'Lats', 'Biceps', 'Biceps', 'Forearms', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises


def pull():
    exercises = [] # [('Pull Day','3 sets x 8~12 reps')]
    for target in ['Chest', 'Chest', 'Chest', 'Triceps', 'Triceps', 
                   'Shoulders', 'Shoulders', 'Traps', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises


def legs():
    exercises = [] #[('Legs Day','3 sets x 8~12 reps')]
    for target in ['Hamstrings', 'Hamstrings', 'Quadriceps', 'Quadriceps',
                   'Adductors', 'Abductors', 'Glutes', 'Glutes', 'Calves']:
        exercises.append((get_exercise(target), target))
    return exercises


def create_basic_routine(routine):
    exercises = []
    for i in routine:
        user = check_input(i)
        
        if user == 'Full body':
            exercises = [full()]
            
        elif user == 'Push':
            exercises.append(push())
      
        elif user == 'Pull':
            exercises.append(pull())
            
        elif user == 'Legs':
            exercises.append(legs())
      
    return exercises


def create_personalized_routine(routine):
    targets = []
    for (muscle, times) in routine:
        targets += ([muscle] * times)

    exercises = []
    for target in targets:
        while True: 
            exercise = get_exercise(target)
            
            if not exercise in exercises:
                break
            
            elif target == 'Aerobic':
                if all([x in exercises for x in ['Rowing', 'Running', 'Walking']]):
                    exercise = 'Only 3 exercises available'
                    break
            
        exercises.append(exercise)
    
    exercises = zip(exercises, targets)
    return [exercises]
