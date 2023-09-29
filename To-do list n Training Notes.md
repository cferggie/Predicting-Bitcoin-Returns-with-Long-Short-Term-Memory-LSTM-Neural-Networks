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

        
