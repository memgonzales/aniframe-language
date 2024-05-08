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

### Configuring the p5.js Widget

1. Install the necessary dependencies for the p5.js widget by running:

   ```
   cd browser/p5-widget/p5.js-widget
   npm install
   ```

1. Start the local server for the p5.js widget by running:

   ```
   npm start
   ```

### Configuring the Django Server

1. Open another terminal in the root of the cloned repository and activate the AniFrame virtual environment on this terminal as well:
   ```
   conda activate aniframe
   ```
  
1. Create the Django migration files by running: 

   ```
   cd browser/aniframe
   python manage.py makemigrations
   ```

   You might get a warning similar to the one below because the `build` folder has not yet been created. You may safely ignore it.

   ```
   ?: (staticfiles.W004) The directory '<some_path>/aniframe-language/browser/aniframe/frontend/build/static' in the STATICFILES_DIRS setting does not exist.
   ```

1. Migrate the changes by running:
   
   ```
   python manage.py migrate
   ```
   
1. Install the remaining dependencies by running: 

   ```
   cd frontend
   npm install
   npm run build
   ```

1. Start the local server by running:

   ```
   cd ../
   python manage.py runserver
   ```

1. Visit [http://localhost:8000](http://localhost:8000) on your browser.

## Enabling Cross-Origin Resource Sharing (CORS)

AniFrame uses a modified version of the p5.js widget in order to display graphics and animation sequences. However, since the browser-based environment is served over port 8000 while the p5.js widget is served over port 8080, **cross-origin resource sharing (CORS) should be enabled**. By default, it is disabled on most browsers, but an easy workaround is to use a CORS-enabling browser extension.

1. Install a CORS-enabling extension such as [this one](https://chromewebstore.google.com/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf) for Google Chrome.

1. Activate the extension for the AniFrame webpage.

---

## For Contributors: Making Changes to AniFrame's Browser-Based Environment

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


