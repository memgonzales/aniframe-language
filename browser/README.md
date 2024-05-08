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

1. Launch another terminal from the root of the cloned repository, and activate the AniFrame virtual environment on this terminal as well:
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

AniFrame's browser-based environment embeds a [modified version](https://github.com/memgonzales/p5.js-widget) of the [p5.js widget](https://toolness.github.io/p5.js-widget) in order to display graphics and animation sequences. However, since the browser-based environment is served over port 8000 while the p5.js widget is served over port 8080, **cross-origin resource sharing (CORS) should be enabled**. By default, it is disabled on most browsers, but you can use a CORS-enabling browser extension to enable it for AniFrame.

1. Install a CORS-enabling extension like [this one](https://chromewebstore.google.com/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf) for Google Chrome.

1. Activate the extension for the AniFrame webpage:
   - Make sure to allow the extension to read and change site data when you click the extension.
     
     <img src = "https://github.com/memgonzales/aniframe-language/assets/44253974/db13b6c8-e1fc-490a-bbf2-83a21ec3d87e" width = "50%">

   - Make sure to toggle the extension on when you are using AniFrame at [http://localhost:8000](http://localhost:8000).
  
     <img src = "https://github.com/memgonzales/aniframe-language/assets/44253974/1fa2a475-bbad-42e1-8d9f-336c113f52cc" width = "50%">

## Running AniFrame Code via Conda

**💡 We highly recommend that you [install](https://github.com/memgonzales/aniframe-language?tab=readme-ov-file#option-1-using-docker-recommended) and [run](https://github.com/memgonzales/aniframe-language?tab=readme-ov-file#if-you-installed-aniframe-via-docker) AniFrame via Docker instead.**

1. Every time you want to use AniFrame, perform the following steps first:
   - Launch a terminal from the root of the cloned repository. Activate the AniFrame virtual environment on this terminal and start the local server for the p5.js widget by running:
     
     ```
     conda activate aniframe
     cd browser/p5-widget/p5.js-widget
     npm start 
     ```
     
   - Launch another terminal from the root of the cloned repository. Activate the AniFrame virtual environment on this terminal as well and start the Django server by running:
     
     ```
     conda activate aniframe
     cd browser/aniframe
     python manage.py runserver
     ```

1. Visit [http://localhost:8000](http://localhost:8000) on your browser.
   
1. Write the AniFrame code on the text editor at the left side of the webpage.

   For a quick start, you can refer to sample AniFrame source code [here](https://github.com/memgonzales/aniframe-language/tree/main/gallery).
   
1. Once you are done writing your code, click the Submit button.

   Doing so should open a window prompting you to select a folder. Select the `aniframe-code` folder that you created when [installing AniFrame](https://github.com/memgonzales/aniframe-language?tab=readme-ov-file#option-1-using-docker-recommended). If your browser prompts you to allow AniFrame to view files and save changes to this folder, grant these permissions.

1. Launch a (third) terminal from the root of the cloned repository. On this terminal, run:

   - For Windows:
     
     ```
     python interpreter/interpreter.py browser/p5-widget/p5.js-widget/static/sample.js && copy /y src.anf-int "browser/p5-widget/p5.js-widget/static/sample.js"
     ```

   - For Linux and macOS:

     ```
     python interpreter/interpreter.py browser/p5-widget/p5.js-widget/static/sample.js && cp -f src.anf-int browser/p5-widget/p5.js-widget/static/sample.js
     ```

   The text output of your code will be displayed on this terminal.

1. Navigate back to your browser, and click the Reset button.

   The visual output of your code will be displayed on the player at the right side of the webpage.

   _If no output is displayed, check if you properly enabled CORS (see instructions [here](https://github.com/memgonzales/aniframe-language/blob/main/browser/README.md#enabling-cross-origin-resource-sharing-cors))._

1. Once you are finished using AniFrame, deactivate the AniFrame virtual environment by running:
     
   ```
   conda deactivate
   ```

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


