function loadPath() {
  const dummyData = {
    skills: { python: 2 },
    target_role: "data_scientist",
    time_per_week: 5
  };

  fetch("http://127.0.0.1:5000/assess", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dummyData)
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText =
      JSON.stringify(data, null, 2);
  });
}

