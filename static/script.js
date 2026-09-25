const marketSelect = document.getElementById("market");
const assessButton = document.getElementById("assess-button");

assessButton.addEventListener("click", function () {

    const selectedMarket = marketSelect.value;

    if (!selectedMarket) {
        alert("Please select a market first.");
        return;
    }

    alert("Assessment for " + marketSelect.options[marketSelect.selectedIndex].text + " will begin.");
});
