// Change visibility of standart image field in HTML
// Send pre-loading image to AWS S3 before submit
// Block Submit button before form is ready and IMG is loaded to AWS



// For Submit Active or Disable (SD)
const form = document.querySelector('form')
const inputs = document.querySelectorAll('#id_title, #id_text')
const register = document.querySelector('input[type="submit"]')
const progressStatus = document.getElementById("progress-status");

// JS object checking inputs (SD)
// On create is Bool from django temlates (edit or add)
const disabledFields = new Object()
disabledFields.title = on_create
disabledFields.text = on_create
disabledFields.image = on_create
disabledFields.aws_loaded = on_create

// make Submit button Active or Disable 
checkSubmit = () => {
	if ((!disabledFields.title) && (!disabledFields.text) && (!disabledFields.image) && (!disabledFields.aws_loaded))
		register.removeAttribute('disabled')
	else 
		register.setAttribute('disabled', 'disabled')
	}


checkSubmit()

// checkSubmit() for form.title, form.text at change moment(keyup)
form.addEventListener('keyup', function(e) {
	inputs.forEach(function(input, index) {
		if (input.value === '' || !input.value.replace(/\s/g, '').length) {
			disabledFields[input.name] = true
			checkSubmit()
		}
		else {
			disabledFields[input.name] = false
			checkSubmit()
		console.log(disabledFields)
		}
	})
})



///// For Img Label (show or hide) /////

const inpFile = document.getElementById("inpFile")
const previewContainer = document.getElementById("image-preview")
const previewImage = document.getElementById("image-preview__image")
const previewButton= document.getElementById("image-preview__label")
const removeImage = document.getElementById("image-remove")


inpFile.addEventListener("change", function() {
	let file = this.files[0]
	if (file) {
		const reader = new FileReader ()
		previewButton.style.display = "none"
		previewImage.style.display = "inline-block"

		reader.addEventListener("load", function () {
			previewImage.setAttribute("src", this.result)
		})

		reader.readAsDataURL(file)
		removeImage.style.display = "inline-block"
		progressStatus.style.display = "block"

		/// getSignedRequest for file to AWS S3 ///
		getSignedRequest(file);

		// Submit Disable here and next few times //
		disabledFields.image = false
		checkSubmit()

	} else {
		previewButton.style.display = null
		previewImage.style.display = null
		progressStatus.style.display = null
		previewImage.setAttribute("src", "")
	}
})


removeImage.addEventListener('click', function () {
	inpFile.value = ""
	removeImage.style.display = "none"
	previewImage.style.display = "none"
	previewButton.style.display = "block"
	progressStatus.style.display = "none"

	// for submit disable button
	disabledFields.aws_loaded = true
	disabledFields.image = true
	checkSubmit()

}, false);
