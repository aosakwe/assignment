set.seed(423)
#total papers: 537
#total students: 12
#537 mod 12 = 9
#(537-9)/12=44 papers divided evenly between us
#randomly arrange the numbers 1 through 528
v <- 1:528
v <- sample(v)
#split papers into groups of size 44
split(v, ceiling(seq_along(v)/44))