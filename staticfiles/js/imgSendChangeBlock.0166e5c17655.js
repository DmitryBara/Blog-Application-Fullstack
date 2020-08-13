// Change visibility of standart image field in HTML
// Send pre-loading image to AWS S3 before submit
// Block Submit button before form is ready and IMG is loaded to AWS



// For Submit Active or Disable (SD)
const form = document.querySelector('form')
const inputs = document.querySelectorAll('#id_title, #id_text')
const register = document.querySelector('input[type="submit"]')


// JS object checking inputs (SD)
const disabledFields = new Object()
disabledFields.title = true
disabledFields.text = true
disabledFields.image = true
disabledFields.aws_loaded = true

// make Submit button Active or Disable 
checkSubmit = () => {
	if ((!disabledFields.title) && (!disabledFields.text) && (!disabledFields.image) && (!disabledFields.aws_url))
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

		/// getSignedRequest for file to AWS S3 ///
		getSignedRequest(file);

		// Submit Disable here and next few times //
		disabledFields.image = false
		checkSubmit()

		removeImage.addEventListener('click', function () {
			inpFile.value = ""
			removeImage.style.display = "none"
			previewImage.style.display = "none"
			previewButton.style.display = "block"

			// for submit disable button
			disabledFields.aws_loaded = true
			disabledFields.image = true
			checkSubmit()

		}, false);

	} else {
		previewButton.style.display = null
		previewImage.style.display = null
		previewImage.setAttribute("src", "")
		
		disabledFields.image = true
		checkSubmit()
	}
})
