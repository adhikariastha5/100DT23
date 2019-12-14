# CNN by Ajad Chhatkuli
- Human vision is done by brain.
- The summer vision Project (paper) -mit, patter recognition, find object
- Human different and good than computer.
- Children growing up interact with environment , computer barely can.
- We need data, learn with data, method and tools to learn data, knowledge (3d image project in our eyes,color). In our brain integrated already but we need to activate that in our computer by code.
- Image formation in eyes same as camera. Lens,retina.....(3D vision)
- Pixels in camera image having 1 or 3 channels(gray,color), dimension-resolution.(we get bunch of numbers which do onot change according to place and object-->that is challenging, view points different). For human we see differently and similarity but for computer just value comparision its different. Especially projection and scale, illumination, background clutter, intra-class varaiation,occlusion.
- How campare 2 images? (similarity-difference)::: We could vectorize features(image itself as feature), then compare x and y and sum of square distance(assume in eucledian distance). Another way is absolute value differences. Norms can be many. ( if we know it has noise )
- We cannot just use eucledian distance for comparision, we need other features.
- If image shifted,noise value, image is dark. These images are equidistant for computer.
- for all this we need better representation, we need CNN. (convolution)
- CNN not limited to images. Here CV only.
- func====> g*f=h
- sliding window, dot product.
- g*f=f*g=h
- Multiple feature channel from sliding multiple filters.
- Gauusian filter averages and makes blurr image.
- Sobel filters give Gx,Gy and joined gives overall outlines.( see the filters having 0,0,0 )
- Gabor filters  are special as realted to brain cells. They are just gaussian oriented by sinusoidal signals in mathematics. We and convolve by this filter and gives patterns.
- First cV app as product is Eureka. (fingerprint,faces){A.K.Jain at 1998}. He used Gabor filters.
- Loosely linked to the human brain. V1 cells in the Visual Cortex=> like Gabor filters
- We need to use filters conv with image and get feature maps.
- We need to use filters by asking What patterns do you want the machine to recognize?
- We can apply more than one filters and conv with image, conv with all channels and take average and make a single feature matrix.
- Pettern recognition book. Take inp image conv with filters , take features image/maps then make rules, like threshold this is cat is feature maps are this. eg. height of person use linear regression,lda,pca and get output.
- PCA only combine most important in vectors, In lda we consider lebels more than pca, use this labels to differentiate features of different classes and differentiate. 
- Here comes the CNN!
- We don't do handcrafted filters, In CNN filters are learned by themselves which is important how they learn. Imp backpropagation-help variables, convolve with multiple banks of features learned,how to reduce dimension like PCA.
- Yan LeCun's CNN paper (imp)
- Dimension Reduction ---> if 10 resolution image, we get 10 images after conv then again another and .... and so run out of memeory. So we do PCA, take 4 values and take max or average. Idea is like 0 then no info and throught it away. We are doing non- linear operation for dim. reduction. Agpool, maxpool.
- Kernel size/Mask Size-----> no of parameters,size of respective field,computational cost. More filters more parameters, more computation, notion of receptive field. We do not want to use huge filter size but receptive field we want big, so we use dilation filters. We leave one pixel out from the filters we convolve like sliding window=2. imp for image segmentation.
- Padding/Stride ---> when we want to convolve on boarder unless putting values or add 0. We want feature map same as input so we use padding. (we remove 1 layer out if we do not do padding). Stride means sliding window jump steps like 2....
- Summary:: Kernel,stride,dilation,(receptive field,parameter ), padding(size),pooling(taking relevant inf as dim red).
- Width and depth(channels and Layers)----> 6@28*28 ; 6 is the width. And layers means how deep or how many. We increase the width as we go in, as we do cnn. So many ways to represent image, 2-3D is not enough so we need more channels.....
- Activations----> max pooling do not solve, so we take non-linear one after max pooling. We apply some function with some weights that possibly can change feature map. 1. relu 2.sigmoid(rep probabilty-if feature map gives random then sigmoid compress the random and gives probability; does non linear activation).....there are more activation. (generally used relu, and sigmoid if you are regressing/logistic regression task). Softmax,tanh and so on.
- Bunch of filters(output no of feature maps, kernel size filters,define stride,dilation)*Conv , choose pooling , activation, we want to use batch normalization, sometimes we do not need batch norm..so we norm by 0,1 and then we have single layer output.
- CNN Encoder--->takes image as input, perform dim reduction, get more width,and represent feature.
- Aggregating global features----> fully connected layer. Output is linear operation on input and weights plus bias. We can add bias as extra parameter.
- Plug in the fully connected neuron. And take classification.
- Given image-- which class is the image? --- Create dataset with labeled. It can be 0,1,2,... (We have correct values with ground truth values), Feed image into encoder, get prediction, minimize loss function with relative to ground truth value.
- ImageNet Classification Challenge (Dataset public)
- ImageNet Classification with Deep Convolutional NN (Paper) /AlexNet
- They were able to optimized this network. Large dataset boon. Many parameters. Then deep learning hype strated from this result.
- Fully connected layer gives scores, they do not represented probability, only value of linear combination. Convert to probability such that sum of scores is 1. Using softmax S(yi)=exp of each values and normalize with all the values). 
- Network of Enc+Softmax: Conv+Max pooling then relu then fully connected layer with softmax and then gives the output probability.
- Dataset environment same as testing then fne, if new completely then NN will not perform good.
- Attention problem? not looking at the particular thing you want. Not the whole image. eg. sports and what is the action in it? Feed to CNN and classify it as related to environment or field like football,baseball rather than bat,ball, person. This becomes problem as infered the environment. To solve this we need to focus on action what is happening. This is called attention. In feature map, you have certain features coming from action what is happening, and remove not related to action and then only take the action. Have diff hands mask diff and see the actions, weight differently to find different actions. (RNN Attention model)
- What are the problems in image classification problem? 
- If you classify diff images, CNN learn more correctly.Take diff of the vectors and fing how similar they are. Used in many cases like google was using how to localize w/o gpu. Create database of images with location label, create feature vector and match with different feature of diff location. Feature with similarity gives right ans. (Image localization)
- To know segmentation, projection we should go into deep convolution. We need to bigger dimension than reducing.
- Deconvolutions, perform unsampling. Using this we give same image back.
- Eg. Auto-Encoder same image. Bottleneck. Naturally loose inf. we have loss after optimising we can get it back somehow. (Not perfect as encoder might not encode exact but decoder cannot get it perfectly)
- Transfer Learning (Auto encoder eg). We can use learned feature using transfer learning, we have some extra layer here and there and we have network from trained add some wanted features and then train for finding those.
- Cnn app: different approach--->classification,regression(location in image). Tasks--->depth(autonomous car, how far object id projected), normals(shake of the object), saliency(imp parts of image we focus on).
- For Tasks , our encoder is not enough. 
- Skip connections---> used in resnet, activation (learn identity function easily)-->learn residual from the identity(difference from identity only)...this makes it stable when we train. Handles exploding gradients.(ability for network to transfer)
- Image segmeantation ----> learn what is what like road, car,sky.. task is to find pixel and which class belong to which class.
- If we use simple encoder we loose info in bottle neck so in segmentation it loose much of the data. So we use skip connection.
- We use U-Net (enc-dec with skip connector) dim take care by upsampling,downsampling, do not need to learn everything in super low dimension feature space. Task which need detail uses skip connection.
- eg surgery using robots, used to find tools or key points. 
- Learning point sets, no order in points...like paint brush(point clouds), We cannnot find second point collinear with the first. So we use 1 by 1 conv and max pooling and so on.
- We take each point in input to higher and higher dimension then pool features ang get sort of repr of all point in high demensional. We can feedback to the network and learn local,global features.
- Learn PointNet(imp)
- Pointset eg. like 3D images, events happening in some locations diffrently there is no ordering.
- Data about users in business there is no ordering
- graph in Social network also is kind of related.
- Loss function optimization without ground truth labels-----> unsupervised methods. 
- Semantic segmentaion so we cannot use unsupervised, cluster or distance then unsupervised. For segmentation we can use semi supervise though.
- We don't use bias much in CNN

