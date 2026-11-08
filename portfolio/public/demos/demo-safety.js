document.addEventListener('submit', function(event) {
  event.preventDefault();
  let status = event.target.querySelector('[data-demo-status]');
  if (!status) { status = document.createElement('p'); status.dataset.demoStatus=''; status.setAttribute('role','status'); event.target.appendChild(status); }
  status.textContent='Demonstration only. Nothing was sent or saved.';
}, true);
