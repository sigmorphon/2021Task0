#!/usr/bin/env Rscript
# SIGMORPHON 2021 - Task 0, Part 2 Evaluation
shhh <- suppressPackageStartupMessages # It's a library, so shhh!

shhh(require(tidyverse))
shhh(require(glmmTMB))
shhh(require(gsubfn))

get_args <- function() {
    args <- commandArgs(trailingOnly = TRUE)
    fname_gold <- args[1]
    fname_model <- args[2]

    return(c(fname_gold, fname_model))
}


list[fname_gold, fname_model] = get_args()

# fname_gold <- 'part2/eng.judgements.dev'
# fname_model <- 'part2/eng.judgements.dev'

data1 <- read_delim(fname_gold, "\t", escape_double = FALSE, trim_ws = TRUE, col_names = FALSE)
colnames(data1) <- c("lemma", "form", "tag", "human_rating")

data2 <- read_delim(fname_model, "\t", escape_double = FALSE, trim_ws = TRUE, col_names = FALSE)
colnames(data2) <- c("lemma", "form", "tag", "model_rating")

data <- merge(data1,data2,by=c("lemma","form", "tag"))
# summary(data)

# Make it between 0 and 1
data$human_rating <- data$human_rating / 7

# # create noise / fake data
# data$noise_high <- rnorm(nrow(data), 0, 1)
# data$model_rating <- data$model_rating + data$noise_high

# run models
model <- glmmTMB(human_rating ~ model_rating + (1 | lemma), data = data, family = beta_family())
# summary(model)
print('AIC')
print(AIC(model))
print('Log Likelihood:')
print(logLik(model))
