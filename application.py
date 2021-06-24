from flask import Flask, render_template, request
from helpers import create_basic_routine, create_personalized_routine

predef_routines = ['Full body', 'Push', 'Pull', 'Legs']

muscles_list = ['Chest', 'Triceps', 'Lats', 'Traps', 'Neck', 'Shoulders', 
                'Middle back', 'Lower back', 'Biceps', 'Forearms',
                'Abdominals', 'Quadriceps', 'Hamstrings', 'Glutes', 
                'Calves', 'Adductors', 'Abductors', 'Aerobic']

number_ex_list = ['Chest_n', 'Triceps_n', 'Lats_n', 'Traps_n', 'Neck_n', 
                  'Shoulders_n', 'Middle back_n', 'Lower back_n', 'Biceps_n',
                  'Forearms_n', 'Abdominals_n', 'Quadriceps_n', 'Hamstrings_n',
                  'Glutes_n', 'Calves_n', 'Adductors_n', 'Abductors_n', 'Aerobic_n']

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])

def index():
    if request.method == 'POST':
        
        if request.form.get('action') == 'Generate Predefined Workout':
            
            routine_selected = []
            for selected in predef_routines:
                if request.form.get(selected) == 'on':
                    routine_selected.append(selected)
                
                user_routine = create_basic_routine(routine_selected)
                routine = zip(routine_selected, user_routine)
                
                try:
                    sets = request.form.get('sets')
                    reps = request.form.get('reps')
                except:
                    pass

            if not (user_routine == [] or sets is None or reps is None):                
                return render_template('workout.html', 
                                       routine=routine, 
                                       sets=sets, 
                                       reps=reps)
        
        if request.form.get('action') == "Generate Personalized Workout":
            personalized = []
            
            for i in range(len(muscles_list)):
               
                muscle_check = request.form.get(muscles_list[i])
                if muscle_check is None:
                    continue
                
                try:
                    number_exercises = int(request.form.get(number_ex_list[i]))
                except:
                    continue
            
                if not (number_exercises >= 1 and number_exercises <= 8):
                    continue
                
                personalized.append((muscles_list[i], number_exercises))
            
            try:           
                sets = request.form.get('sets')
                reps = request.form.get('reps')   
            except:
                    pass
            
            if not (personalized == [] or sets is None or reps is None):
                
                routine_personalized = create_personalized_routine(personalized)
                routine_name = [request.form.get('routine_name')]
                routine = zip(routine_name, routine_personalized)
                
                return render_template('workout.html', 
                                        routine=routine,
                                        routine_name=routine_name, 
                                        reps=reps,
                                        sets=sets)
            
        
    return render_template('index.html', 
                           muscles_list=muscles_list, 
                           predef_routines=predef_routines, 
                           number_ex_list=number_ex_list)


if __name__ == "__main__":  
    app.run()
    