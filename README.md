# Perceptron
Trains a perceptron with data of any dimension.

# Usage
Run `python test_script.py`

This will show sample output for the perceptron given data.

# Sample output
```
Perceptron: 1.0
Perceptron: 0.42857142857142855
```
The values listed here is the accuracy the perceptron was able to achieve for both tests.
The first test trains the perceptron on data_1.txt, and prints the accuracy.
The second test trains the perceptron on data_2.txt, and runs it on the data in data_1.txt.

# Function descriptions for perceptron.py

X = samples (a list of samples, where each sample is the same dimension. The dimension can be anything, but it just needs to be the same for each sample.)
Y = labels for each sample.
w = perceptron weights
b = perceptron bias

## perceptron_train(X,Y)
Here is the process for how my perceptron model works.
- First, we initilize weights, equal to the number of items in X.
- We set the Bias to 0.
- We then run through epochs until we converge:
	- For each epoch, we calculate the result for each sample:
		- We compute the "value" by multiplying each feature of the sample le by its corresponding weight, and adding the bias.
		- We get the "result" by multiplying the "value" by the label.
		- If our result > 0, we continue, because this means we don't need to update any weights.
		- Otherwise, we update weights.
			- We add the label to the bias.
			- To update each weight, we add the existing weight + label * the corresponding feature.
			- We also mark that we "changed"/updated weights, so that our program knows we didn't converge.
	- If we did not make any changes to the weights when running through the Epoch, then we converged.
- After converging, we return the set of weights, and bias.

## perceptron_test(X,Y,w,b):
- We keep track of the number tested, and the number correct.
- For each sample in X, we compute the "value" and "result" in the same way we did in perceptron_train.
  - In this case, we use the weight set "w" and bias "b" to make the calculations.
	- If the result is > 0, then that means our model guessed correctly, and we add one to the number correct.
	- Regardless, we increment the number we tested.
- Finally, we return num_correct / num_tested to show the accuracy.
