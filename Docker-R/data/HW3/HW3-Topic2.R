
house_prices  <- read.csv("datasets//Housing.csv", header = TRUE, sep = ",")
str(house_prices)
# Select only numeric variables
house_prices_numeric <- house_prices[sapply(house_prices, is.numeric)]

# Standardize the data (Z-score normalization)
house_prices_scaled <- scale(house_prices_numeric)

# Compute the correlation matrix
cor_matrix <- cor(house_prices_scaled)

# Round the correlation values to 3 decimal places
cor_matrix_rounded <- round(cor_matrix, 3)

# Print the correlation matrix
print(cor_matrix_rounded)

#-- b --#
# correlation matrix
cor_matrix <- cor(house_prices_scaled)

# Extract correlations of all numeric features with 'price'
cor_price <- cor_matrix["price", ]
cor_price

# Remove 'price' 
cor_price <- cor_price[names(cor_price) != "price"]
cor_price

# Rank in descending order
cor_price_sorted <- sort(cor_price, decreasing = TRUE)
cor_price_sorted

# Select the top 3 features
selected_features <- names(cor_price_sorted)[1:3]

# Create a data frame for plotting
cor_df <- data.frame(Feature = selected_features, Correlation = cor_price_sorted[1:3])
cor_df

# bar chart
ggplot(cor_df, aes(x = reorder(Feature, Correlation), y = Correlation)) + 
  geom_bar(stat = "identity", fill = "red") + 
  coord_flip() + 
  labs(title = "Top 3 Correlated Features with Price",
       x = "Feature", 
       y = "Correlation") + 
  theme_minimal()

#-- c --#

# linear regression based on the top 3 features
lm_model <- lm(price ~ ., data = house_prices[, c("price", selected_features)])
lm_model

# calculate R-squared
model_summary <- summary(lm_model)
rsquared <- model_summary$r.squared
cat("R-squared: ", rsquared, "\n")

# predict the prices
predictions <- predict(lm_model, newdata = house_prices[, selected_features])
# Mean Absolute Error
mae <- mean(abs(house_prices$price - predictions))
cat("Mean Absolute Error (MAE): ", mae, "\n")

#-- d --#
# mean deviation 
price_mean <- mean(house_prices$price, na.rm = TRUE)
#standard deviation
price_sd <- sd(house_prices$price, na.rm = TRUE)
# De-normalize the predictions and actual values
denormalized_predictions <- (predictions * price_sd) + price_mean

house_prices_top3 <- house_prices[order(-house_prices$price), ][1:3, ]
denormalized_actual <- (house_prices$price * price_sd) + price_mean
denormalized_actual
# Provide de-normalized predictions for specific houses (ID: 5, 100, 305)
specific_denormalized_predictions <- round(denormalized_predictions[c(5, 100, 305)], digits = 3)
print(specific_denormalized_predictions)

# predicted vs actual values with a y = x reference line
plot(denormalized_actual, denormalized_predictions, 
     xlab = "Actual Price", ylab = "Predicted Price", 
     main = "Predicted vs Actual Prices")
abline(a = 0, b = 1, col = "red")  # y = x line for reference

#-- e --#
# mean and standard deviation of the original 'price' variable 
price_mean <- mean(house_prices$price, na.rm = TRUE)
price_sd <- sd(house_prices$price, na.rm = TRUE)

# de-normalize
denormalized_predictions <- (predictions * price_sd) + price_mean
denormalized_actual <- (house_prices$price * price_sd) + price_mean

# de-normalized predictions for specific houses (ID: 5, 100, 305)
specific_denormalized_predictions <- round(denormalized_predictions[c(5, 100, 305)], 3)
print(specific_denormalized_predictions)

# predicted vs actual values with a y = x reference line
plot(denormalized_actual, denormalized_predictions, 
     xlab = "Actual Price", ylab = "Predicted Price", 
     main = "Predicted vs Actual Prices")
abline(a = 0, b = 1, col = "red")  # y = x line for reference

