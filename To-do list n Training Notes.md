Implement the following:
- hyperparameter optimization (learn to automate this process eventually)
- compare results to baseline performance (ARIMA, random walk simulation)

*There was a lot of work done, but i noticed the code was a bit messy and so I am redoing my approach to optimization that I previously had implemented

OG Scores from paper: 
    Model  Train RMSE  Test RMSE
    ARIMA    0.0355      0.0292
    LSTM     0.0056      0.0365

Inital RMSE from LSTM (once seed is added):
    train = 0.0066
    validation = 0.0436

Starting Hyper Parameters:
- Lookback = 12
- Hidden size = 1
- Num layers = 1
- Epochs = 1000
- Batch Size = 30
- Training Size = 80%


Training notes
    Issues: the rmse is misleading at times. The rmse will display a score of 0.363 for example, but the prediction will be a straight line         indicating high bias


    Epochs:
        - at 1000 epochs the model suffers from high bias/underfitting, therefore I will increase the number of epochs to increase the amount of training
        - increasing to 2000 resulted in a better fit. Let's keep increasing and reassess.
        - increasing to 3000 resulted in a better fit. Let's keep increasing and reassess. 
            - train RMSE 0.0364, validation RMSE 0.0173, test RMSE 0.0171 
        - 5000, visually, seems to be little improvement
            - train RMSE 0.0364, validation RMSE 0.0174, test RMSE 0.0171
    Batch size:
        - Started with 30 (small size)
            train RMSE 0.0365, validation RMSE 0.0172
        - 80, train RMSE 0.0365, validation RMSE 0.0172 (no difference)
        - 200, seems to have high bias aka underfitting
        - 300, no improvement in underfitting. 
    Regularization:
    
    Lookback:


    Hidden Size:

    Number of layers:

        
