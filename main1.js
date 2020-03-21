function courseSearch(){
	let keyword = document.getElementById("course_keyword").value;
	document.getElementById("course_search_result").innerHTML = keyword;
	//console.log(keyword);
}

function checkRoomAval(){
	let roomCode = document.getElementById('room_code').value;
	console.log(roomCode);
}