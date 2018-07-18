function myFunction() {
    var x = document.getElementById("pass");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

/*
function myfunc() {
	var x = document.getElementById("user");
	var y = document.getElementById("pass");

	var loc = window.location.pathname;
	var dir = loc.substring(0, loc.lastIndexOf('/'))
	
	if(x.value === "9423050" && y.value==="123"){
		location.replace(dir+"/portal/home")
	} else {
		document.getElementById("wrong").style.display="block";
	}
}
*/