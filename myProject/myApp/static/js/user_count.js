// Function to update the user count badge
function updateUserCountBadge() {
    // Fetch total user count from the server
    fetch('/get_total_user_count/')
        .then(response => response.json())
        .then(data => {
            const userCountBadge = document.getElementById('user-count');
            if (userCountBadge) {
                // Update the user count in the badge
                userCountBadge.textContent = data.total_users;
            }
        })
        .catch(error => {
            console.error('Error fetching total user count:', error);
        });
}
