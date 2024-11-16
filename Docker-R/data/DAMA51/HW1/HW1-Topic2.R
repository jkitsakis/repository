# 
# Topic 2
# 
#  a.	Inspect the dataset, using the str() and head() functions, 
#      and fill in the information requested in the table below
# 
# | |  Answer  |
# |:-----------------------------------------------------------|:--|
# | Number of dataset records                                  |   |
# | Number of numeric attributes (integer)                     |   |
# | Value of the attribute “Disease” of the 3rd dataset record |   |
#

# step 1 : read data from disease-symptoms-and-patient-profile-dataset.csv
df <- read.csv("DAMA51//HW1//Disease_symptom_and_patient_profile_dataset.csv", header = TRUE, sep = ",")

head(df)
# print(data.class(df))
# print(data.frame(df))

num_records <- nrow(df)
sprintf("Number of dataset records: %d", num_records)

str(df)
numeric_columns <- sum(sapply(df, is.numeric))
sprintf("Total numeric columns: %d", numeric_columns)

third_row_value <- df[3, "Disease"]
print(third_row_value)


resultdf <- data.frame(
  Questions = c("Number of dataset records", "Number of numeric attributes (integer)", "Value of the attribute “Disease” of the 3rd dataset record"),
  Answer = c(num_records, numeric_columns, third_row_value)
)

print(resultdf)

# 
# b. Create a contingency table, using R, with absolute frequencies for the attributes Fever and Cough. 
#
# |  | Cough |
# | --- | --- |
# | Fever | No | Yes | Sum |
# | No |  |  |  |
# | Yes |  |  |  |
# | Sum |  |  |  |

fever <- c(df$Fever)
cough <- c(df$Cough)
dfb <- data.frame(Fever=fever,Cough=cough)
print(dfb)

contingency_table <- table(dfb$Fever, dfb$Cough)
print(contingency_table)

# Add row and column sums. The addmargins() function in R adds row and column sums to the contingency table, providing additional details on data’s distribution
contingency_table_with_sums <- addmargins(contingency_table)

# Print the table
print(contingency_table_with_sums)


#c

fatigue_counts  <- table(df$Fatigue)
print(fatigue_counts )

# Create the bar chart
ggplot(df, aes(x = Fatigue)) +
  geom_bar(fill = "skyblue", color = "black") +
  labs(title = "Frequency of Fatigue Symptom",
       x = "Fatigue",
       y = "Frequency") +
  theme_minimal()


#d
# Create a table of counts for Cholesterol levels
cholesterol_counts <- table(df$Cholesterol)

# Basic pie chart
pie(cholesterol_counts, main = "Distribution of Cholesterol Levels", col = c("lightblue", "lightgreen", "lightcoral"))



#e
# Create the data frame
dfe <- data.frame(Disease = df$Disease, Age = df$Age)

# Print the data frame
print(dfe)

df_typhoid <- df[df$Disease == "Typhoid Fever", ]

ggplot(dfe, aes(x = Disease, y = Age, fill = Disease)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3") +
  labs(title = "Age Distribution Across Diseases",
       x = "Disease",
       y = "Age") +
  theme_minimal()
