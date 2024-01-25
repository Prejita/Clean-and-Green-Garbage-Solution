// Function to update the notification count
function updateNotificationCount() {
    // Fetch the current count from the server
    fetch('/get_notification_count/')
        .then(response => response.json())
        .then(data => {
            const notificationCountElement = document.getElementById('notification-count');
            if (notificationCountElement) {
                // Update the notification count in the badge
                notificationCountElement.textContent = data.count;
            }
        })
        .catch(error => {
            console.error('Error fetching notification count:', error);
        });
}