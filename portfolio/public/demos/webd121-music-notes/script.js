const dateButton = document.querySelector("[data-date-trigger]");
const dateOutput = document.querySelector("[data-date-output]");
const quoteButton = document.querySelector("[data-quote-trigger]");
const quoteOutput = document.querySelector("[data-quote-output]");
const quizForm = document.querySelector("[data-quiz-form]");
const quizOutput = document.querySelector("[data-quiz-output]");

if (dateButton && dateOutput) {
    dateButton.addEventListener("click", () => {
        dateOutput.textContent = new Date().toLocaleString();
    });
}

if (quoteButton && quoteOutput) {
    quoteButton.addEventListener("click", () => {
        quoteOutput.textContent = "People never change. They just become better at hiding who they really are.";
    });
}

if (quizForm && quizOutput) {
    quizForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const data = new FormData(quizForm);
        const laterAlbums = data.getAll("laterAlbum");
        const services = data.getAll("streamingService");
        const favoriteSong = data.get("favoriteSong") || "No song selected";
        const favoriteFeature = data.get("favoriteFeature") || "No feature selected";
        const earlyAlbum = data.get("earlyAlbum") || "No early album selected";
        const liveMemory = data.get("liveMemory") || "No live memory added";

        quizOutput.innerHTML = `
            <ul>
                <li><strong>Favorite song:</strong> ${escapeHtml(favoriteSong)}</li>
                <li><strong>Favorite feature:</strong> ${escapeHtml(favoriteFeature)}</li>
                <li><strong>Early album:</strong> ${escapeHtml(earlyAlbum)}</li>
                <li><strong>Later albums:</strong> ${escapeHtml(laterAlbums.join(", ") || "None selected")}</li>
                <li><strong>Streaming:</strong> ${escapeHtml(services.join(", ") || "None selected")}</li>
                <li><strong>Live memory:</strong> ${escapeHtml(liveMemory)}</li>
            </ul>
        `;
    });

    quizForm.addEventListener("reset", () => {
        quizOutput.innerHTML = "<p>Submit the form to see your listening profile here.</p>";
    });
}

function escapeHtml(value) {
    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}
