const phishButton = document.querySelector("[data-phish-trigger]");
const phishTitle = document.querySelector("[data-phish-title]");
const phishOutput = document.querySelector("[data-phish-output]");
const alertPanel = document.querySelector(".alert-panel");

if (phishButton && phishTitle && phishOutput && alertPanel) {
    phishButton.addEventListener("click", () => {
        phishTitle.textContent = "Warning: fake urgency detected";
        phishOutput.innerHTML = "Your computer has a virus! Click this link immediately. A safer response is to pause, avoid the link, verify the sender, and report the message through the organization's security process.";
        alertPanel.classList.add("is-warning");
    });
}
