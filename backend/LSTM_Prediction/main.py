import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import torch
from torch import nn, optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
import torch.utils.data as Data

plt.style.use('ggplot')

seq_length = 7  # time step
input_size = 5  # input dim
hidden_size = 6
num_layers = 1
num_classes = 1
learning_rate = 0.0001
batch_size = 16
n_iters = 12000
split_ratio = 0.7
data_path = 'data.xls'


def read_data(data_path):
    data = pd.read_excel(data_path)
    data_features = data.iloc[:, :input_size]  # Extracting the features from the data
    label = data.iloc[:, input_size]  # Extracting the last column as the label
    print(data_features.head())
    print(label)
    return data_features, label


def normalization(data, label):
    mm_x = MinMaxScaler()
    mm_y = MinMaxScaler()
    data = data.values
    data = mm_x.fit_transform(data)

    # Transpose the label data to maintain shape consistency before normalization
    label = label.values.reshape(-1, 1)  # Reshape label data to be 2D
    label = mm_y.fit_transform(label)
    return data, label, mm_y


def sliding_windows(data, label, seq_length):
    x = []
    y = []
    for i in range(len(data) - seq_length - 1):
        _x = data[i:(i + seq_length), :]
        _y = label[i + seq_length]  # Accessing label directly from NumPy array
        x.append(_x)
        y.append(_y)
    x, y = np.array(x), np.array(y)
    print('x.shape, y.shape:\n', x.shape, y.shape)
    return x, y


def data_split(x, y, split_ratio):
    train_size = int(len(y) * split_ratio)
    test_size = len(y) - train_size

    x_data = Variable(torch.Tensor(np.array(x)))
    y_data = Variable(torch.Tensor(np.array(y)))

    x_train = Variable(torch.Tensor(np.array(x[0:train_size])))
    y_train = Variable(torch.Tensor(np.array(y[0:train_size])))
    x_test = Variable(torch.Tensor(np.array(x[train_size:len(x)])))
    y_test = Variable(torch.Tensor(np.array(y[train_size:len(y)])))

    print('x_train.shape,y_train.shape,x_test.shape,y_test.shape:\n', x_train.shape, y_train.shape, x_test.shape,
          y_test.shape)
    return x_data, y_data, x_train, y_train, x_test, y_test


def data_generator(x_train, y_train, x_test, y_test, n_iters, batch_size):
    num_epochs = n_iters / (len(x_train) / batch_size)
    num_epochs = int(num_epochs)
    train_dataset = Data.TensorDataset(x_train, y_train)
    test_dataset = Data.TensorDataset(x_test, y_test)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=batch_size,
                                               shuffle=False)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=batch_size,
                                              shuffle=False)
    return train_loader, test_loader, num_epochs



data, label = read_data(data_path)
data, label, mm_y = normalization(data, label)
x, y = sliding_windows(data, label, seq_length)
x_data, y_data, x_train, y_train, x_test, y_test = data_split(x, y, split_ratio)
train_loader, test_loader, num_epochs = data_generator(x_train, y_train, x_test, y_test, n_iters, batch_size)

print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('x_test shape:', x_test.shape)
print('y_test shape:', y_test.shape)
print('Sample x_train:', x_train[0])  # Print a sample of x_train to understand its structure
print('Sample y_train:', y_train[0])  # Print a sample of y_train to understand its structure


import torch.nn.functional as F


