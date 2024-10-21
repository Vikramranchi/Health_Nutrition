

# Create your views here.
# from django.shortcuts import render
# from .models import Food



from django.shortcuts import render

def homepage(request):
    return render(request, 'Nutrition/homepage.html') 

 # This renders your homepage template
def healthy_calories(request):
    return render(request, 'Nutrition/healthy-calories.html')
def bmi_calculator(request):
    if request.method == 'POST':
        # Get height and weight from the form
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))

        # Calculate BMI
        bmi = round(weight / (height * height), 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Pass the calculated values to the template
        return render(request, 'nutrition/bmi_calculator.html', {'bmi': bmi, 'category': category})

    # Render the form initially
    return render(request, 'Nutrition/bmi_calculator.html')


def healthy_diets(request):
    return render(request, 'Nutrition/healthy_diets.html')

def exercise_plans_view(request):
    return render(request, 'Nutrition/exercise_plans.html')

# nutrition/views.py



def know_yourself(request):
    result = None
    if request.method == "POST":
        # Get data from the form
        age = int(request.POST.get('age', 0))
        gender = request.POST.get('gender', '')
        weight = float(request.POST.get('weight', 0))
        height = float(request.POST.get('height', 0))
        activity_level = request.POST.get('activityLevel', '')
        blood_pressure = request.POST.get('bloodPressure', '')
        blood_sugar = float(request.POST.get('bloodSugar', 0))
        temperature = float(request.POST.get('temperature', 0))

        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)
        health_status = 'Underweight' if bmi < 18.5 else 'Normal weight' if bmi < 24.9 else 'Overweight' if bmi < 29.9 else 'Obesity'

        # Check blood sugar and temperature (basic evaluation)
        sugar_status = "Low" if blood_sugar < 70 else "High" if blood_sugar > 140 else "Normal"
        temp_status = "Low" if temperature < 36 else "High" if temperature > 37.5 else "Normal"

        result = {
            'bmi': round(bmi, 2),
            'health_status': health_status,
            'blood_pressure': blood_pressure,
            'sugar_status': sugar_status,
            'temp_status': temp_status,
        }

    return render(request, 'Nutrition/know_yourself.html', {'result': result})
def fit_yoga_hit_yoga(request):
    return render(request, 'Nutrition/fit_yoga_hit_yoga.html')


