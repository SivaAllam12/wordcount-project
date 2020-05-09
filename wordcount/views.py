from django.http import HttpResponse
from django.shortcuts import render
def homefn(request):
	return render(request,'homepage.html')

def countfn(request):
	text=request.GET['text']
	if text:
		wordList=text.split()
		d={}
		for word in wordList:
			d[wordList.count(word)]=word
		if max(d)>1:
			mostFreqntWord=d[max(d)]
		else:
			mostFreqntWord=r"There's no word that's repeated"
		return render(request,'countpage.html',{'text':text,'count':len(wordList),'word':mostFreqntWord})
	else:
		message="Please enter some text"
		return render(request,'homepage.html',{'message':message})
		
	
def aboutfn(request):
	return render(request, 'aboutpage.html')