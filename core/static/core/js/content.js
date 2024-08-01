document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector("#gallery-container")) {
        const images = document.querySelectorAll('.image-section');
        const prevButton = document.getElementById('prev-button');
        const nextButton = document.getElementById('next-button');
        const sliding = document.querySelector(".content-slider");
        const btnLength = images.length;
        const estimatedValue = 0;
        // console.log(estimatedValue);
        let curIndex = estimatedValue;
        let intervalId;

        function showImage() {
            const transValue = -curIndex * 100 + "vw";
            sliding.style.transform = "translateX(" + transValue + ")";
        }

        function nextSlide() {
            curIndex++;
            if (curIndex > btnLength - 1) {
                curIndex = -estimatedValue;
            }
            showImage();
        }

        function prevSlide() {
            curIndex--;
            if (curIndex < -estimatedValue) {
                curIndex = btnLength - 1;
            }
            showImage();
        }

        prevButton.addEventListener('click', () => {
            clearInterval(intervalId);
            prevSlide();
            intervalId = setInterval(nextSlide, 5000);
        });

        nextButton.addEventListener('click', () => {
            clearInterval(intervalId);
            nextSlide();
            intervalId = setInterval(nextSlide, 5000);
        });

        // Initialize the slider position
        showImage();

        // Set up the automatic slide change
        intervalId = setInterval(nextSlide, 5000);
    } else {
        // Do nothing
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const textContainers = document.querySelectorAll(".text-content");
    const tableContainers = document.getElementsByTagName('td');

    if (document.getElementById("popup")) {
        const popup = document.getElementById("popup");
        const popupContent = document.getElementById("popup-content");
        const popupAddImage = document.getElementById("popup-image");
        const popupClose = document.getElementById("popup-close");
        const overlay = document.getElementById("overlay");
        
        textContainers.forEach(function(textContainer) {
            var fullTextData = textContainer.getElementsByClassName('full-text-data');
            popupAddImage.style.display = "none";

            if (fullTextData.length > 0) {
                fullTextData = fullTextData[0].textContent;
                textContainer.setAttribute('data-fulltext', fullTextData);
            }

            textContainer.addEventListener("click", function() {
                popupContent.textContent = fullTextData;
                popup.style.display = "block";
                overlay.style.display = "block";
            });
        });
        
        Array.prototype.forEach.call(tableContainers, function(tableContainer) {
            var fullText = tableContainer.textContent;
            popupAddImage.style.display = "none";
            if (fullText.length >= 30) {
                tableContainer.addEventListener("click", function() {
                    popupContent.textContent = fullText;
                    popup.style.display = "block";
                    overlay.style.display = "block";
                });
            }
        });

        if (document.getElementById("popup-div")) {
            const popupImage = document.getElementById("popup-div");
            var imageUrl = popupImage.getAttribute("data-image-url");
            var admission = popupImage.getAttribute("data-link");
            var imageTag = popupImage.getElementsByClassName('full-text-data');
            var imageAlt = popupImage.getAttribute("data-image-alt");
            var newImageTag = document.createElement("img");
            var ahref = document.createElement("a");
            ahref.href = admission;
            ahref.textContent = "Apply Now";
            newImageTag.src = imageUrl;
            newImageTag.alt = imageAlt;
            popupAddImage.appendChild(newImageTag);
            popupContent.textContent = imageTag[0].textContent;
            popupContent.appendChild(ahref);
            popupAddImage.style.display = "block";
            popup.style.display = "flex";
            popup.style.flexDirection = "column";
            popup.style.justifyContent = "center";
            popup.style.alignContent = "center";
            overlay.style.display = "block";
        };

        popupClose.addEventListener("click", function() {
            popup.style.display = "none";
            overlay.style.display = "none";
            popupAddImage.style.display = "none";
        });

        overlay.addEventListener("click", function() {
            popup.style.display = "none";
            overlay.style.display = "none";
            popupAddImage.style.display = "none";
        });
    };
});

// Gallery swiping function
function gallery_image(swiper, content) {
    // console.log(content, swiper);
    if (document.querySelector("#gallery")) {
        
        const swiper = document.querySelector(swiper);
    
        const len = document.querySelectorAll(content).length;
        let est = 1/len;
        let currentIdx = 0;
        let count = 0;
        
        function nextSwipe() {
        currentIdx += est;
        count++;
        if (count >= len) {
            currentIdx= count = 0;
        }
        updateSwiper();
        }
    
        function updateSwiper() {
        const translateV = -currentIdx * 100 + "%";
        swiper.style.transform = "translateX(" + translateV + ")";
        }
    
        // Initialize the slider position
        updateSwiper();
    
        setInterval(nextSwipe, 5000); // Change slide every 5 seconds
    }  else {
        // Do nothing
    }
};

document.addEventListener("DOMContentLoaded", function () {
    if (document.getElementById("overview")){
        const overview = document.getElementById("overview");
        overview.style.display = "flex";
        overview.style.width = "100vw";
        overview.style.height = "100vh";
        overview.style.position = "relative";

        gallery_image(".gallery-image", ".gallery-content");
    };
})

function showSection(content, swiper_image, image_sector, section) {
    if (image_sector === "") {
        image_sector = '.img-content';
    }
    var selections = document.querySelectorAll(image_sector);
    selections.forEach(function(selection) {
        // selection.classList.remove('active');
        selection.style.display = "none";
    });
    var activeSection = document.getElementById(section);
    if (activeSection) {
        activeSection.style.display = "flex";
        // activeSection.classList.add('active');
    };
    gallery_image(content, swiper_image);
};

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('about-main')) {
        headers = document.querySelectorAll('.about-head-tag');
        headers.forEach(header => {
            header.addEventListener('click', () => {
                const content = header.nextElementSibling;
                if (content.style.display === "none" || content.style.display === "") {
                    content.style.display = "block";
                } else {
                    content.style.display = "none";
                }
            });
        });

        const container = document.getElementById('about-main');
        const items = Array.from(container.getElementsByClassName('about-main'));
        
        items.sort((a, b) => {
            return a.dataset.order - b.dataset.order;
        });

        items.forEach(item => {
            container.appendChild(item);
        });
    };
});