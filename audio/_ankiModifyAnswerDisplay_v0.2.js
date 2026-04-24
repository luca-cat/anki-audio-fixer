// Anki Script for modifying 'Show Answer' behavior for Input types.
//
// This script captures the ANKI reviewer HTML output of the 'type:' field modifier,
// removes existing formatting, and returns only the typed answer in a <div> 
// element. The answer appearance can be customized using CSS and the 
// ID's '#correct' and '#incorrect'.
// A third ID tag, "checkAnswer" must be added to a div surrounding the answer to be
// checked against.		e.g. <div id="checkAnswer">{{AnkiField}}</div>
// This field can be an already displayed field or you can use a different field and
// hide the "checkAnswer" div using CSS.
//
// DO NOT PLACE THE "checkAnswer" DIV AROUND THE {{Type:AnkiField}} FIELD TAG. THIS WILL BREAK THE SCRIPT!
// 

var innerHTMLText = [];
var htmlNodeLength =document.getElementById('typeans').childNodes.length;
var typedAnswer;
var correctAnswer;
var firstBr = null;

//capture each node to array
for (i = 0; i < htmlNodeLength; i++) {
	
	innerHTMLText[i] = document.getElementById('typeans').childNodes[i].innerHTML;
	
	//locate <br> tags for output change markers
	if (document.getElementById('typeans').childNodes[i].nodeName == "BR") {
		if (firstBr == null) {
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
correctAnswer = document.getElementById('checkAnswer').innerHTML;

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