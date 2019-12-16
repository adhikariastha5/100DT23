# Introduction to Graphical models by Samrachana Adhikari
- Mixture of distribution: Mixture model
- Mixture model are flexible way to model complex distribution
- if k=1 then we are in parametric estimation and if k= infinity then we are in infinite estimation
- data point has each probability and then we can cluster into different groups in k means clustering
- start from k=2 and move towards k=50
- Latent variable Point of view :: Hidden layer is latent , make problem identify,interpret:: it is a class where random variable belong to.
- Conditional on class membership
- Mixture Gaussian-->Graphical representation
- lamda is where Z belongs to
- mean,variance of xn (data is n dim vector)
- another is edge aspect denote representation
- Loglikelihood estimation; (MLE) derivative with respect to parameter
- Expectation Maximization
- Start with guess and repeat again and again and when it reach equilibrium it is the final result
- fix the weight and then maximize func with respect to data (slide 14)
- guarantee to minimize to global minima (lower bound is always global---> converge all to global rather than local so it is smooth)
- Markov chain ; initialize; sample (we need value from previous sample right before)...keep doing until some convergence hold.(sample from posterior sample)
- lamda is membership vector
- we can choose k by maximizes information criteria (penalty term) eg aic,bic,dic ; train on some data and test data we take the likelihood
- as comp increases we introduce cause, so likelihood does not overpower much, so this cause becomes the k .
- non parametric -k means clustering
- Social network analysis 
- challenging is highly corelated data in unsupervised learning
- topic modeling we use idea of mixture model 
- we use lda in topic modeling(document topic modeling---->fix topic ; topic we don't label just 5 then they get it itself the label. topic to word distribution----> each topic ...gives picture of what it is. It has to assign.(need to learn...imp imp))
- heuristic that automatically gives clusture
- 




