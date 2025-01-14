function toggleForm(date) {
	const formContainer = document.getElementById('task-form');
	
    const dateInput = document.querySelector("input[name='date']");
    

    // * form initially will be display === none so when we click the + button: 
    //*  1. we change the display to block to show it 
    //*  2. we assign the date value to the date that is passed into the function 
	if (formContainer.style.display === 'none') {
		formContainer.style.display = 'block';
        dateInput.value = date;
	}
    //* form initially will be display === block so when we click the + button: 
    // * 1. we change the display back to 'none' to hide it 
    // * 2. we then clear the dateInput value to return to default  
	if (formContainer.style.display === 'block') {
		formContainer.style.display = 'none';
		dateInput.value = '';
	}
}

// * the const formContainer = document.getElementById('task-form'): 
//* is used to find the <div> which contains the form so we can change the style.display 

// * the dateInput is used to find the <input> field in the form that is called name='date' so we can reassign the value later with date 
