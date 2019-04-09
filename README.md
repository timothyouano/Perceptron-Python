# Perceptron-Python
An implemention of a supervised learning artificial intelligence, feed-forward neural network with backpropagation using Python. Supervised in a way that the AI uses a desired output which you yourself input. It's like a baby that you are teaching how to walk and giving instruction if he/she is doing right. Unlike unsupervised learning, you just tell the baby what he/she can do but does not actually point out what is right. This implementation is a single-layer perceptron but you could use to class to generate a multi-layer one.

This perceptron accepts 35 (5x7) inputs for a letter outputting a "CONSONANT" or "VOWEL".

The UI was generated using [PYQT5 Desinger][PYQT5 Designer].

## Training Steps
1. Initialize the weights randomly (including bias weight).
2. For each example j in our training set, perform calculate output where our input is x<sub>j</sub> and our desired output is d<sub>j</sub>. Add the bias weight after caluclating![calculate output](./img/calculate_output.svg)
3. Get the local error: desired output - output
4. If error is not equal to 0 then update weights ![update weights](./img/update_weights.svg) where <i>r</i> is the learning rate
5. Add the local error to the global error, if the global error is not equal to 0 then go back to step 2 or if current iteration is not equal to max iteration.

[PYQT5 Designer]: https://www.codementor.io/deepaksingh04/design-simple-dialog-using-pyqt5-designer-tool-ajskrd09n
[Calculate Output]: img/calculate_output.svg