//Anki Script for modifying 'Show Answer' behavior for Input types.
//This script captures the ANKI reviewer HTML output of the 'type:' field modifier,
//removes existing formatting, and returns only the typed answer in a <div> 
//element. The answer appearance can be customized using CSS and the 
//ID's '#correct' and '#incorrect'.

var htmlTextNodes = [];
var innerHTMLText = [];
var htmlNodeLength =document.getElementById('typeans').childNodes.length;
var typedAnswer;
var correctAnswer;
var firstBr = null;
var secondBr;

//capture each node to array
for (i = 0; i < htmlNodeLength; i++) {
	
	htmlTextNodes[i] = document.getElementById('typeans').childNodes[i];
	innerHTMLText[i] = document.getElementById('typeans').childNodes[i].innerHTML;
	
	//locate <br> tags for output change markers
	if (document.getElementById('typeans').childNodes[i].nodeName == "BR") {
		console.log("Runs if BR");
		if (firstBr != null) {
			secondBr = i;
		} else {
			firstBr = i;
		};
	};
};

//If answer is correct, firstBr will still be null, so must set to length of typeans.childNode
if (firstBr == null) {
	firstBr = htmlNodeLength;
};
//assemble typed and correct answer strings
typedAnswer = innerHTMLText.slice(0,firstBr).join("");
correctAnswer = innerHTMLText.slice(secondBr,htmlNodeLength).join("");

//Modify answer output
if (typedAnswer === correctAnswer) {
	var c = "<div id='correct'>"+typedAnswer+"</div>";
	var d = document.getElementById('typeans');
	d.innerHTML =  c;
} else {
	var e = "<div id='incorrect'>"+typedAnswer+"</div>";
	var f = document.getElementById('typeans');
	f.innerHTML =  e;
};