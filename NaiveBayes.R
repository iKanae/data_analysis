library(tm)
library(ggplot2)



spam.path<-'data/spam/'
#spam2.path<-'/home/data/spam_2/'
easyham.path<-'data/easy_ham/'
#easyham2.path<-'data/easy_ham_2'
hardham.path<-'data/hard_ham/'
#hardham2.path<-'data/hard_ham_2/'

get.msg<-function(path){
  con<-file(path,open='rt',encoding='latin1')
  text<-readLines(con)
  msg<-text[seq(which(text=='')[1]+1,length(text),1)]
  close(con)
  return(paste(msg,collapse='\n'))
}

get.tdm<-function(doc.vec){
  doc.corpus<-Corpus(VectorSource(doc.vec))
  control<-list(stopwords=TRUE,removePunctuation=TRUE,removeNumber=TRUE,
                minDocFreq=2)
  doc.dtm<-TermDocumentMatrix(doc.corpus,control)
  return(doc.dtm)
}

training.email<-function(training.path){
  training.docs<-dir(training.path)
  training.docs<-training.docs[which(training.docs!='cmds')]
  all.training<-sapply(training.docs,function(p) get.msg(paste(training.path,p,sep='')))
  training.tdm<-get.tdm(all.training)
  training.matrix<-as.matrix(training.tdm)
  training.counts<-rowSums(training.matrix)
  training.df<-data.frame(cbind(names(training.counts),as.numeric(training.counts)),stringsAsFactors = FALSE)
  names(training.df)<-c('term','frequency')
  training.df$frequency<-as.numeric(training.df$frequency)
  training.occurrence<-sapply(1:nrow(training.matrix),
                          function(i) {length(which(training.matrix[i,]>0))/ncol(training.matrix)})
  training.density<-training.df$frequency/sum(training.df$frequency)          
  training.df<-transform(training.df,density=training.density,occurrence=training.occurrence)
  return(training.df)
}


classify.email<-function(path,training.df,prior=0.2,c=1e-6){
  msg<-get.msg(path)
  msg.tdm<-get.tdm(msg)
  msg.freq<-rowSums(as.matrix(msg.tdm))
  msg.match<-intersect(names(msg.freq),training.df$term)
  if(length(msg.match)<1){
    return(prior*c^(length(msg.freq)))
  }
  else {
    match.probs<-training.df$occurrence[match(msg.match,training.df$term)]
    return(prior*prod(match.probs)*c^(length(msg.freq)-length(msg.match)))
  }
}

spam.df<-training.email(spam.path)
easyham.df<-training.email(easyham.path)

hardham.path<-easyham.path
hardham.docs<-dir(hardham.path)
hardham.docs<-hardham.docs[which(hardham.docs!='cmds')]
hardham.spamtest<-sapply(hardham.docs,function(p) classify.email(file.path(hardham.path,p),training.df=spam.df))
hardham.hamtest<-sapply(hardham.docs,function(p) classify.email(file.path(hardham.path,p),training.df=easyham.df))
hardham.res<-ifelse(hardham.spamtest>hardham.hamtest,TRUE,FALSE)
summary(hardham.res)

