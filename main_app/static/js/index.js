function filterTasks() {
	const searchInput = document.getElementById('searchbar');
	const query = searchInput.value.toLowerCase()

	const taskList = document.querySelectorAll('.task-item');
	const searchResults = document.getElementById('search-results');

	const filteredTasks = [];

	taskList.forEach((task) => {
        const taskName = task.querySelector('h2').textContent.toLowerCase()
        //* I am looking for the text content inside the <h2> which is usually the task.name
        //* textContent then extracts the text inside the <h2> : get a string 

		if (taskName.includes(query)) {
			filteredTasks.push(task);
		}
	});

    searchResults.innerHTML = '';
    //* this line clears the whole div content in the beginning 

	if (filteredTasks.length > 0) {
		filteredTasks.forEach((task) => {
			searchResults.appendChild(task);
        });
        // * the task elements in the filteredTasks are not just plain string but are actually DOM elements: in our case <a> tag
	} else {
        const noTasksFoundMessage = document.createElement('p');
        //* this creates a <p> element 
		noTasksFoundMessage.textContent = 'No tasks found matching your query.';
		searchResults.appendChild(noTasksFoundMessage);
	}
}


// * .include(): I used this instead of === because I am looking for a partial match 