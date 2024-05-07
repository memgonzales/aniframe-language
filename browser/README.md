# AniFrame's Browser-Based Environment

We provide a browser-based environment where you can write AniFrame scripts and view the output.

## Dependencies & Attribution

-   **Frontend:** ReactJS
-   **Backend:** Django, Django REST Framework
-   AniFrame's browser-based environment is based on this [web app](https://github.com/Faruqt/React-Django) by Faruq Abdulsalam.
-   AniFrame uses a [modified version](https://github.com/memgonzales/p5.js-widget) of the [p5.js widget](https://toolness.github.io/p5.js-widget) originally developed by Atul Varma.

## Installing AniFrame's Browser-Based Environment via Conda

**💡 We highly recommend that you install AniFrame via Docker following the instructions [here](https://github.com/memgonzales/aniframe-language?tab=readme-ov-file#option-1-using-docker-recommended).** This Docker installation bundles both the interpreter and the browser-based environment.

The instructions below assume that you opt to install via Conda and have run the steps [here](https://github.com/memgonzales/aniframe-language?tab=readme-ov-file#option-2-using-conda).

### Configuring p5.js Widget

1. Clone the repository
1. Set up the p5.js widget locally:

    ```
    cd browser/p5-widget/p5.js-widget
    npm install
    ```

    Run the p5.js widget:

    ```
    cd browser/p5-widget/p5.js-widget
    npm start
    ```

### Configuring AniFrame Browser

1. In a separate terminal, create your environment:
    ```
    cd browser
    python -m venv env
    ```
1. Activate your environment:
    ```
    env\Scripts\activate.bat
    ```
1. Navigate to the aniframe base folder that contains the `requirements.txt` file:
    ```
    cd aniframe
    ```
1. Install all requirements:
    ```
    pip install -r requirements.txt
    ```
1. Make migrations:

    ```
    python manage.py makemigrations
    ```

    You might get a warning similar to this one below because the build folder has not been created yet. Ignore it and proceed to the next step.

    ```WARNINGS:
    ?: (staticfiles.W004) The directory '/Users/faruq/Desktop/test/React-Django/project1/frontend/build/static' in the STATICFILES_DIRS setting does not exist.
    ```

1. Migrate changes:
    ```
    python manage.py migrate
    ```
1. Navigate to the front end folder:
    ```
    cd frontend
    ```
1. Install npm:
    ```
    npm install
    ```
1. Build the files:
    ```
    npm run build
    ```
1. Navigate back to the root directory:
    ```
    cd ..
    ```
1. Run the following command to run the code in development mode:
    ```
    python manage.py runserver
    ```
1. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application in the browser.

---

### C. Enabling CORS

Cross-origin resource sharing (CORS) is needed for AniFrame to read user-input files, but it is disabled on browsers by default. This can be rectified with a browser extension.

1. Install a CORS-enabling extension such as [this one for Google Chrome](https://chromewebstore.google.com/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf).

1. Activate the extension for the AniFrame webpage.

---

### D. Viewing New Changes

New changes made to the model or frontend of AniFrame are only reflected upon restarting the browser.

1. Navigate to the root directory:

    ```
    cd ..
    ```

1. Run the following commands upon updating the frontend:
    ```
    cd frontend
    npm run build
    cd ..
    ```
1. Run the following commands upon updating the model:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
1. Run the code in development mode:
    ```
    python manage.py runserver
    ```
1. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the new changes in the browser.

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
1. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application in the browser.

1. Remember to activate the CORS-enabling extension for the AniFrame webpage before testing the application.
