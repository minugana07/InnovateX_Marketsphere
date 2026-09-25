/* =========================================================
   MARKET ASSESSMENT
========================================================= */

const marketSelect = document.getElementById("market");
const assessButton = document.getElementById("assess-button");


if (marketSelect && assessButton) {

    assessButton.addEventListener("click", async function () {

        const selectedMarket = marketSelect.value;


        if (!selectedMarket) {

            alert("Please select a market first.");

            return;
        }


        try {

            assessButton.disabled = true;

            assessButton.innerHTML = `
                Assessing...
            `;


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


            if (!response.ok) {

                throw new Error(
                    data.error || "Assessment failed."
                );

            }


            displayAssessment(data);


        } catch (error) {

            console.error("Assessment error:", error);

            alert(
                "Something went wrong while assessing the market."
            );


        } finally {

            assessButton.disabled = false;

            assessButton.innerHTML = `
                Assess Market
                <span>→</span>
            `;

        }

    });

}


/* =========================================================
   DISPLAY ASSESSMENT
========================================================= */

function displayAssessment(data) {

    const resultSection =
        document.createElement("section");


    resultSection.className =
        "assessment-result";


    resultSection.innerHTML = `

        <div class="result-header">

            <p class="section-label">
                ASSESSMENT RESULT
            </p>

            <h2>
                ${data.market}
            </h2>


            <div class="score-display">

                <span class="score">
                    ${data.overall_score}
                </span>

                <span class="score-label">
                    / 5.0
                </span>

            </div>


            <div class="status-badge">
                ${data.status}
            </div>

        </div>


        <div class="entry-approach">

            <p class="section-label">
                RECOMMENDED ENTRY APPROACH
            </p>

            <h3>
                ${data.entry_approach}
            </h3>

        </div>


        <div class="dimensions">

            <p class="section-label">
                REGULATORY DIMENSIONS
            </p>


            ${
                Object.entries(data.dimensions)
                .map(([name, details]) => `

                    <div class="dimension-row">

                        <div>

                            <strong>
                                ${name}
                            </strong>

                            <p>
                                ${details.reason}
                            </p>

                        </div>


                        <span class="dimension-score">
                            ${details.score}/5
                        </span>

                    </div>

                `)
                .join("")
            }

        </div>

    `;


    const existingResult =
        document.querySelector(".assessment-result");


    if (existingResult) {

        existingResult.remove();

    }


    const mainContainer =
        document.querySelector(".main-container");


    if (!mainContainer) {

        console.error(
            "Assessment result container not found."
        );

        return;

    }


    mainContainer.appendChild(resultSection);


    resultSection.scrollIntoView({

        behavior: "smooth",

        block: "start"

    });

}


/* =========================================================
   GEMINI PANEL
========================================================= */

const geminiButton =
    document.getElementById("gemini-button");

const geminiPanel =
    document.getElementById("gemini-panel");

const geminiClose =
    document.getElementById("gemini-close");


if (geminiButton && geminiPanel) {

    geminiButton.addEventListener(
        "click",
        function () {

            geminiPanel.classList.toggle("open");

        }
    );

}


if (geminiClose && geminiPanel) {

    geminiClose.addEventListener(
        "click",
        function () {

            geminiPanel.classList.remove("open");

        }
    );

}


/* =========================================================
   GEMINI SUGGESTIONS
========================================================= */

const geminiSuggestions =
    document.querySelectorAll(
        ".gemini-suggestion"
    );


const geminiInput =
    document.getElementById("gemini-input");


geminiSuggestions.forEach(
    function (suggestion) {

        suggestion.addEventListener(
            "click",
            function () {

                if (geminiInput) {

                    geminiInput.value =
                        suggestion.textContent.trim();

                    geminiInput.focus();

                }

            }
        );

    }
);


/* =========================================================
   GEMINI INPUT
========================================================= */

const geminiSend =
    document.getElementById("gemini-send");


if (geminiSend && geminiInput) {

    geminiSend.addEventListener(
        "click",
        function () {

            const question =
                geminiInput.value.trim();


            if (!question) {

                return;

            }


            /*
             * Gemini backend connection will be added later.
             * For now, keep the interface ready.
             */

            console.log(
                "Gemini question:",
                question
            );

        }
    );


    geminiInput.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Enter") {

                geminiSend.click();

            }

        }
    );

}