document.getElementById("predictForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const age = document.getElementById("age").value;
    const likesSweet = document.getElementById("likes_sweet").value;
    const color = document.getElementById("color").value;

    const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ age, likes_sweet: likesSweet, color })
    });

    const data = await response.json();
    document.getElementById("result").innerText = `Prediction: You prefer ${data.prediction}!`;
});
