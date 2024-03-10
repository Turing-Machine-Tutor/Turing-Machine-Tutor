# UC1 - Creating exercise

**Primary actor: ** TA

**Stakeholders and interests:**

- Course senior staff, who outline the goals and emphasis of the exercise
- TA, who creates the exercise, uploads it to MOODLE and checks user solutions
- Student, who will do the exercise.

**Preconditions: ** TA has received goals and emphasis for the exercise from the course senior staff, and outlined for themselves the tasks of the exercise, even if just in general lines.

**Postconditions: ** Exercise colab notebook is ready to be uploaded to MOODLE

## Basic flow

1. TA opens a template for creating exercise. The template is a basic Colab notebook file, with boilerplate lines that import the library and some comments.
2. TA writes markdown blocks explaining the tasks and possibly some code blocks.
3. TA may want to look at example files, PyDoc documentation and other user manuals provided to them.
4. Tasks may include, among other things:
   1. Defining a Turing Machine for a specific language, for example: $L=\{a^nb^n:\; n\in \mathbb{N}\}$
   2. Defining a function that creates a Turing machine for a certain language that is defined by one or more parameters, for example:
      $L(n) = \{ \sigma_1 \dots \sigma_k: \;k\leq n, \forall i<j.\, \sigma_i<\sigma_j \}\;\; (\text{over } \Sigma=\{0, 1, \dots, n-1\}^*)$
   3. Defining a function that creates Turing machines from other Turing machines (for examples, given $M_1, M_2$, to create a single-tape Turing Machine for $L(M_1) \cap L(M_2)$), or from other computational models, such as automata

