# AniFrame

![badge][badge-python]
![badge][badge-django]
![badge][badge-django-rest]
![badge][badge-react] <br>
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Create and publish Docker image](https://github.com/memgonzales/aniframe-language/actions/workflows/dockerize-and-publish.yml/badge.svg)](https://github.com/memgonzales/aniframe-language/actions/workflows/dockerize-and-publish.yml)
![badge][badge-github-actions]

AniFrame is an open-source domain-specific language for two-dimensional drawing and frame-based animation for novice programmers.

**This work was accepted for full paper presentation at the 24<sup>th</sup> Philippine Computing Science Congress ([PCSC 2024](https://pcsc.dlsu.edu.ph/)), held in Laguna, Philippines.**

-   Our preprint can be accessed via this [link](https://arxiv.org/abs/2404.10250).
-   Our PCSC 2024 can be accessed via this [link]().

If you find AniFrame useful, please consider citing:

```
@inproceedings{aniframe2024,
  title        = {AniFrame: A Programming Language for 2D Drawing and Frame-Based Animation},
  author       = {Gonzales, Mark Edward M. AND Ibrahim, Hans Oswald A. AND Ong, Elyssia Barrie H. AND Fernandez, Ryan Austin},
  year         = 2024,
  month        = {May},
  booktitle    = {24th Philippine Computing Science Congress (PCSC 2024)},
  publisher    = {Computing Society of the Philippines}
}
```

## ⚙️ Installing AniFrame

This installation bundles AniFrame's interpreter and browser-based environment where you can write and run code.

### System Requirements
- **Operating System:** Windows, macOS, or Linux
- **Storage:** ~1.8 GB

### Option 1: Using Docker (Recommended)

The simplest way to install AniFrame is via Docker.

1. Download and install [Docker](https://docs.docker.com/get-docker/), a platform for building and running containerized apps:

    - **[For macOS and Windows]** Install [Docker Desktop](https://docs.docker.com/get-docker/).
    - **[For Linux]** For easier installation, we recommend installing Docker Engine instead of Docker Desktop. Instructions for different Linux distributions can be found [here](https://docs.docker.com/engine/install/#supported-platforms).

1. Start the Docker daemon:
    - **[For macOS and Windows]** Open Docker Desktop to start the daemon.
    - **[For Linux]** Follow the instructions [here](https://docs.docker.com/config/daemon/start/).

1. Launch a terminal (from anywhere), and pull the latest version of AniFrame by running:
   ```
   docker pull ghcr.io/memgonzales/aniframe:latest
   ```

1. Create a folder named `aniframe-code` anywhere in your computer. Inside this folder, create an empty file named `sample.js`.

1. Spin up a container by running;
   ```
   docker create --name aniframe -p 8000:8000 -p 8080:8080 -v path/to/aniframe-code/sample.js/in/your/computer:/app/browser/p5-widget/p5.js-widget/static/sample.js ghcr.io/memgonzales/aniframe:latest
   ```

   Replace `path/to/aniframe-code/sample.js/in/your/computer` with the path to the `sample.js` file that you created in the previous step. It may be more convenient to use the absolute path. If you are using Windows, make sure to replace the backward slashes (`\`) in the path with forward slashes (`/`).

1. Launch a terminal (from anywhere), and start the AniFrame container by running:
   ```
   docker start aniframe
   ```

1. Open a shell _inside the container_ by running:
   ```
   docker exec -it aniframe bash
   ```
   
1. Inside this shell, run the following command:
   ```
   sh start-django.sh && exit
   ```

1. To open the environment where you can write and run AniFrame code, visit [http://localhost:8000](http://localhost:8000) on your browser.

### Option 2: Using Conda
<details>
  <summary>Click here to show/hide instructions for installing AniFrame via Conda.</summary>
  
1. Clone this repository by running:
   ```
   git clone https://github.com/memgonzales/aniframe-language
   ```

1. Create a virtual environment with the dependencies installed via Conda (we recommend using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html)):
   ```
   cd aniframe-language
   conda env create -f environment.yaml
   ```

1. Activate this environment by running:
   ```
   conda activate aniframe
   ```

1. Follow the instructions [here](https://github.com/memgonzales/aniframe-language/blob/main/browser/README.md) to configure AniFrame's browser-based environment.
</details>

## 🚀 Running AniFrame Code

### If you installed AniFrame via Docker
1. Every time you want to use AniFrame, perform the following steps first:
   - Launch a terminal (from anywhere). Start the AniFrame container and open a shell inside it by running:
     
     ```
     docker start aniframe
     docker exec -it aniframe bash
     ```
     
     Doing so should change the working directory to `root@<conainer_id>:/app/browser/p5-widget/p5.js-widget`.

   - Enable cross-origin resource sharing (CORS) following the instructions [here]().
     
1. Visit [http://localhost:8000](http://localhost:8000) on your browser.
   
1. Write the AniFrame code on the text editor at the left side of the webpage.

   For a quick start, you can refer to sample AniFrame source code [here](https://github.com/memgonzales/aniframe-language/tree/main/gallery).
   
1. Once you are done writing your code, click the Submit button.

   Doing so should open a window prompting you to select a folder. Select the `aniframe-code` folder that you created when [installing AniFrame](https://github.com/memgonzales/aniframe-language?tab=readme-ov-file#option-1-using-docker-recommended). If your browser prompts you to allow AniFrame to view files and save changes to this folder, grant these permissions. 
   
1. On the terminal that you opened in Step 1 (i.e., the shell with working directory `root@<conainer_id>:/app/browser/p5-widget/p5.js-widget`), run:
   ```
   sh run-code.sh
   ```
  
   The text output of your code will be displayed on this terminal.

1. Navigate back to your browser, and click the Reset button.

   The visual output of your code will be displayed on the player at the right side of the webpage.

   _If no output is displayed, check if you properly enabled CORS._
   
   ![aniframe_kirby](https://github.com/memgonzales/aniframe-language/assets/44253974/bdcf7a0b-b5fa-40ad-a4f6-7492b7e922f4)

### If you installed AniFrame via Conda

Refer to the instructions [here]().

## 📚 Description

Creative coding is an experimentation-heavy activity that requires translating high-level visual ideas into code. However, most languages and libraries for creative coding may not be adequately intuitive for beginners. Designed for novice programmers, AniFrame's core principles and features are as follows:

-   **Ready Support for Animation-Specific Constructs.** AniFrame features animation-specific data types (e.g., for drawn objects and colors), operations (e.g., for mixing colors and simplifying the layering of objects into composite objects), and built-in functions for shapes and affine transformations.
-   **Fine-Grained Control Over Animation.** AniFrame adopts a frame-based strategy where programmers explicitly specify the object to be animated, along with the start and end frames for the animation sequence. Settings such as the frame rate and the total number of frames can also be configured.
-   **Reduced Learning Curve.** AniFrame follows a Python-like syntax, limits the number of keywords and control structures to a minimum, and tries to use keywords that are close to their semantic intent (e.g., `Text` instead of `string`). Specifying data types is optional since type inferencing is enforced.
-   **Computational Expressivity.** AniFrame supports common mathematical operations, built-in trigonometric functions, and user-defined recursive functions. Their utility is demonstrated in creating self-similar patterns, such as fractals.

## 📒 Language Documentation

Refer to https://aniframe-docs.vercel.app/

## 🖼️ Gallery

We'd love to showcase your creative coding artwork here!

Code | Result | Code | Result
-- | -- | -- | --
[Jumping Shapes](https://github.com/memgonzales/aniframe-language/blob/main/gallery/jumping_shapes.anf) | <img src="https://github.com/memgonzales/aniframe-language/assets/79676314/177c8483-3f7f-4447-b208-3d1e7443db6a" width="200" height="200"> | [Smaller and Smaller Circles](https://github.com/memgonzales/aniframe-language/blob/main/gallery/smaller_and_smaller_circles.anf) | <img src="https://github.com/memgonzales/aniframe-language/assets/79676314/edd9d922-07e4-49f6-a5e1-19e0aeca081e" width="200" height="200">
[A Pink Round Hero](https://github.com/memgonzales/aniframe-language/blob/main/gallery/kirby.anf) | <img src="https://github.com/memgonzales/aniframe-language/assets/79676314/0998a8f4-c09a-4ca4-9e30-e3a5240b5f91" width="200" height="200"> | [Pinocchio](https://github.com/memgonzales/aniframe-language/blob/main/gallery/pinocchio.anf) | <img src="https://github.com/memgonzales/aniframe-language/assets/79676314/eb73c9b5-1a9a-4606-b0b9-76ee228eed12" width="200">

## 💻 Authors

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
