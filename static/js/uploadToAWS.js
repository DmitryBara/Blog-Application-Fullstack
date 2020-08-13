// This script upload choose files (form.image) to AWS S3
// Also listener setting on xhr. So proccess of loading is available



function getSignedRequest(file){
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sign_s3?file_name="+file.name+"&file_type="+file.type);
  xhr.onreadystatechange = function(){
    if(xhr.readyState === 4){
      if(xhr.status === 200){
        var response = JSON.parse(xhr.responseText);
        uploadFile(file, response.data, response.url);
      }
      else{
        alert("Could not get signed URL.");
      }
    }
  };
  xhr.send();
}


function uploadFile(file, s3Data, url){
  var xhr = new XMLHttpRequest();
  xhr.open("POST", s3Data.url);

  var postData = new FormData();
  for(key in s3Data.fields){
    postData.append(key, s3Data.fields[key]);
  }
  postData.append('file', file);
  xhr.upload.addEventListener("progress", uploadProgress, false);
  xhr.send(postData);

  // Percent of loading
  function uploadProgress(evt) {
    if (evt.lengthComputable) {
        var percentComplete = Math.round(evt.loaded * 100 / evt.total);
        progressStatus.textContent='Загрузка: ' + percentComplete.toString() + '%';
        if (percentComplete==100) {
        	disabledFields.aws_loaded = false
			checkSubmit()
        }
    }
  }
}