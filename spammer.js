let isSpamming = false;

document.getElementById('start-button').addEventListener('click', startSpam);
document.getElementById('stop-button').addEventListener('click', stopSpam);
document.getElementById('continue-button').addEventListener('click', continueSpam);
document.getElementById('abort-button').addEventListener('click', abortSpam);

function startSpam() {
    const url = document.getElementById('webhook-url').value;
    const message = document.getElementById('spam-message').value;

    if (!url || !message) {
        alert('Please enter both Webhook URL and Spam Message.');
        return;
    }

    isSpamming = true;
    document.getElementById('stop-button').disabled = false;
    document.getElementById('continue-button').disabled = true;

    spamLoop(url, message);
}

function spamLoop(url, message) {
    if (!isSpamming) return;

    // Send POST request to the webhook URL with the spam message
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: message })
    }).catch(error => console.error('Error:', error));

    // Schedule the next request
    setTimeout(() => spamLoop(url, message), 0); // Immediate next request
}

function stopSpam() {
    isSpamming = false;
    document.getElementById('stop-button').disabled = true;
    document.getElementById('continue-button').disabled = false;
}

function continueSpam() {
    const url = document.getElementById('webhook-url').value;
    const message = document.getElementById('spam-message').value;

    if (!url || !message) {
        alert('Please enter both Webhook URL and Spam Message.');
        return;
    }

    isSpamming = true;
    document.getElementById('stop-button').disabled = false;
    document.getElementById('continue-button').disabled = true;

    spamLoop(url, message);
}

function abortSpam() {
    isSpamming = false;
    location.href = 'spammer.html';
}