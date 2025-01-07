# Open a file selection dialog to choose and read eyes_pred.csv file
file_path <- file.choose()
eye_data <- read.csv(file_path, sep=";", stringsAsFactors=TRUE)

# Calculate the TPR & FPR
thrList = c(0.25, 0.5, 0.75)
data_actual <- factor(eye_data[,5])  # Assuming column 5 contains actual class labels
for (thr in thrList)
{
  # Generate predicted labels based on threshold
  data_predicted <- ifelse(eye_data[,4] >= thr, 1, 0)  # Assuming column 4 contains predicted probabilities
  
  # Create a confusion matrix
  conf_matrix <- caret::confusionMatrix(factor(data_predicted), data_actual)  # Using caret for `table` object
  
  # Extract TP, TN, FP, FN from conf_matrix$table
  TP <- conf_matrix$table[2, 2]
  TN <- conf_matrix$table[1, 1]
  FP <- conf_matrix$table[2, 1]
  FN <- conf_matrix$table[1, 2]
  
  # Calculate TPR and FPR
  TPR <- TP / (TP + FN)  # True Positive Rate
  FPR <- FP / (FP + TN)  # False Positive Rate
  
  # Print results
  cat("\nThreshold:")
  print(thr)
  cat("TPR:")
  print(round(TPR, 3))
  cat("FPR:")
  print(round(FPR, 3))
}


