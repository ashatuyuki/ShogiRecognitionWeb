## Shogi Diagram Converter
Last updated: 14/02/2022

This page describes Shogi Diagram Converter, an image recognition program written in Python. 

The goal of this project is to convert screenshots or photos of computer-printed Shogi (Japanese chess) diagrams into a machine-readable format. Such diagrams show positions of pieces on a chessboard and are frequently seen in publications.

<img src="/static/images/IMG_6109_mini.jpg" style="max-width:250px;" />

This problem can be broken down into three main steps: **Finding the diagram**, **correcting convexity defects** and **detecting the contents inside the diagram**.

### Finding the diagram
After reading the image, we first need to locate the chess board. 

Shogi books typically do not contain many images or shapes other than positional diagrams. The diagrams are also often the largest object on a page. Taking advantage of this, we can simply locate the diagram by finding the largest object in the image. Once located, we draw a [contour](https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html), or a bound around it.

<img src="/static/images/1-img_contour.jpg" style="max-width:300px;" />

### Correcting convexity defects
For pictures taken in real life, the books are often hand-held and as a result, diagrams can be warped. Here is a more extreme example where you can see bent board borders.

<img src="/static/images/defect_example.gif" style="max-width:300px;" />

Overly distorted images may not be correctly handled by our machine learning models. To correct the image, we first need to identify its vertical and horizontal lines through a series of image processing techniques. From there we can find the grid points - or the intersections between the rows and columns.

<img src="/static/images/grid_point_example.gif" style="max-width:300px;" />

Acquiring grid points also means that we now know coordinates of the board. This allows us to perform perspective transformation on each individual square. We then combine all 81 squares to create the corrected image. This step also standardises the size of the chess board to 504x504.

<img src="/static/images/1-img_diagram.jpg" style="max-width:300px;" />

See [here](https://stackoverflow.com/questions/10196198/how-to-remove-convexity-defects-in-a-sudoku-square) for a detailed explanation.

### Text recognition
Finally, we want to know the type and position of each chess piece represented in the diagram.

This is a typical text recognition problem that can potentially be solved by OCR. However, Tesseract proved to be weak against single characters that can be shown in an inverse position. For this reason we opted to use a Convolutional Neural Network (CNN) model using TensorFlow. The CNN model is trained on manually labelled data generated from previous steps of this project.

At last, we obtain the board position as required.

<img src="/static/images/1-output.jpg" style="max-width:300px;" />


### FAQ
#### What about 持ち駒 (captured pieces)?
It is out of scope. However, it is possible to detect them by drawing a contour around the text area and perform a similar exercise.

#### What about converting the results into standard computer notation such as SFEN?
It'll be done Soon<sup>TM</sup>