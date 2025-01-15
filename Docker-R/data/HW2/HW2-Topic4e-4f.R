# Gradient Descent function
LR_GradientDescent <- function(xx, yy, r, m, b, N) {
  n <- length(xx)  # Number of data points
  
  # Perform N iterations of gradient descent
  for (i in 1:N) {
    # Predicted values
    y_pred <- m * xx + b
    
    # Calculate gradients
    grad_m <- -sum((yy - y_pred) * xx) / n  # Gradient of SSE w.r.t. slope
    grad_b <- -sum(yy - y_pred) / n         # Gradient of SSE w.r.t. intercept
    
    # Update parameters
    m <- m - r * grad_m
    b <- b - r * grad_b
  }
  
  # Return the final slope, intercept, and cost
  rval <- list("slope" = m, "intercept" = b)
  return(rval)
}

# Load the longley dataset
data("longley")

# Data: Independent and dependent variables
x_data <- longley$Year
y_data <- longley$GNP

# Data scaling
xx <- scale(x_data)
yy <- scale(y_data)

# Perform Gradient Descent for 10 iterations (previous question)
lr_gd_10 <- LR_GradientDescent(xx, yy, r = 0.01, m = 1, b = 1, N = 10)

# Perform Gradient Descent for 50 iterations (new request)
lr_gd_50 <- LR_GradientDescent(xx, yy, r = 0.01, m = 1, b = 1, N = 50)

# Extract the slopes and intercepts
slope_10 <- lr_gd_10$slope
intercept_10 <- lr_gd_10$intercept

slope_50 <- lr_gd_50$slope
intercept_50 <- lr_gd_50$intercept

slope_50
intercept_50

# Predicted values for both lines
y_pred_10 <- slope_10 * xx + intercept_10
y_pred_50 <- slope_50 * xx + intercept_50

# Plot the data points
plot(xx, yy,
     main = "Linear Regression Using Gradient Descent (10 vs 50 Iterations)",
     xlab = "Year (scaled)",
     ylab = "GNP (scaled)",
     col = "blue", pch = 16)

# Plot the best-fit line after 10 iterations
lines(xx, y_pred_10, col = "red", lwd = 2, lty = 1)

# Plot the best-fit line after 50 iterations
lines(xx, y_pred_50, col = "green", lwd = 2, lty = 2)

# Add a legend
legend("topleft", legend = c("10 Iterations", "50 Iterations"),
       col = c("red", "green"), lwd = 2, lty = c(1, 2))
