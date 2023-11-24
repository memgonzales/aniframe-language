# Aniframe Browser

## Tools Used
- Frontend: ReactJS 
- Backend: Django, Django REST Framework
- Base web application is taken from [here](https://github.com/Faruqt/React-Django)
- The p5.js Widget is taken from [here](https://toolness.github.io/p5.js-widget). For this project, a modified version was used which is found [here](https://github.com/memgonzales/p5.js-widget).

## Setup Intructions
1. Clone the repository 
2. Set up the p5.js widget locally:
```
 cd browser/p5-widget/p5.js-widget
 npm install
 ```
To run the p5.js widget:
```
 cd browser/p5-widget/p5.js-widget
 npm start
 ```
3. In a separate terminal, create your environment 
 ```
 cd browser
 python -m venv env
 ```
4. Activate your environment 
- For Windows:
```
env\Scripts\activate.bat
```
5. Navigate to the aniframe base folder that contains the requirements.txt file.
```
cd aniframe
```
6. Install all requirements
```
pip install -r requirements.txt
```
7. Make migrations
```
python manage.py makemigrations
```
 You might get the warning below because the build folder has not been created yet. Ignore it and proceed to the next step.
``` WARNINGS:
?: (staticfiles.W004) The directory '/Users/faruq/Desktop/test/React-Django/project1/frontend/build/static' in the STATICFILES_DIRS setting does not exist.
```

8. Migrate changes
```
python manage.py migrate
```
9. Navigate to the front end folder 
```
cd frontend
```
10. Install npm
```
npm install
```
11. Build the files
```
npm run build
```
12. Then navigate back to the root directory
```
cd ..
```
13. Run the following command to run the code in development mode
```
python manage.py runserver
```

14. Open [http://127.0.0.1:8000/]( http://127.0.0.1:8000/) to view and test the application in the browser.


## Additional Reminders
 - Remember to activate the virtual env for every start up of application:
```
cd browser
env\Scripts\activate.bat
cd aniframe
```

 - For new edits made to frontend, run the ff before viewing in the browser:
```
cd frontend
npm run build
cd ..
python manage.py runserver
```

 - For new edits made to model, run the ff before viewing in the browser:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
