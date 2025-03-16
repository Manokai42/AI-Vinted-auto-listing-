document.getElementById('listingForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;
    
    const response = await fetch('/generate-listing', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description, price })
    });
    
    const result = await response.json();
    document.getElementById('result').innerText = result.listing || 'Error generating listing.';
});