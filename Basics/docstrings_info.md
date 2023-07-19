# Docstrings Info

- In Python, a docstring is a string literal that appears as the first statement within a module, function, class, or method definition. Docstrings are used to document and describe the purpose, usage, and behavior of the code entity they are associated with.

Here are some key points about docstrings:

1. **Purpose of Docstrings:**
   - Docstrings serve as a form of documentation for your code, providing a way to describe the functionality, usage, and expected inputs/outputs of a code entity.
   - They help other developers understand and use your code correctly, acting as a reference for how to interact with the code entity.

2. **Location of Docstrings:**
   - Docstrings are typically placed immediately after the definition line of a module, function, class, or method.
   - They are enclosed within triple quotes (`"""` or `'''`) to denote a multi-line string literal.

3. **Types of Docstrings:**
   - There are different conventions for writing docstrings, such as:
     - **Google Style**: Follows the Google Python Style Guide and uses a specific format for docstrings.
     - **Numpydoc Style**: Similar to Google Style but with additional conventions specific to NumPy.
     - **reStructuredText (reST) Style**: Uses reStructuredText markup language for more structured documentation.
   - The choice of style may depend on personal preference or adherence to project-specific guidelines.

4. **Content of Docstrings:**
   - Docstrings typically include the following sections:
     - A brief summary or description of the code entity's purpose and functionality.
     - Details about the inputs (parameters) and outputs (return values) of functions or methods.
     - Examples or usage scenarios demonstrating how to use the code entity.
     - Any additional notes, caveats, or special considerations related to the code entity.
   - The level of detail and sections included in docstrings may vary depending on the complexity and intended audience of the code.

5. **Accessing Docstrings:**
   - Python provides a way to access the docstring of a code entity programmatically using the `__doc__` attribute.
   - By accessing `__doc__`, you can retrieve and display the docstring at runtime.

Docstrings play an important role in documenting code, promoting code readability, and facilitating code reuse and maintenance. They provide a self-contained and concise way to describe the purpose and usage of your code entities, making it easier for others (and yourself) to understand and work with the code in the future.