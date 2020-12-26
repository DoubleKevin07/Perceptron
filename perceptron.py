# X is features, Y is label.
def perceptron_train(X,Y):
    w = []
    b = 0

    for val in range(len(X[0])):
        weight = 0
        w.append(weight)

    converged = False
    num_epoch = 0
    
    # Each iteration will go through an epoch.
    while converged is False:

        # Keep track to see if we made any changes to our weights.
        changed = False

        # Cycle through data set.
        for features, label in zip(X,Y):
            
            value = 0

            # For all weights, compute value
            weight_index = 0
            for weight in w:
                value += features[weight_index] * weight
                weight_index += 1

            # Add bias
            value += b

            # Multiply by label
            result = value * label

            # If result > 0, continue.
            if result > 0:
                continue # Don't update weights, we're good, just keep going.

            # Else, update. Set "changed" to true.    
            else:
                weight_index = 0
                for weight in w:
                    weight = weight + label * features[weight_index]
                    w[weight_index] = weight # Update the data  in the array itself.
                    weight_index += 1
                
                b += label

                changed = True
        
        num_epoch += 1
        
        # If we haven't changed anything when going through the data set, then we conerged.
        if changed is False:
            converged = True        
    
    return w,b

# Perceptron test
def perceptron_test(X,Y,w,b):

    num_tested = 0
    num_correct = 0

    # Cycle through data set.
    for features, label in zip(X,Y):

        # For all weights, compute value
        value = 0
        weight_index = 0
        for weight in w:
            value += features[weight_index] * weight
            weight_index += 1

        # Add bias
        value += b

        # Multiply by label
        result = value * label

        if result > 0:
            num_correct += 1

        num_tested += 1

    return num_correct / num_tested