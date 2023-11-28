document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('profileNames');
    const resultDiv = document.getElementById('result');
  
    fetch('https://http://127.0.0.1:5000/')
      .then(response => response.json())
      .then(profiles => {
        profiles.forEach(profile => {
          const option = document.createElement('option');
          option.text = profile.name;
          select.add(option);
        });
      });
  

    select.addEventListener('change', function () {
      const selectedName = select.options[select.selectedIndex].text;
  
      // Fetch approximate age
      fetch(`https://your-flask-endpoint/age?name=${selectedName}`)
        .then(response => response.text())
        .then(age => {
          resultDiv.innerText = `Approximate Age: ${age}`;
        });
    });
  });
  