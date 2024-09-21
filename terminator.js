document.getElementById('delete-button').addEventListener('click', function() {
    const webhookUrl = document.getElementById('webhook-url').value;
    if (webhookUrl) {
        fetch(webhookUrl, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                showModal('Webhook deleted successfully.');
            } else {
                showModal('Failed to delete webhook.');
            }
        })
        .catch(error => {
            showModal('Error deleting webhook.');
            console.error('Error:', error);
        });
    } else {
        showModal('Please enter a webhook URL.');
    }
});

function showModal(message) {
    document.getElementById('modal-message').textContent = message;
    document.getElementById('modal').style.display = 'flex';
}

document.getElementById('modal-ok-button').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'none';
});

document.querySelector('.modal-close-button').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'none';
});