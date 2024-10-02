// Get the canvas contexts for both graphs
const barCtx = document.getElementById('moodBarGraph').getContext('2d');
const lineCtx = document.getElementById('moodLineGraph').getContext('2d');

// Sample emotions and timestamps
const emotions = ['Joy', 'Neutral', 'Neutral', 'Sadness', 'Neutral', 'Joy', 'Neutral'];
const timestamps = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

console.log("Emotions:", emotions);
console.log("Timestamps:", timestamps);

// Function to map emotions to numeric values
const emotionToValue = (emotion) => {
    switch (emotion) {
        case 'Joy': return 5;
        case 'Neutral': return 3;
        case 'Sadness': return 1;
        case 'Anger': return 2;
        case 'Fear': return 4;
        default: return 0;
    }
};

// Bar graph configuration
const moodBarGraph = new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: timestamps,  // The time data for x-axis
        datasets: [{
            label: 'Mood Over Time',
            data: emotions.map(emotionToValue),  // Map emotions to numeric values
            backgroundColor: 'rgba(75, 192, 192, 0.2)',  // Set bar fill color
            borderColor: 'rgba(75, 192, 192, 1)',  // Set bar border color
            borderWidth: 1  // Width of bar borders
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    // Show labels for the emotions
                    callback: function (value) {
                        const labels = ['Unknown', 'Sadness', 'Anger', 'Neutral', 'Fear', 'Joy'];
                        return labels[value];
                    }
                }
            }
        }
    }
});

// Line graph configuration
const moodLineGraph = new Chart(lineCtx, {
    type: 'line',
    data: {
        labels: timestamps,  // The time data for x-axis
        datasets: [{
            label: 'Mood Over Time',
            data: emotions.map(emotionToValue),  // Map emotions to numeric values
            backgroundColor: 'rgba(75, 192, 192, 0.2)',  // Set line fill color
            borderColor: 'rgba(75, 192, 192, 1)',  // Set line color
            borderWidth: 2,  // Width of line
            fill: false  // Disable fill under line
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    // Show labels for the emotions
                    callback: function (value) {
                        const labels = ['Unknown', 'Sadness', 'Anger', 'Neutral', 'Fear', 'Joy'];
                        return labels[value];
                    }
                }
            }
        }
    }
});
