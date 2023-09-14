Lambda, RMSE Scores:

Chosen: 0.0000001,  train RMSE 0.0369, validation RMSE 0.0294


Code to find lambda:

model = LSTM()
optimizer = optim.Adam(model.parameters())
loss_fn = nn.MSELoss()
loader = data.DataLoader(data.TensorDataset(X_train, y_train), shuffle=False, batch_size=1)
lambda_value = 0.0000001
n_epochs = 100
model_select = {}

for x in lambda_value:
    print(f"\nLambda = {x}")
    for epoch in range(n_epochs+1):
        model.train()
        for X_batch, y_batch in loader:
            optimizer.zero_grad()
            y_pred = model(X_batch)
            y_pred = y_pred.unsqueeze(2)

            #Loss and Regularization THIS IS WHERE THINGS MESS UP
            loss = loss_fn(y_pred, y_batch)
            reg_term = model.regularization(x)
            loss = torch.sqrt(loss + reg_term)

            loss.backward()
            optimizer.step()
        # #Progress Printer
        if epoch % 10 != 0:
            continue
        model.eval()
        with torch.no_grad():
            y_pred = model(X_train)
            y_pred = y_pred.unsqueeze(2)
            train_rmse = torch.sqrt(loss_fn(y_pred, y_train) + reg_term)
            
            y_pred = model(X_valid)
            y_pred = y_pred.unsqueeze(2)
            valid_rmse = torch.sqrt(loss_fn(y_pred, y_valid) + reg_term)
        print(f"Epoch {epoch}: train RMSE {train_rmse:.4f}, validation RMSE {valid_rmse:.4f}")
        if epoch == n_epochs:
            model_select[x] = valid_rmse
