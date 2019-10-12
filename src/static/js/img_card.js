let ibs = document.querySelectorAll(".action-buttons > button.product-fader");
// body > div > div > div:nth-child(1) > div > div.txt-block > div > button
// let ibsArray = Array.from(ibs);
let overlays = document.querySelectorAll("div[id^='overlay_']");
// let overlaysArr = Array.from(overlays);

ibs.forEach(function(elem) {
    elem.addEventListener("click", function(e) {
        e.preventDefault();

        overlays.forEach(function(target) {
            if (target.dataset.cotarget === elem.dataset.coid) {
                $(target).fadeToggle("slow");
            }
        });
        
    });
});