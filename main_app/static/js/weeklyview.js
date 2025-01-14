function toggleForm(date) {
	const formContainer = document.getElementById('task-form');
	
	const dateInput = document.querySelector("input[name='date']");

	if (
		formContainer.style.display === 'none' ||
		formContainer.style.display === ''
	) {
		formContainer.style.display = 'block';
		
		dateInput.value = date;
	} else {
		formContainer.style.display = 'none';
		
		dateInput.value = '';
	}
}

// * 
