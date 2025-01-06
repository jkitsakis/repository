# load and read data 
eyes_data  <- read.csv("datasets//eyes_pred.csv", header = TRUE, sep = ";")

# Inspect dataset structure
str(eyes_data )

# Apply threshold
threshold <- 0.65
predicted_labels <- ifelse(eyes_data$UseOfGlassesPredicted >= threshold, 1, 0)
# View predicted labels
predicted_labels
# Simulated true labels (ground truth)
true_labels  <- eyes_data$UseOfGlassesActual
true_labels
# Create confusion matrix
confusion_matrix <- table(Predicted = predicted_labels, Actual = true_labels)
# Print confusion matrix
print(confusion_matrix)

# Extract values from confusion matrix
TP <- confusion_matrix[2, 2]
TN <- confusion_matrix[1, 1]
FP <- confusion_matrix[2, 1]
FN <- confusion_matrix[1, 2]

# Accuracy
accuracy <- (TP + TN) / sum(confusion_matrix)

# Precision
precision <- TP / (TP + FP)

# Recall (Sensitivity)
recall <- TP / (TP + FN)

# F1-Score
f1_score <- 2 * ((precision * recall) / (precision + recall))

# Print metrics
cat("Accuracy:", accuracy, "\n")
cat("Precision:", precision, "\n")
cat("Recall:", recall, "\n")
cat("F1-Score:", f1_score, "\n")