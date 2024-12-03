# a
studentData <- read.csv("DAMA51//HW1//datasets//StudentPerformanceFactors.csv", header = TRUE, sep = ",")

# Inspect structure
str(studentData)

# Number of records
num_records <- nrow(studentData)
sprintf("Number of dataset records: %d", num_records)

# Number of attributes
num_columns <- ncol(studentData)
sprintf("Total number of columns: %d", num_columns)

numeric_columns <- sum(sapply(studentData, is.numeric))
sprintf("Total numeric columns: %d", numeric_columns)

result_a <- data.frame(
  Questions = c("Number of records in the dataset", "Number of different attributes", "Number of numeric attributes (integer)"),
  Answer = c(num_records, num_columns, numeric_columns)
)

print(result_a)

#b. numeric attributes
StudentDataNumeric <- studentData[, sapply(studentData, is.numeric)]
print(StudentDataNumeric)

#c.Calculate the correlation matrix for the numeric subset
correlation_matrix <- cor(StudentDataNumeric, method = "pearson")
print(correlation_matrix)


# Create a heatmap of the correlation matrix
heatmap(correlation_matrix)
max_corr_value <- max(correlation_matrix[correlation_matrix != 1])  # Exclude diagonal (1's)
print(max_corr_value)
# Find the position of the maximum correlation value
max_corr_pair <- which(correlation_matrix == max_corr_value, arr.ind = TRUE)
print(max_corr_pair)

#d. Specific correlations
cor_attendance_hours <- cor(studentData$Attendance, studentData$Hours_Studied, method = "pearson")
cor_attendance_exam <- cor(studentData$Attendance, studentData$Exam_Score, method = "pearson")
cor_tutoring_prev <- cor(studentData$Tutoring_Sessions, studentData$Previous_Scores, method = "pearson")
cor_physical_sleep <- cor(studentData$Physical_Activity, studentData$Sleep_Hours, method = "pearson")

# Create a table to display the pairs and their correlation coefficients
result_d <- data.frame(
  Pair = c("(Attendance, Hours_Studied)", "(Attendance, Exam_Score)", 
           "(Tutoring_Sessions, Previous_Scores)", "(Physical_Activity, Sleep_Hours)"),
  Pearson_Correlation = c(cor_attendance_hours, cor_attendance_exam, cor_tutoring_prev, cor_physical_sleep)
)
print(result_d)

#e. Scatter plot of attributes Exam_Score and Hours_Studied
plot(studentData$Hours_Studied, studentData$Exam_Score,
     xlab = "Hours Studied",  # Label for x-axis
     ylab = "Exam Score",     # Label for y-axis
     main = "Scatter Plot",   # Title
     pch = 19,                # Point type (19 is a solid circle)
     col = "blue")            # Point color (blue)
