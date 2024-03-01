# AniFrame
AniFrame is an open-source domain-specific language for two-dimensional drawing and frame-based animation for novice programmers. 

The language's core principles and features are as follows:
- **Ready Support for Animation-Specific Constructs.** AniFrame features animation-specific data types (e.g., for drawn objects and colors), operations (e.g., for mixing colors and simplifying the layering of objects into composite objects), and built-in functions for shapes and affine transformations.
- **Fine-Grained Control Over Animation.** AniFrame adopts a frame-based strategy where programmers explicitly specify the object to be animated, along with the start and end frames for the animation sequence. Settings such as the frame rate and the total number of frames can also be configured.
- **Reduced Learning Curve.** AniFrame follows a Python-like syntax, limits the number of keywords and control structures to a minimum, and tries to use keywords that are close to their semantic intent (e.g., \texttt{Text} instead of \texttt{string}). Specifying data types is optional since type inferencing is enforced.  
- **Computational Expressivity.** AniFrame supports common mathematical operations, built-in trigonometric functions, and user-defined recursive functions. Their utility is demonstrated in creating self-similar patterns, such as fractals.
