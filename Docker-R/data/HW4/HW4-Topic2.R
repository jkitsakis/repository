
file_path <- file.choose()
p_dec <- read.csv(file_path, header = TRUE, sep = ",")
print(p_dec)

#install.packages('data.tree')
library('data.tree')   # load library

IsPure <- function(data) {
  length(unique(data[,ncol(data)])) == 1
}

Entropy <- function( vls ) {
  res <- vls/sum(vls) * log2(vls/sum(vls))
  res[vls == 0] <- 0
  -sum(res)
}

InformationGain <- function( tble ) {
  tble <- as.data.frame.matrix(tble)
  entropyBefore <- Entropy(colSums(tble))
  s <- rowSums(tble)
  entropyAfter <- sum (s / sum(s) * apply(tble, MARGIN = 1, FUN = Entropy ))
  informationGain <- entropyBefore - entropyAfter  
  return (informationGain)
}

TrID3 <- function(node, data) {
  node$obsCount <- nrow(data)
  #if the data-set is pure (e.g. all no), then
  if (IsPure(data)) {
    #a leaf having the name of the pure feature (e.g. ‘no')will be  constructed
    child <- node$AddChild(unique(data[,ncol(data)]))
    node$feature <- tail(names(data), 1)
    child$obsCount <-  nrow(data)
    child$feature <- ''
  } else {
    #the feature with the highest information gain (e.g. 'outlook') will be   chosen
    ig <- sapply(colnames(data)[-ncol(data)], 
                 function(x) InformationGain(
                   table(data[,x], data[,ncol(data)])
                 )
    )
    feature <- names(ig)[ig == max(ig)][1]
    node$feature <- feature
    #the subset of the data-set having that feature value will be taken
    childObs <- split(data[,!(names(data) %in% feature), drop = FALSE], data[,feature], drop = TRUE) 
    
    for (i in 1:length(childObs)) { 
      #a child having the name of that feature value (e.g. 'sunny') will be constructed
      child <- node$AddChild(names(childObs)[i])
      #the algorithm recursively on the child and the subset will be called
      TrID3(child, childObs[[i]])
    }
  }
}

tree <- Node$new("Play")
TrID3(tree, p_dec)
print(tree, "feature", "obsCount")
