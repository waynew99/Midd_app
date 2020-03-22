function courseSearch(){
	let keyword = document.getElementById("course_keyword").value;
	document.getElementById("course_search_result").innerHTML = "keyword: " + keyword + "<br>Result:";
	


}

function checkRoomAval(){
	let roomCode = document.getElementById('room_code').value;
	document.getElementById("room_search_result").innerHTML = roomCode;
	document.getElementById("room_search_result").innerHTML = "Room entered: " + roomCode + "<br>Result:";
}