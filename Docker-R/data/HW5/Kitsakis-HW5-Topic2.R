
library(caret)
library(dplyr)
library(e1071)
library(ggplot2)
library(class)

file_path <- file.choose()
heart_data <- read.csv(file_path)

# Normalize non-discrete features
minmax <- function(x) (x - min(x)) / (max(x) - min(x))

#Create a copy of heart_data to store the normalized values
heart_data_norm <- heart_data
heart_data_norm[, c("age", "trestbps", "chol", "thalach", "oldpeak")] <- 
  lapply(heart_data_norm[, c("age", "trestbps", "chol", "thalach", "oldpeak")], minmax)

# Convert categorical variables to factors excluding the target variable
categorical_cols <- c("sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal")
heart_data_norm[categorical_cols] <- lapply(heart_data_norm[categorical_cols], factor)

#Replace each factor attribute with a set of other (dummy) attributes, equal in number to the levels of the original attribute, where different values are represented using one-hot encoding.
dummy_model <- dummyVars(~ ., data = heart_data_norm)
heart_data_norm <- predict(dummy_model, newdata = heart_data_norm)
heart_data_norm <- as.data.frame(heart_data_norm)
head(heart_data_norm) 

# Create the Train-Test datasets (80-20 split rule)
set.seed(123)
train_index <- createDataPartition(heart_data$target, p = 0.8, list = FALSE)
train_data <- heart_data_norm[train_index, ]
test_data <- heart_data_norm[-train_index, ]

# Display dimensions of training and testing data
cat("Training Data Size:", nrow(train_data), "\n")
cat("Testing Data Size:", nrow(test_data), "\n")

# Separate features and labels
train_x <- train_data[, -which(names(train_data) == "target")]
train_y <- train_data$target
test_x <- test_data[, -which(names(test_data) == "target")]
test_y <- test_data$target

# Apply kNN algorithm
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
  print(acc)
  accuracy_list <- c(accuracy_list, acc)
}
plot(k_vals, accuracy_list, type = "b", col = "blue", pch = 19, xlab = "k", ylab = "Accuracy")
