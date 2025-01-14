function toggleForm(date) {
	const formContainer = document.getElementById('task-form');
	
    const dateInput = document.querySelector("input[name='date']");
    
	if (formContainer.style.display === 'none') {
		formContainer.style.display = 'block';
        dateInput.value = date;
        
	} else {
		formContainer.style.display = 'none';
		dateInput.value = '';
	}
    
}

// * the const formContainer = document.getElementById('task-form'): 
//* is used to find the <div> which contains the form so we can change the style.display 

// * the dateInput is used to find the <input> field in the form that is called name='date' so we can reassign the value later with date 


//! tried to do 2 if statement but it won't work because it gets checked twice