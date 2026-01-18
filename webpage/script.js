function login() {
  const user = document.getElementById("username").value.trim();
  const pass = document.getElementById("password").value.trim();

  if (user === "admin" && pass === "admin") {
    window.location.href = "predict.html";
  } else {
    document.getElementById("error").innerText =
      "Invalid username or password";
  }
}

function predict() {
  const payload = {
    inch: Number(document.getElementById("inch").value),
    ram: Number(document.getElementById("ram").value),
    weight: Number(document.getElementById("weight").value),
    total_memory: Number(document.getElementById("memory").value),
    cpu_tier: Number(document.getElementById("cpu").value),
    gpu_tier: Number(document.getElementById("gpu").value),
    total_pixels: Number(document.getElementById("pixels").value)
  };

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText =
      "Predicted Price: ₹ " + data.predicted_price.toFixed(2);
  })
  .catch(() => {
    document.getElementById("result").innerText =
      "Backend not reachable";
  });
}
