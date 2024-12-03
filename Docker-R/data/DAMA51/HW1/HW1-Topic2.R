# 
# Topic 2
# 

#  a.	
#
# load and read data 
data <- read.csv("DAMA51//HW1//datasets//Disease_symptom_and_patient_profile_dataset.csv", header = TRUE, sep = ",")

# Inspect dataset structure
str(data)

# view the first rows
head(data)

num_records <- nrow(data)
sprintf("Number of dataset records: %d", num_records)


numeric_columns <- sum(sapply(data, is.numeric))
sprintf("Total numeric columns: %d", numeric_columns)

third_row <- data[3, "Disease"]
print(third_row)


resultdf <- data.frame(
  Questions = c("Number of dataset records", "Number of numeric attributes (integer)", "Value of the attribute “Disease” of the 3rd dataset record"),
  Answer = c(num_records, numeric_columns, third_row)
)

print(resultdf)

# 
# b. Create a contingency table

# Contingency table
table <- table(data$Fever, data$Cough)
print(table)
addmargins(table)  # Add row and column sums


#c. bar chart 
fatigue_sums <- table(data$Fatigue)
print(fatigue_sums)
barplot(fatigue_sums, col = c("blue", "red"), main = "Fatigue Symptom Frequency",
        xlab = "Fatigue", ylab = "Count")


#d. Pie chart 
cholesterol_sums <- table(data$Cholesterol)
pie(cholesterol_sums, main = "Cholesterol Levels", col = c("blue", "green", "red"))



#e. Box plots for Age by Disease
boxplot(Age ~ Disease, data = data, main = "Age Distribution by Disease",
        xlab = "Disease", ylab = "Age")

# Specific analysis for Typhoid Fever
typhoid_age <- data$Age[data$Disease == "Typhoid Fever"]
# statistical summary of the typhoid_age 
summary(typhoid_age)  # Provides a summary of the age group


