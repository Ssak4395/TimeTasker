// file upload
window.setInterval(function () {
    var input = document.querySelector("input[type=file]");
    if (input.files.length == 0) {
        // alert('nothing');
    }
    else {
        // alert('sth');
        // check file type
        if (input.files[0].type != "text/calendar") {
            alert("Wrong type of file for uploading.\n.ics file is the only acceptable file type");
        }
    }
}, 5000);