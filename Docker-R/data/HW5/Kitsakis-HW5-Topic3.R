# Aggelou-Topic3.R
# Topic 3: SVMs

library(e1071)
library(ggplot2)
library(dplyr)

data(mtcars)
df <- mtcars[, c("hp", "wt", "am")]
df$am <- ifelse(df$am == 1, -1, 1)
df$hp <- scale(df$hp)
df$wt <- scale(df$wt)

svm_model <- svm(am ~ ., data = df, kernel = "linear", cost = 10, scale = FALSE)
w <- t(svm_model$coefs) %*% svm_model$SV
b <- -svm_model$rho
print(round(w, 3)); print(round(b, 3))

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
  indices <- which(mMax > 0)
  d1 <- -C * sum(y[indices] * X[indices, 1]) + w[1]
  d2 <- -C * sum(y[indices] * X[indices, 2]) + w[2]
  return(c(d1, d2))
}
compute_DJ(df, matrix(w, ncol = 1), 1)

ggplot(df, aes(x = hp, y = wt, color = factor(am))) +
  geom_point(size = 3) +
  geom_abline(intercept = -b/w[2], slope = -w[1]/w[2], color = "black") +
  geom_abline(intercept = (1 - b)/w[2], slope = -w[1]/w[2], linetype = "dashed", color = "red") +
  geom_abline(intercept = (-1 - b)/w[2], slope = -w[1]/w[2], linetype = "dashed", color = "blue") +
  labs(title = "SVM Decision Boundary", x = "hp", y = "wt")
