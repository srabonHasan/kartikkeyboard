let textInput = document.getElementById("textInput");
let button = document.getElementById("button-U");

let dict = {"a":"আ",  "b":"ব" , "c":"চ","d":"দ","e":"এ","f":"ফ","g":"গ","h":"হ","i":"ই","j":"জ","k":"ক","l":"ল","m":"ম","n":"ন","o":"অ", "p":"প","q":"ক","r": "র","s":"স","t":"ত","u":"উ","v":"ভ", "w":"ও","x":"এক্স","y":"য়","z":"য","A":"আ","B":"বি", "C":"চ","D":"ড", "E":"এ","F":"ফ","G":"গ","H":"হ","I": "ঈ","J":"য",
"K":"ক","L": "ল", "M": "ম","N":"ণ","O":"ো","P":"প","Q":"ক","R":"ড়","S":"শ","T":"ট","U":"উ","V": "ভ","W":"ও","X":"এক্স","Y":"য়","Z": "য"};

let dictBanglaToBangla = {"কউ":"কু","কই":"কি","কআ":"কা","মআ":"মা","নআ":"না","সহ":"শ","শর":"শ্র","শ্রআ":"শ্রা","বঅ":"ব","কএ":"কে","মই": "মি","বআ":"বা","নগ" : "ং","লআ": "লা","দএ": "দে","শএ": "শে","তহ": "থ","থআ": "থা","থআ" : "থা","ভআ": "ভা","সই": "সি","তউ": "তু","যএ": "যে","সঅ" : "স","তয়": "ত্য","ত্যই": "ত্যি","কঅ": "ক","রএ": "রে","বহ": "ভ","বই": "বি","ড়আ": "ড়া","হঅ": "হ","পউ": "পু","লএ": "লে","কহ": "খ","খঅ": "খ","নএ":"নে","জহ":"ঝ","রঅ":"র","জআ":"জা","বএ":"বে","লই":"লি","ঝএ":"ঝে","নঅ":"ন","রআ":"রা","খআ":"খা","রই":"রি","ফআ":"ফা"};

textInput.addEventListener("keyup", convertLanguage);
button.addEventListener("click",buttonToBangla);
function convertLanguage() {
  
  translateText(dict);
  translateText(dictBanglaToBangla);
  }
    function translateText(dict){
      let text = textInput.value;
    
  for(let letter in dict){// I run it for very key from dict.

    let re = new RegExp(letter,"g");// I create simple regex. I am using flag "g" global to change in whole text.
    text =  text.replace(re, dict[letter]); 
    textInput.value = text;
  }
    }
function buttonToBangla(){
 let buttonText = button.innerHTML;//I take letter of key.
   for(elem in dict){//I check for whole dictionary
     if(buttonText == elem){ //if letter on key is the same as key of dict I change with value of key
         button.innerHTML=dict[elem];
        break; //I use break do stop checking dict when I already find what I was looked
     }
   }
}
