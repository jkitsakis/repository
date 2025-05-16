library(e1071)
library(ggplot2)
library(dplyr)

# Load the mtcars dataset
data(mtcars)

#Calculate means and standard deviations
# Mean values:
mean_hp <- mean(mtcars$hp)
mean_wt <- mean(mtcars$wt)

#Standard deviation values:
sd_hp <- sd(mtcars$hp)
sd_wt <- sd(mtcars$wt)

cat("Mean values:\n  hp:", round(mean_hp, 3), " wt:", round(mean_wt, 3), "\n")
cat("Standard deviation values:\n  hp:", round(sd_hp, 3), " wt:", round(sd_wt, 3), "\n")

#Use 'hp' (horsepower) and 'wt' (weight) as features, and 'am' (transmission type) as target variable
df <- mtcars[, c("hp", "wt", "am")]
# Convert 'am' to numeric (1 for automatic, -1 for manual)
df$am <- ifelse(df$am == 1, -1, 1)

# Normalize features using Z-score
df$hp <- scale(df$hp)
df$wt <- scale(df$wt)

# Check the structure and first few rows of the dataframe
str(df)
head(df)

# Train a linear SVM model
svm_model <- svm(am ~ ., data = df, kernel = "linear", cost = 10, scale = FALSE)

# Extract weights and bias from trained SVM model
w <- t(svm_model$coefs) %*% svm_model$SV
b <- -svm_model$rho

# Ensure `w` is a column vector
w <- matrix(w, ncol = 1)  # Convert w into a column vector

print(round(w, 3))
print(round(b, 3))

compute_J <- function(w, b, ds, C=1) {
  y <- ds$am
  X <- as.matrix(ds[, c("hp", "wt")])
  decision_values <- X %*% w + b
  hinge_loss <- sum(pmax(0, 1 - y * decision_values))
  regularization_term <- 0.5 * sum(w^2)
  return(regularization_term + C * hinge_loss)
}
compute_J(matrix(c(0.3, 0.7), ncol = 1), 0.5, df, 1)
compute_J(matrix(c(1, 1), ncol = 1), 0.2, df, 0.5)

compute_DJ <- function(ds, w, C) {
  X <- as.matrix(ds[, c("hp", "wt")])
  y <- ds$am
  tmp <- 1 - y * (X %*% w + b)
  mMax <- pmax(tmp, 0)
  
  # Find indices of misclassified points (where the hinge loss is > 0)
  indices <- which(mMax > 0)
  # Calculate gradients (d1 for hp, d2 for wt)
  d1 <- -C * sum(y[indices] * X[indices, 1]) + w[1]
  d2 <- -C * sum(y[indices] * X[indices, 2]) + w[2]
  return(c(d1, d2))
}

# Set regularization constant
C <- 1

# Compute Gradient at Initial Weights w(0)
gradient_values <- compute_DJ(df, w, C)

# Print the gradient values
cat("Gradient with respect to weights at initial w(0):\n")
cat("gradient w.r.t hp:", round(gradient_values[1], 3), "\n")
cat("gradient w.r.t wt:", round(gradient_values[2], 3), "\n")

