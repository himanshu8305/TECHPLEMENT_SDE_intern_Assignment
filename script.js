// static/script.js

function searchLogs() {
    const searchQuery = document.getElementById('searchQuery').value;
    const filterQuery = document.getElementById('filterQuery').value;

    axios.post('/api/search', { searchQuery, filterQuery })
        .then(response => {
            displayResults(response.data);
        })
        .catch(error => {
            console.error('Error searching logs:', error);
        });
}

function clearResults() {
    document.getElementById('logResults').innerHTML = '';
}

function displayResults(logs) {
    const logResultsDiv = document.getElementById('logResults');
    logResultsDiv.innerHTML = '';

    logs.forEach(log => {
        const logDiv = document.createElement('div');
        logDiv.classList.add('notification');
        logDiv.classList.add('is-primary');
        logDiv.innerHTML = `
            <p><strong>Level:</strong> ${log.level}</p>
            <p><strong>Message:</strong> ${log.log_string}</p>
            <p><strong>Timestamp:</strong> ${log.timestamp}</p>
            <p><strong>Source:</strong> ${log.metadata.source}</p>
        `;
        logResultsDiv.appendChild(logDiv);
    });
}