class BP(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(BP, self).__init__()
        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length
        self.fc1 = nn.Linear(seq_length * input_size, 20)
        self.fc2 = nn.Linear(20, 20)
        self.fc3 = nn.Linear(20, num_classes)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        out = x.view(-1, self.seq_length * self.input_size)
        out = F.relu(self.fc1(out))
        out = F.relu(self.fc2(out))  # F.relu()
        out = self.fc3(out)
        return out


class GRU(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(GRU, self).__init__()

        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length

        self.gru = nn.GRU(input_size=input_size, hidden_size=hidden_size,
                          num_layers=num_layers, batch_first=True)

        self.fc1 = nn.Linear(hidden_size, 20)
        self.fc2 = nn.Linear(20, num_classes)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        h_0 = Variable(torch.zeros(
            self.num_layers, x.size(0), self.hidden_size))
        # Propagate input through GRU
        ula, h_out = self.gru(x, h_0)
        h_out = h_out.view(-1, self.hidden_size)
        out = F.relu(self.fc1(h_out))
        out = self.fc2(out)
        return out


class LSTM(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()

        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length

        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                            num_layers=num_layers, batch_first=True)

        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        h_0 = Variable(torch.zeros(
            self.num_layers, x.size(0), self.hidden_size))

        c_0 = Variable(torch.zeros(
            self.num_layers, x.size(0), self.hidden_size))

        # Propagate input through LSTM
        ula, (h_out, _) = self.lstm(x, (h_0, c_0))

        h_out = h_out.view(-1, self.hidden_size)

        out = self.fc(h_out)

        return out


criterion = torch.nn.MSELoss()  # mean-squared error for regression

# 训练并评估BP神经网络模型
bp_model = BP(num_classes, input_size, hidden_size, num_layers)
print(bp_model)
bp_optimizer = torch.optim.Adam(bp_model.parameters(), lr=learning_rate)

train_bp_losses = []  # 用于记录BP模型的训练损失

for epoch in range(num_epochs):
    for i, (batch_x, batch_y) in enumerate(train_loader):
        bp_optimizer.zero_grad()
        outputs = bp_model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        bp_optimizer.step()
        train_bp_losses.append(loss.item())


# 评估BP神经网络模型
def evaluate_model(model, x_data, y_data):
    model.eval()
    predictions = []
    with torch.no_grad():
        for i in range(0, len(x_data), batch_size):
            batch_x = x_data[i:i + batch_size]
            batch_predict = model(batch_x)
            predictions.append(batch_predict)
    predictions = torch.cat(predictions)
    data_predict = predictions.numpy()
    data_predict = mm_y.inverse_transform(data_predict)
    y_data_plot = y_data.data.numpy()
    y_data_plot = np.reshape(y_data_plot, (-1, 1))
    y_data_plot = mm_y.inverse_transform(y_data_plot)
    return y_data_plot, data_predict


# 评估BP神经网络模型
bp_train_true, bp_train_pred = evaluate_model(bp_model, x_train, y_train)
bp_test_true, bp_test_pred = evaluate_model(bp_model, x_test, y_test)

# 训练并评估GRU模型
gru_model = GRU(num_classes, input_size, hidden_size, num_layers)
gru_optimizer = torch.optim.Adam(gru_model.parameters(), lr=learning_rate)

train_gru_losses = []  # 用于记录GRU模型的训练损失

for epoch in range(num_epochs):
    for i, (batch_x, batch_y) in enumerate(train_loader):
        gru_optimizer.zero_grad()
        outputs = gru_model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        gru_optimizer.step()
        train_gru_losses.append(loss.item())

# 评估GRU模型
gru_train_true, gru_train_pred = evaluate_model(gru_model, x_train, y_train)
gru_test_true, gru_test_pred = evaluate_model(gru_model, x_test, y_test)

# 训练并评估LSTM模型
lstm_model = LSTM(num_classes, input_size, hidden_size, num_layers)
lstm_optimizer = torch.optim.Adam(lstm_model.parameters(), lr=learning_rate)

train_lstm_losses = []  # 用于记录LSTM模型的训练损失

for epoch in range(num_epochs):
    for i, (batch_x, batch_y) in enumerate(train_loader):
        lstm_optimizer.zero_grad()
        outputs = lstm_model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        lstm_optimizer.step()
        train_lstm_losses.append(loss.item())

# 评估LSTM模型
lstm_train_true, lstm_train_pred = evaluate_model(lstm_model, x_train, y_train)
lstm_test_true, lstm_test_pred = evaluate_model(lstm_model, x_test, y_test)

# 可视化比较三种模型的预测结果
plt.figure(figsize=(12, 6))

# 绘制训练集的预测结果比较图
plt.subplot(1, 2, 1)
# plt.plot(bp_train_true, label='BP True')
plt.plot(bp_train_pred, label='BP Predict')
# plt.plot(gru_train_true, label='GRU True')
plt.plot(gru_train_pred, label='GRU Predict')
plt.plot(lstm_train_true, label='True data')
plt.plot(lstm_train_pred, label='LSTM Predict')
plt.title('Training Set Predictions')
plt.legend()

# 绘制测试集的预测结果比较图
plt.subplot(1, 2, 2)
# plt.plot(bp_test_true, label='BP True')
plt.plot(bp_test_pred, label='BP Predict')
# plt.plot(gru_test_true, label='GRU True')
plt.plot(gru_test_pred, label='GRU Predict')
plt.plot(lstm_test_true, label='True data')
plt.plot(lstm_test_pred, label='LSTM Predict')
plt.title('Test Set Predictions')
plt.legend()

plt.tight_layout()
plt.savefig("./fitResult.jpg")
plt.show()



# 评估模型并返回评估指标
def evaluate_model(model, x_data, y_data):
    model.eval()
    predictions = []
    with torch.no_grad():
        for i in range(0, len(x_data), batch_size):
            batch_x = x_data[i:i + batch_size]
            batch_predict = model(batch_x)
            predictions.append(batch_predict)
    predictions = torch.cat(predictions)
    data_predict = predictions.numpy()
    data_predict = mm_y.inverse_transform(data_predict)
    y_data_plot = y_data.data.numpy()
    y_data_plot = np.reshape(y_data_plot, (-1, 1))
    y_data_plot = mm_y.inverse_transform(y_data_plot)

    # 计算评估指标
    mae = mean_absolute_error(y_data_plot, data_predict)
    rmse = np.sqrt(mean_squared_error(y_data_plot, data_predict))

    return mae, rmse


# 评估三个模型并输出评估指标
bp_mae, bp_rmse = evaluate_model(bp_model, x_test, y_test)
gru_mae, gru_rmse = evaluate_model(gru_model, x_test, y_test)
lstm_mae, lstm_rmse = evaluate_model(lstm_model, x_test, y_test)

# Debugging checkpoint 5: Print model evaluation metrics
print("BP Model Evaluation:")
print(f"MAE: {bp_mae}, RMSE: {bp_rmse}")

print("GRU Model Evaluation:")
print(f"MAE: {gru_mae}, RMSE: {gru_rmse}")

print("LSTM Model Evaluation:")
print(f"MAE: {lstm_mae}, RMSE: {lstm_rmse}")