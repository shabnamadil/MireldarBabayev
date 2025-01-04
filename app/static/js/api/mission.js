document.addEventListener("DOMContentLoaded", function() {
    // Select all mission-wrap elements
    const missionWraps = document.querySelectorAll(".mission-wrap");

    // Loop through each mission-wrap div
    missionWraps.forEach((missionWrap) => {
        // Select elements within the current mission-wrap
        const readMoreLink = missionWrap.querySelector(".readMoreLink");
        const showLessLink = missionWrap.querySelector(".showLessLink");
        const missionContent = missionWrap.querySelector(".missionContent");
        const fullMissionContent = missionWrap.querySelector(".fullMissionContent");

        // Show full content on "Read More" click
        readMoreLink.addEventListener("click", function(event) {
            event.preventDefault();
            missionContent.style.display = "none";
            fullMissionContent.style.display = "block";
            readMoreLink.style.display = "none";
            showLessLink.style.display = "inline";
        });

        // Show preview content on "Show Less" click
        showLessLink.addEventListener("click", function(event) {
            event.preventDefault();
            missionContent.style.display = "block";
            fullMissionContent.style.display = "none";
            readMoreLink.style.display = "inline";
            showLessLink.style.display = "none";
        });
    });
});
