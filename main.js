let courseData = []
const jsonUrl = 'courses_data.json';

$.ajax({ 
    url: jsonUrl, 
    dataType: 'json',
    async: false, 
    success: function(json){ 
        for(i in json){
			courseData.push(json[i]);
		};
	}
});


function courseSearch(){
	let keyword = document.getElementById("course_keyword").value;
	
	let options = {
		shouldSort: true,
		threshold: 0.2,
		distance: 100,
		location: 0,
		includeScore: true,
		keys: [
			"Course_title",
			"Course_code",
			"CRN",
			"Room",
			"Instructor"
		]
	};


	let fuse = new Fuse(courseData, options);
	let result = fuse.search(keyword);

	displayResult(result);
}

function displayResult(list){
	display = "";
	for(i in list){
		console.log("Course_code:  " + list[i].item.Course_code);
		console.log("Course_Title: " + list[i].item.Course_title);
		console.log("Instructor: " + list[i].item.Instructor);

		display += list[i].item.Course_code;
		display += "<br>" + list[i].item.Course_title;
		display += "<br>" + list[i].item.Instructor + "<br><br>";

	}
	document.getElementById("course_search_result").innerHTML = display;
}


function checkRoomAval(){
	let roomCode = document.getElementById('room_code').value;
	document.getElementById("room_search_result").innerHTML = roomCode;
	document.getElementById("room_search_result").innerHTML = "Room entered: " + roomCode + "<br>Result:";
}