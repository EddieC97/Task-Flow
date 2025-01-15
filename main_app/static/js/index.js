function clearSearchResults() {
	const searchResults = document.getElementById('search-results');

	searchResults.innerHTML = '';
	//* this line clears the whole div content in the beginning
}

// * I moved the searchResults.innerHTML = '' from filterTasks() into another function 
//! Prior to this, without this function, the searchResult container doesn't get cleared correctly if you press the search button twice without changing the search query 
// ~ Basically it will get appended twice 

function filterTasks() {
	const searchInput = document.getElementById('searchbar');
	const query = searchInput.value.toLowerCase().trim();

    const taskList = document.querySelectorAll('.task-item'); 
    const searchResults = document.getElementById('search-results');
    
    const filteredTasks = [];

    
	taskList.forEach((task) => {
		const taskName = task
			.querySelector('h2')
			.textContent.toLowerCase()
			.trim();
		//* I am looking for the text content inside the <h2> which is usually the task.name
		//* textContent then extracts the text inside the <h2> : get a string

		if (taskName.includes(query)) {
			filteredTasks.push(task);
		}
	});

	if (filteredTasks.length > 0) {
        filteredTasks.forEach((task) => {
            const cloneTask = task.cloneNode(true)
			searchResults.appendChild(cloneTask);
		});
        // * the task elements in the filteredTasks are not just plain string but are actually DOM elements: in our case <a> tag
        // * in this case, we need to copy the task because I am directly manipulating the DOM
        // ! without cloneNode, I will basically move the task from the all tasks list to the searchResult container like a true filter 
        // ~ .cloneNode(true) basically makes a deep copy of the task 
	} else {
		const noTasksFoundMessage = document.createElement('p');
		//* this creates a <p> element
		noTasksFoundMessage.textContent =
			'No tasks found matching your query.';
		searchResults.appendChild(noTasksFoundMessage);
	}
}


// * .include(): I used this instead of === because I am looking for a partial match 
// * the .replace(' ', ''): basically taking out spaces 
// * initially I had .replace() but I changed to .trim() for removing whitespaces 