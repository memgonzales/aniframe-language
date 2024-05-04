# AniFrame
![badge][badge-python]
![badge][badge-django]
![badge][badge-django-rest]
![badge][badge-react] <br>
[![Actions Status](https://github.com/memgonzales/aniframe-language/workflows/Check%20for%20syntax%20errors/badge.svg)](https://github.com/memgonzales/aniframe-language/actions)
![badge][badge-github-actions]


AniFrame is an open-source domain-specific language for two-dimensional drawing and frame-based animation for novice programmers. 

The language's core principles and features are as follows:
- **Ready Support for Animation-Specific Constructs.** AniFrame features animation-specific data types (e.g., for drawn objects and colors), operations (e.g., for mixing colors and simplifying the layering of objects into composite objects), and built-in functions for shapes and affine transformations.
- **Fine-Grained Control Over Animation.** AniFrame adopts a frame-based strategy where programmers explicitly specify the object to be animated, along with the start and end frames for the animation sequence. Settings such as the frame rate and the total number of frames can also be configured.
- **Reduced Learning Curve.** AniFrame follows a Python-like syntax, limits the number of keywords and control structures to a minimum, and tries to use keywords that are close to their semantic intent (e.g., `Text` instead of `string`). Specifying data types is optional since type inferencing is enforced.  
- **Computational Expressivity.** AniFrame supports common mathematical operations, built-in trigonometric functions, and user-defined recursive functions. Their utility is demonstrated in creating self-similar patterns, such as fractals.

If you find AniFrame useful, please consider citing:
```
```

![aniframe_kirby](https://github.com/memgonzales/aniframe-language/assets/44253974/bdcf7a0b-b5fa-40ad-a4f6-7492b7e922f4)

## Installing AniFrame

### A. Installing the Parser, Lexer & Interpreter

### B. Installing the Browser Environment

Refer to installation instructions [here](https://github.com/memgonzales/aniframe-language/blob/main/browser/README.md)

## Quick Start
1. Run the p5.js widget:
   ```
   cd browser/p5-widget/p5.js-widget
   npm start
   ```
   
1. In a separate terminal, activate the virtual environment:
   ```
   cd browser
   env\Scripts\activate.bat
   ```
   
1. Run the code in development mode:
   ```
   cd aniframe
   python manage.py runserver
   ```
   
1. Open [http://127.0.0.1:8000/]( http://127.0.0.1:8000/) to view the application in the browser.

1. Remember to activate the CORS-enabling extension for the AniFrame webpage before testing the application.
   

## Language Documentation

Refer to https://aniframe-docs.vercel.app/

## Gallery

## Authors

-   <b>Mark Edward M. Gonzales</b> <br/>
    mark_gonzales@dlsu.edu.ph <br/> 
    
-   <b>Hans Oswald A. Ibrahim</b> <br/>
    hans_oswald_ibrahim@dlsu.edu.ph <br/>

-   <b>Elyssia Barrie H. Ong</b> <br/>
    elyssia_ong@dlsu.edu.ph <br/>
    
-   <b>Mr. Ryan Austin Fernandez</b> <br/>
    ryan.fernandez@dlsu.edu.ph <br/>    

This is the major course output in a theory of programming languages class for master's students under Mr. Ryan Austin Fernandez of the Department of Software Technology, De La Salle University. The task is to create a domain-specific programming language within ten weeks.

[badge-python]: https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=white
[badge-django]: https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white
[badge-django-rest]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray
[badge-react]: https://img.shields.io/badge/react-%2320232a.svg?style=flat&logo=react&logoColor=%2361DAFB
[badge-github-actions]: https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white
