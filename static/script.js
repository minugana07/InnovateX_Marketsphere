const marketSelect = document.getElementById("market");
const assessButton = document.getElementById("assess-button");

assessButton.addEventListener("click", async function () {

    const selectedMarket = marketSelect.value;

    if (!selectedMarket) {
        alert("Please select a market first.");
        return;
    }

    try {
        const response = await fetch("/assess", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                market: selectedMarket
            })
        });

        const data = await response.json();

        displayAssessment(data);

    } catch (error) {
        console.error("Error:", error);
    }
});

function displayAssessment(data) {

    const resultSection = document.createElement("section");

    resultSection.className = "assessment-result";

    resultSection.innerHTML = `
        <div class="result-header">
            <p class="section-label">ASSESSMENT RESULT</p>

            <h2>${data.market}</h2>

            <div class="score-display">
                <span class="score">${data.overall_score}</span>
                <span class="score-label">/ 5.0</span>
            </div>

            <div class="status-badge">
                ${data.status}
            </div>
        </div>

        <div class="entry-approach">
            <p class="section-label">RECOMMENDED ENTRY APPROACH</p>
            <h3>${data.entry_approach}</h3>
        </div>

        <div class="dimensions">
            <p class="section-label">REGULATORY DIMENSIONS</p>

            ${Object.entries(data.dimensions).map(([name, details]) => `
                <div class="dimension-row">
                    <div>
                        <strong>${name}</strong>
                        <p>${details.reason}</p>
                    </div>

                    <span class="dimension-score">
                        ${details.score}/5
                    </span>
                </div>
            `).join("")}
        </div>

        <div class="launch-gates">

        <p class="section-label">LAUNCH GATES</p>

        ${Object.entries(data.gates).map(([name, gate]) => `
            <div class="gate-row">

                <div class="gate-icon ${gate.status ? "gate-pass" : "gate-pending"}">
                    ${gate.status ? "✓" : "!"}
                </div>

                <div class="gate-content">
                    <strong>${name}</strong>
                    <p>${gate.reason}</p>
                </div>

                <span class="gate-status ${gate.status ? "status-ready" : "status-pending"}">
                    ${gate.status ? "SATISFIED" : "UNRESOLVED"}
                </span>

            </div>
        `).join("")}

    </div>
    `;

    const existingResult = document.querySelector(".assessment-result");

    if (existingResult) {
        existingResult.remove();
    }

    document.querySelector(".main-container").appendChild(resultSection);
}