# Machine Learning and ethics by Juliane Klatt
-  Talked about ethics like security,privacy and so on. (Refer to slides and watch the videos linked and papers written out there.)
# AI in Social Sciences by Sunnie Joshi
-  Images to verify proxy. Alternative sources of data to proxy.
- Earthquake, Hurricane, monitoring urban growth, high risk buildings for building inspection.
- Using deep learning,cnn from drone,satelite data.
- Sri Lanka Poverty mapping.
- Real time Global Landslide Hazard Mapping(gather data related to landslide, geo specific data then mapped to real data and then get alert)
- Wildfire Prediction. factor like wind,himidity,temperature....but could not measure biomass.
- Flood extent mapping -----> understand where flood is happening the more. Use digital elevation of model and deep learning.
- Google ai for social good
- using ai for social good(go to website)
- Flood forecasting::massive amount of data to study flood.
- Detecting Plant disease.
- Google AI- Wind Power(renewable energy)
- Ai for earth(go to website)
 # Introduction to Probability by Samrachana Adhikari
 - rel freq of outcome after inf repetition.
 - cond/marg prob to cond prob--->bayes
 - Probablistic model::: Sample Space- set of all outcomes from experiment
 - Probabilty law: assign value to set A of possible outcomes.
 - A is event, P(A) is prob of A. Inter in terms of freq.
 - A is set and W is whole universe . If finite ,discrete it is straight forward.
 - eg. Pack of cards- Sample space=All poss draws, event E
 - Happening or not happening. Axioms: non-neg,additivity,normalization
 - prob a cond b= prob a intersection b /prob  b
 - ind p a and b equals a ......(see formula)
 - a is ind the b is ind also
 - Total probability Theorem: 
 - Bayes Rule
 - A1,.....An disjoint events form sample and assume P(Ai)>0 . then for any event B such that P(B)>0, 
# Lab Session
- self.conv1=nn.Conv2d(in_channels=3,out_channels=6,kernel_size=3,padding=1,bias=False)
- self.pool1=nn.MaxPool()
