# a
StudentData <- read.csv("DAMA51//HW1//StudentPerformanceFactors.csv", header = TRUE, sep = ",")

str(StudentData)

num_records <- nrow(StudentData)
sprintf("Number of dataset records: %d", num_records)

num_columns <- ncol(StudentData)
sprintf("Total number of columns: %d", num_columns)

numeric_columns <- sum(sapply(StudentData, is.numeric))
sprintf("Total numeric columns: %d", numeric_columns)

resultdf <- data.frame(
  Questions = c("Number of records in the dataset", "Number of different attributes", "Number of numeric attributes (integer)"),
  Answer = c(num_records, num_columns, numeric_columns)
)

#b
StudentDataNumeric <- StudentData[, sapply(StudentData, is.numeric)]
print(StudentDataNumeric)

#c
# Calculate the correlation matrix for the numeric subset
correlation_matrix <- cor(StudentDataNumeric, method = "pearson")

# Display the correlation matrix
print(correlation_matrix)


# Create a heatmap of the correlation matrix
heatmap(correlation_matrix)

# Assuming you have already created `correlation_matrix`:
# correlation_matrix <- cor(StudentDataNumeric, method = "pearson")

# Set the lower triangle of the matrix to NA to avoid duplicates
correlation_matrix[lower.tri(correlation_matrix)] <- NA

# Find the maximum absolute correlation value
max_corr <- max(abs(correlation_matrix), na.rm = TRUE)

# Identify the pairs of variables with the strongest positive and negative correlations
strongest_positive_pair <- which(correlation_matrix == max_corr, arr.ind = TRUE)
strongest_negative_pair <- which(correlation_matrix == -max_corr, arr.ind = TRUE)

# Display results
print(paste("The pair with the strongest positive correlation is:", 
            colnames(correlation_matrix)[strongest_positive_pair[1]], "and", 
            rownames(correlation_matrix)[strongest_positive_pair[2]]))

print(paste("The pair with the strongest negative correlation is:", 
            colnames(correlation_matrix)[strongest_negative_pair[1]], "and", 
            rownames(correlation_matrix)[strongest_negative_pair[2]]))
