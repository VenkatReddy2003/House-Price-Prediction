document.getElementById('predictionForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const sqft = document.getElementById('sqft').value;
    const bhk = document.getElementById('bhk').value;
    const bathrooms = document.getElementById('bathrooms').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ location, sqft, bhk, bathrooms }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Estimated Price: ₹${data.price}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
