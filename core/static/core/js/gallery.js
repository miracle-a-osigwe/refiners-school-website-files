function changeImage(btnName) {
    // var imgElement = document.getElementById('displayedImage');
    console.log(btnName)
    if (btnName === 'reception') {
        image_type = 5;
    } else if (btnName === 'labs') {
        image_type = 4;
    } else if (btnName === 'primary') {
        image_type = 6;
    } else if (btnName === 'secondary') {
        image_type = 7;
    } else if (btnName === 'classes') {
        image_type = 8;
    } else if (btnName === 'workshop') {
        image_type = 9;
    } else if (btnName === 'sports') {
        image_type = 10;
    }
}
