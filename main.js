
let courseData

$.getJSON('courses_data.json', function(data){
	courseData = data;
})


function courseSearch(){
	let keyword = document.getElementById("course_keyword").value;
	
	let options = {
		shouldSort: true,
		threshold: 0.6,
		distance: 100,
		location: 0,
		keys: [
			"Course_title",
			"Course_code",
			"CRN",
			"Room",
			"Instructor"
		]
	};

	let fuse = new Fuse(courseData, options);
	fuse.search(keyword);

	document.getElementById("course_search_result").innerHTML = "keyword: " + keyword + "<br>Result:" + fuse;

	console.log(fuse);
	/*
	let options = {
		shouldSort: true,
		threshold: 0.6,
		location: 0,
		distance: 100,
		minMatchCharLength: 1,
		keys: [
		"Course_title"
		]
	};
	let fuse = new Fuse(courseData, options); // "list" is the item array
	let result = fuse.search("comp");
	*/


}


function checkRoomAval(){
	let roomCode = document.getElementById('room_code').value;
	document.getElementById("room_search_result").innerHTML = roomCode;
	document.getElementById("room_search_result").innerHTML = "Room entered: " + roomCode + "<br>Result:";
}