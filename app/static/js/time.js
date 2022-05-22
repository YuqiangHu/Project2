function loadXMLDoc()
{
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		//  for IE7+, Firefox, Chrome, Opera, Safari browser
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		// for old IE6, IE5 browser 
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			var result_json = JSON.parse(xmlhttp.response);
			document.getElementById("test").innerHTML=result_json["datetime"]
		}
	}
	xmlhttp.open("GET","http://worldtimeapi.org/api/timezone/Australia/Perth",true);
	xmlhttp.send();
}