const ctx = document.getElementById('moodGraph').getContext('2d');

// Sample emotions and timestamps
const emotions = ['Joy', 'Neutral', 'Neutral', 'Sadness', 'Neutral', 'Joy', 'Neutral'];
const timestamps = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

console.log("Emotions:", emotions);
console.log("Timestamps:", timestamps);

const moodGraph = new Chart(ctx, {
    type: 'bar',  // Chart type: bar
    data: {
        labels: timestamps,  // The time data for x-axis
        datasets: [{
            label: 'Mood Over Time',
            data: emotions.map(emotion => {
                switch (emotion) {
                    case 'Joy': return 5;
                    case 'Neutral': return 3;
                    case 'Sadness': return 1;
                    case 'Anger': return 2;
                    case 'Fear': return 4;
                    default: return 0;
                }
            }),  // Map emotions to numeric values
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
                    callback: function (value, index, values) {
                        const labels = ['Unknown', 'Sadness', 'Anger', 'Neutral', 'Fear', 'Joy'];
                        return labels[value];
                    }
                }
            }
        }
    }
});
