function toggleForm(date) {
	const formContainerEl = document.getElementById('task-form');
	const nameInputEl = document.querySelector("input[name='name']");
    const dateInputEl = document.querySelector("input[name='date']");
    
	if (formContainerEl.style.display === 'none') {
		formContainerEl.style.display = 'block';
        dateInputEl.value = date;
        
	} else {
		formContainerEl.style.display = 'none';
		dateInputEl.value = '';
	}

	nameInputEl.focus()
    
}

// * the const formContainer = document.getElementById('task-form'): 
//* is used to find the <div> which contains the form so we can change the style.display 

// * the dateInput is used to find the <input> field in the form that is called name='date' so we can reassign the value later with date 


//! tried to do 2 if statement but it won't work because it gets checked twice