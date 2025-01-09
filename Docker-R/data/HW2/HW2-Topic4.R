# Inspect dataset structure
str(PlantGrowth)

# Subset data for control and treatment #2 groups
ctrl_group <- subset(PlantGrowth, group == "ctrl")$weight
trt2_group <- subset(PlantGrowth, group == "trt2")$weight


# Perform a two-sample t-test
t_test_result <- t.test(ctrl_group, trt2_group, alternative = "two.sided", var.equal = TRUE)

# Print the t-test result
print(t_test_result)

# Check if the p-value is less than 0.05
if (t_test_result$p.value < 0.05) {
  cat("Reject the null hypothesis: Treatment #2 significantly changes the plant weight.\n")
} else {
  cat("Fail to reject the null hypothesis: No significant change in plant weight due to treatment #2.\n")
}

satisfaction_table <- matrix(c(109, 141, 94, 180), nrow = 2, byrow = TRUE)
# Perform the Chi-Squared Test
chi_test_result <- chisq.test(satisfaction_table)

# Print the test results
print(chi_test_result)

# Check if the p-value is less than 0.05
if (chi_test_result$p.value < 0.05) {
  cat("Reject the null hypothesis.\n")
} else {
  cat("Fail to reject the null hypothesis.\n")
}


# Load the dataset
data("longley")

# Build the linear model
linear_model <- lm(Population ~ Year, data = longley)
# Display the model summary to extract slope and intercept
summary(linear_model)
# Extract slope and intercept
slope <- coef(linear_model)["Year"]
intercept <- coef(linear_model)["(Intercept)"]

# Calculate Mean Squared Error (MSE)
predicted_values <- predict(linear_model)
actual_values <- longley$Population
mse <- mean((actual_values - predicted_values)^2)

# Print results
cat("Slope:", slope, "\n")
cat("Intercept:", intercept, "\n")
cat("Mean Squared Error (MSE):", mse, "\n")

# Scatter plot of Year vs Population
plot(longley$Year, longley$Population, main = "Year vs Population",
     xlab = "Year", ylab = "Population", pch = 19, col = "blue")

# Add the regression line
abline(linear_model, col = "red", lwd = 2)


# Create a new data frame for the years 1963 to 1967
new_years <- data.frame(Year = 1963:1967)

# Predict the population for these years
predicted_population_new_years <- predict(linear_model, new_years)

# Create the table with the Year and Predicted Population
result_table <- data.frame(
  Year = 1963:1967,
  Predicted_Population = predicted_population_new_years
)

# Display the table
print(result_table)

