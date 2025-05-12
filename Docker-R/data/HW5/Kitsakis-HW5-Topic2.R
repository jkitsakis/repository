
library(caret)
library(tcltk)
library(dplyr)
library(e1071)
library(ggplot2)
library(class)

file_path <- tk_choose.files()
heart_data <- read.csv(file_path)

# Min-max normalization
minmax <- function(x) (x - min(x)) / (max(x) - min(x))
heart_data_norm <- heart_data
heart_data_norm[, c("age", "trestbps", "chol", "thalach", "oldpeak")] <- 
  lapply(heart_data_norm[, c("age", "trestbps", "chol", "thalach", "oldpeak")], minmax)

# Factor conversion
categorical_cols <- c("sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal")
heart_data_norm[categorical_cols] <- lapply(heart_data_norm[categorical_cols], factor)

# One-hot encoding
dummy_model <- dummyVars(~ ., data = heart_data_norm)
heart_data_norm <- predict(dummy_model, newdata = heart_data_norm)
heart_data_norm <- as.data.frame(heart_data_norm)

# Split
set.seed(123)
train_index <- createDataPartition(heart_data$target, p = 0.8, list = FALSE)
train_data <- heart_data_norm[train_index, ]
test_data <- heart_data_norm[-train_index, ]

train_x <- train_data[, -which(names(train_data) == "target")]
train_y <- train_data$target
test_x <- test_data[, -which(names(test_data) == "target")]
test_y <- test_data$target

# kNN
k_value <- 5
knn_pred <- knn(train_x, test_x, cl = train_y, k = k_value)

# Evaluation
knn_pred_numeric <- as.numeric(as.character(knn_pred))
conf_matrix <- table(Predicted = knn_pred_numeric, Actual = test_y)
accuracy <- sum(diag(conf_matrix)) / sum(conf_matrix)
precision <- conf_matrix["1", "1"] / sum(conf_matrix["1", ])
recall <- conf_matrix["1", "1"] / sum(conf_matrix[, "1"])
print(conf_matrix)
cat("Accuracy:", accuracy, "Precision:", precision, "Recall:", recall, "\n")

# Accuracy vs k
accuracy_list <- c()
k_vals <- seq(1, 20, by = 2)
for (k in k_vals) {
  pred <- knn(train_x, test_x, cl = train_y, k = k)
  acc <- sum(pred == test_y) / length(test_y)
  accuracy_list <- c(accuracy_list, acc)
}
plot(k_vals, accuracy_list, type = "b", col = "blue", pch = 19, xlab = "k", ylab = "Accuracy")
